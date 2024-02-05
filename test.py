import json
import paho.mqtt.client as mqtt
import random
# Define MQTT broker details
broker_address = "localhost"  # Replace with your broker's IP address or hostname
broker_port = 1883

# Create a MQTT client
client = mqtt.Client()

# Connect to the broker
client.connect(broker_address, broker_port)

# Create the message payload as a JSON
#
#    "x": 31,
#    "y": 35,
#    "z": 36
#}


def generate_data():
    latitudine = random.uniform(-90, 90)  # Intervallo per latitudine
    longitudine = random.uniform(-180, 180)  # Intervallo per longitudine
    magnitudo = random.uniform(1, 10)  # Intervallo per magnitudo

# Create the message payload as a JSON
    payload = {
        "latitudine": latitudine,
        "longitudine": longitudine,
        "magnitudo": magnitudo
    }
    return json.dumps(payload)

# Convert the payload to JSON string
message = generate_data()

# Publish the message to the topic
topic = "/zone1/accelerometer"
client.publish(topic, message)

# Disconnect from the broker
client.disconnect()