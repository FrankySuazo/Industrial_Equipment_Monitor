machines = [
    {"id": 1, "name": "Laser Welder", "temperature": 72},
    {"id": 2, "name": "Conveyor", "temperature": 85},
    {"id": 3, "name": "Cooling System", "temperature": 105}
]

for machine in machines:
    if machine['temperature'] < 80:
        print(f"{machine['name']} is operating normally! Current temperature: {machine['temperature']}°C | Alarm")
    elif machine['temperature'] < 100:
        print(f"{machine['name']} temperature is elevated! Current temperature: {machine['temperature']}°C | WARNING")
    elif machine['temperature'] >= 100:
        print(f"{machine['name']} is in critical zone! Current temperature: {machine['temperature']}°C | CRITICAL")
    else:
        print(f"{machine['name']} has an unknown status. Current temperature: {machine['temperature']}°C | UNKNOWN")

