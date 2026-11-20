#Imported modules
import random

#List and Dictionaries 
machines = [
    {"id": 1, "name": "Laser Welder"},
    {"id": 2, "name": "Conveyor"},
    {"id": 3, "name": "Cooling System"}
]
#Generate random temperature values for each machine
for machine in machines:
    machine['temperature'] = random.randint(60, 110)  # Random temperature between 60 and 110 degrees Celsius   

#For loop to iterate through the machines and check their temperature status
for machine in machines:
    if machine['temperature'] < 80:
        print(f"{machine['name']} is operating normally! Current temperature: {machine['temperature']}°C | NORMAL")
    elif machine['temperature'] < 100:
        print(f"{machine['name']} temperature is elevated! Current temperature: {machine['temperature']}°C | WARNING")
    else:
        print(f"{machine['name']} is in critical zone! Current temperature: {machine['temperature']}°C | CRITICAL")

