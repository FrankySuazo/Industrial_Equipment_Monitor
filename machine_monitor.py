#Imported modules
import random
import csv
import os

#List and Dictionaries 
machines = [
    {"id": 1, "name": "Laser Welder"},
    {"id": 2, "name": "Conveyor"},
    {"id": 3, "name": "Cooling System"}
]
#Generate random temperature and status values for each machine
for machine in machines:
    machine['temperature'] = random.randint(60, 110)  # Random temperature between 60 and 110 degrees Celsius

#For loop to iterate through the machines and check their temperature status
for machine in machines:
    if machine['temperature'] < 80:
        machine['status'] = "NORMAL"
        print(f"{machine['name']} is operating normally! Current temperature: {machine['temperature']}°C | NORMAL")
    elif machine['temperature'] < 100:
        machine['status'] = "WARNING"
        print(f"{machine['name']} temperature is elevated! Current temperature: {machine['temperature']}°C | WARNING")
    else:
        machine['status'] = "CRITICAL"
        print(f"{machine['name']} is in critical zone! Current temperature: {machine['temperature']}°C | CRITICAL")

#Check if the CSV file exists and has data
file_has_data = (
    os.path.exists("machine_readings.csv")
    and os.path.getsize("machine_readings.csv") > 0
)

# To write CSV file with machine data
with open("machine_readings.csv", "a", newline='') as file:
    writer = csv.writer(file)

    #If the file does not have data, write the header row
    if not file_has_data:
        writer.writerow(["Machine ID", "Machine Name", "Temperature", "Status"])

    for machine in machines:
        writer.writerow([
            machine["id"],
            machine["name"],
            machine["temperature"],
            machine["status"]
    ])

#Read the CSV file and print its contents
with open("machine_readings.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(f"{row['Machine Name']} | {row['Temperature']}°C | {row['Status']}")       
