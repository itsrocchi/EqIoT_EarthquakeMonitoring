import accelerometro
import geofonoX,geofonoY
import paho.mqtt.client as mqtt
import random
import time

locations = {
    "north" : {
        "lat" : 40.870116137628095,
        "long" : 14.120001469229564
    },
    "south" : {
        "lat" : 40.7710164666433, 
        "long" :14.131956697473646
    },
    "west" : {
        "lat" : 40.80120639546184, 
        "long" : 14.062120599402748
    },
    "east" : {
        "lat" : 40.79781894455775,
        "long" : 14.19665427977961
    }
}

mqtt_broker = "host.docker.internal"
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
    print("Data sent to broker. Waiting 4 seconds to send new data.")
    
    time.sleep(4)