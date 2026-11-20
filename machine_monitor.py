machines = [
    {"id": 1, "name": "Laser Welder", "temperature": 72},
    {"id": 2, "name": "Conveyor", "temperature": 85},
    {"id": 3, "name": "Cooling System", "temperature": 105}
]
temperature = machines["temperature"]

if temperature < 80:
    print(f"Alarm: {machines['name']} is operating normally! Current temperature: {temperature}°C")
elif temperature < 100:
    print(f"WARNING: {machines['name']} temperature is elevated! Current temperature: {temperature}°C")
elif temperature >= 100:
    print(f"Alarm: {machines['name']} is in critical zone! Current temperature: {temperature}°C")

