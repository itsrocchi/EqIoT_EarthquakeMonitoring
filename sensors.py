import accelerometro
import geofonoX,geofonoY
import paho.mqtt.client as mqtt
import random
import time

locations = {
    "north" : {
        "lat" : 5.4339,
        "long" : 8.8798
    },
    "south" : {
        "lat" : 5.4339,
        "long" : 8.8798
    },
    "west" : {
        "lat" : 5.4339,
        "long" : 8.8798
    },
    "east" : {
        "lat" : 5.4339,
        "long" : 8.8798
    }
}

mqtt_broker = "localhost"
mqtt_port = 1883
client = mqtt.Client()

def generate_send_Data(location):
    if random.random() < 0.7:
        generate_send_NormalValues(location=location)
    else:
        generate_send_BadValues(location=location)


def generate_send_BadValues(location):
    client.connect(mqtt_broker, mqtt_port, 60)

    lat = locations[location]["lat"]
    long = locations[location]["long"]
    
    acc_x,acc_y,acc_z = accelerometro.generate_alarm_data_acc()
    geo_X = geofonoX.generate_alarm_data_geoX()
    geo_Y = geofonoY.generate_alarm_data_geoY()
    
    accelerometer_topic = f"/{location}/accelerometer"
    geophone_X_topic = f"/{location}/geophone_X"
    geophone_Y_topic = f"/{location}/geophone_Y"
    latitude_topic =  f"/{location}/latitude"
    longitude_topic =  f"/{location}/longitude"
    
    client.publish(latitude_topic, f"{lat}")
    client.publish(longitude_topic, f"{long}")
    
    client.publish(accelerometer_topic, f"{acc_x},{acc_y},{acc_z}")
    client.publish(geophone_X_topic, f"{geo_X}")
    
    client.publish(geophone_Y_topic, f"{geo_Y}")
    
    client.disconnect()

def generate_send_NormalValues(location):
    client.connect(mqtt_broker, mqtt_port, 60)
    
    lat = locations[location]["lat"]
    long = locations[location]["long"]
    
    acc_x,acc_y,acc_z = accelerometro.generate_normal_data_acc()
    geo_X = geofonoX.generate_normal_data_geoX()
    geo_Y = geofonoY.generate_normal_data_geoY()
    
    accelerometer_topic = f"/{location}/accelerometer"
    geophone_X_topic = f"/{location}/geophone_X"
    geophone_Y_topic = f"/{location}/geophone_Y"
    
    latitude_topic =  f"/{location}/latitude"
    longitude_topic =  f"/{location}/longitude"
    
    client.publish(latitude_topic, f"{lat}")
    client.publish(longitude_topic, f"{long}")
    
    client.publish(accelerometer_topic, f"{acc_x},{acc_y},{acc_z}")
    client.publish(geophone_X_topic, f"{geo_X}")
    
    client.publish(geophone_Y_topic, f"{geo_Y}")
    
    client.disconnect()


while True:
    for location in locations:
        generate_send_Data(location=location)
    
    time.sleep(4)