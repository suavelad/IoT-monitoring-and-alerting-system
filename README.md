
# IoT-monitoring-and-alerting-system
This is a sample project for sending log messages from a IOT device to a 
backend system using MQTT ( Broker, Subscriber and Publisher) with Django.



## Django Application:  iot_logger

This Django application was built to creating api for 

- a. storing the log messages from the mqtt_subscriber payload to the database
- b. sending email from the mqtt_subscriber  to alert the admin user
- c. that allows the clients have access to the logs generated
       

## MQTT : Here I made use of Mosquito and we have two major packages:

 a. Publisher: This is used to publish the iot message to the subscriber. Ideally, the publisher script should be deployed in the IoT device 
                    but for the test, I wrote a sample .py file for it called mqtt_publisher.py.
                    This can be run by  
                                   - i. activating the virtual environment   
                                   - ii. running mqtt_publisher.py file => python mqtt_publisher.py
                                  
  b.Subscriber: This is used to receive the published iot message based on the topic being listen to. For this project, it suppose to be deployed
                     on the server where the gotten payload is piped into a database  and also other activites and analysis can be done on the payload such
                     as email sending, push notifications .For the test, I wrote a sample .py file for it called mqtt_subscriber.py.
                    This can be run by  
                                   - i. activating the virtual environment   
                                   - ii. running mqtt_publisher.py file => python mqtt_subscriber.py
                     
                     
   * In production, the mqtt_subscriber.py should be converted to a daemon which runs on the background and added to systemctl 
      file which start automatically once the system is booted up.

 c. The Major engine that device it is a broker . I am making using of mosquitto for this project.
