#Import the random module to generate random temperatures for the machines
import random


#List of machine dictionaries
machines = [
    {"id": 1, "name": "Laser Welder"},
    {"id": 2, "name": "Conveyor"},
    {"id": 3, "name": "Cooling System"}
]


# Function to determine machine status
def get_machine_status(temperature):
    if temperature < 80:
        return "NORMAL"
    elif temperature < 100:
        return "WARNING"
    else:
        return "CRITICAL"


# Generate random temperatures and evaluate each machine
def generate_machine_readings():
    readings = []

    for machine in machines:
        temperature = random.randint(60, 110)

        readings.append({
            "id": machine["id"],
            "name": machine["name"],
            "temperature": temperature,
            "status": get_machine_status(temperature)
        })

    return readings


# Function to return the list of machines that are in a critical state
def get_critical_machines(machines):
    high_temp = []

    for machine in machines:
        if machine["temperature"] >= 100:
            high_temp.append(machine)

    return high_temp