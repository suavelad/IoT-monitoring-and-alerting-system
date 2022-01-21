# Import package
import paho.mqtt.client as mqtt
import json,requests
from django.core.mail import send_mail
from django.conf import settings

log_url ='http://localhost:8000/app/logs/'
send_email_url ='http://localhost:8000/app/send-email/'

# Define Variables
# MQTT_HOST = "iot.eclipse.org"
# MQTT_HOST = "broker.hivemq.com"
MQTT_HOST= "test.mosquitto.org"


MQTT_PORT = 1883
MQTT_KEEPALIVE_INTERVAL = 45
MQTT_TOPIC = "monitoring"

email = input ('Kindly insert the admin email that will receive the alert below:\n')
# subscribe to a Topic 
def on_connect(client, userdata, flags, rc):
    mqttc.subscribe(MQTT_TOPIC,2)

# Define on_message event function. 
# This function will be invoked every time,
# a new message arrives for the subscribed topic 
def on_message(mosq, obj, msg):
    payload_datax= msg.payload .decode("utf-8")
    payloadd = json.loads(payload_datax)    
    payloadd['mqtt_topic']= str(msg.topic)
    level=payloadd['level']
    
    # Save to DB via API call
    try:
        r= requests.post(log_url, json=payloadd, verify=False)
    except:
        None
    
    if level in ('error','critical'):
        # Send an alert message to the admin via email or any integrated means
        
        subject = f'SYSTEM MONITORING AND ALERT SYSTEM [{level}]'    
        message = f'Hi Admin, \nBelow is the status update of your IoT Device:\nDevice id: {payloadd["device_id"]}.\nAlert Level:  {level}\nMessage: Your device needs to be checked'
        # email= 'sunnexajayi@gmail.com'
        
        to_list = [email]
        email_payload={
            "senders": to_list,
            "message":message,
            "subject": subject
        }
        try:
            r= requests.post(send_email_url, json=email_payload, verify=False)
            print(r,r.status_code,r.json())
            if r.status_code ==200:
                print("Kindly check your mail for the alert")
        except:
            print("Error occurred while sending mail")
            None
        
          
def on_subscribe(mosq, obj, mid, granted_qos):
    print("Subscribed to Topic: " + 
    MQTT_TOPIC + " with QoS: " + str(granted_qos))
    

# Initiate MQTT Client
mqttc = mqtt.Client()

# Assign event callbacks
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_subscribe = on_subscribe

# Connect with MQTT Broker
mqttc.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL)

# Continue monitoring the incoming messages for subscribed topic
mqttc.loop_forever()