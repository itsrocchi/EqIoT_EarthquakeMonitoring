import paho.mqtt.client as mqtt
import random
import time

mqtt_broker = "mqtt.eclipse.org"
mqtt_port = 1883

# Identificativo del sensore e topic MQTT

sensori = ["nord","sud","ovest","est"]


# Costante di accelerazione dovuta alla gravità
g = 9.8

# Funzione per generare dati normali
def generate_normal_data():
    x = random.uniform(0.1 * g, 0.4 * g)
    y = random.uniform(0.1 * g, 0.4 * g)
    z = random.uniform(0.1 * g, 0.4 * g)
    return x, y, z

# Funzione per generare dati allarmistici
def generate_alarm_data():
    x = random.uniform(0.5 * g, 1 * g)
    y = random.uniform(0.5 * g, 1 * g)
    z = random.uniform(0.5 * g, 1 * g)
    return x, y, z

# Funzione per inviare dati attraverso MQTT
def send_data_to_mqtt(data, x):
    if (x < 0 | x > 3):
        print("Not a valid sensor")
    sensor_id = sensori[x]
    accelerometer_topic = f"/{sensor_id}/accelerometro"
    client = mqtt.Client()
    client.connect(mqtt_broker, mqtt_port, 60)
    client.publish(accelerometer_topic, f"{data[0]},{data[1]},{data[2]}")
    client.disconnect()

# Loop principale
while True:
    # Genera dati normali con probabilità del 70%
    if random.random() < 0.7:
        data = generate_normal_data()
    else:
        # Genera dati allarmistici con probabilità del 30%
        data = generate_alarm_data()

    # Invia i dati attraverso MQTT
    x = random.randint(0,3)
    send_data_to_mqtt(data)

    # Aspetta per un intervallo di tempo (ad esempio, 5 secondi) prima di generare il prossimo dato
    time.sleep(5)