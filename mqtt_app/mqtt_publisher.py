# Import package
import paho.mqtt.client as mqtt
import json

# Define Variables
# MQTT_HOST = "iot.eclipse.org"
# MQTT_HOST = "broker.hivemq.com"
MQTT_HOST= "test.mosquitto.org"
# MQTT_HOST = "localhost"
MQTT_PORT = 1883
MQTT_KEEPALIVE_INTERVAL = 45
MQTT_TOPIC = "monitoring"
# The IoT Device will send the alert data payload as json passed into MQTT_MSGX
MQTT_MSGX = json.dumps({
            "device_id": "2198ddec-97ef-463c-a517-a9b329d16fbc", 
            "location_id": "ddf18f83-3222-4cb8-bc78-9b5f2595c170",
            "message_id": "78310725-1919-47ad-acd8-94a7e4a8f6c8",
            "message": "some embedded IoT application message",
            "level": "error", 
            "timestamp": 1609927802 
            })

# Define on_publish event function
def on_publish(client, userdata, mid):
    print ("Message Published..."
)
# Initiate MQTT Client
mqttc = mqtt.Client()

# Register publish callback function
mqttc.on_publish = on_publish

# Connect with MQTT Broker
mqttc.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL) 

# Publish message to MQTT Broker 
mqttc.publish(MQTT_TOPIC,MQTT_MSGX)
print ('published')

# Disconnect from MQTT_Broker
mqttc.disconnect()