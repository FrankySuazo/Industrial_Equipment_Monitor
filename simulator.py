import random

machines = [
    {"id": 1, "name": "Laser Welder"},
    {"id": 2, "name": "Conveyor"},
    {"id": 3, "name": "Cooling System"}
]

def get_machine_status(temperature):
    if temperature < 80:
        return "NORMAL"
    elif temperature < 100:
        return "WARNING"
    else:
        return "CRITICAL"


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

def get_critical_machines(machines):
    high_temp = []

    for machine in machines:
        if machine["temperature"] >= 100:
            high_temp.append(machine)

    return high_temp