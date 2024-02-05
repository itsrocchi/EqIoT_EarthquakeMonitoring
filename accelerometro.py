import random

# Costante di accelerazione dovuta alla gravità
g = 9.8

# Funzione per generare dati normali
def generate_normal_data_acc():
    x = random.uniform(0.1 * g, 0.4 * g)
    y = random.uniform(0.1 * g, 0.4 * g)
    z = random.uniform(0.1 * g, 0.4 * g)
    return x, y, z

# Funzione per generare dati allarmistici
def generate_alarm_data_acc():
    x = random.uniform(0.5 * g, 1 * g)
    y = random.uniform(0.5 * g, 1 * g)
    z = random.uniform(0.5 * g, 1 * g)
    return x, y, z
