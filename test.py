import json
import paho.mqtt.client as mqtt
# Define MQTT broker details
broker_address = "localhost"  # Replace with your broker's IP address or hostname
broker_port = 1883

# Create a MQTT client
client = mqtt.Client()

# Connect to the broker
client.connect(broker_address, broker_port)

# Create the message payload as a JSON
payload = {
    "x": 31,
    "y": 35,
    "z": 36
}

# Convert the payload to JSON string
message = json.dumps(payload)

# Publish the message to the topic
topic = "/zone1/accelerometer"
client.publish(topic, message)

# Disconnect from the broker
client.disconnect()