# Imported modules
import random
import csv
import os

# List of machine dictionaries
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
for machine in machines:
    machine["temperature"] = random.randint(60, 110)
    machine["status"] = get_machine_status(machine["temperature"])

    # Display detailed machine status
    if machine["status"] == "NORMAL":
        print(f"{machine['name']} is operating normally! Current temperature: {machine['temperature']}°C | NORMAL")
    elif machine["status"] == "WARNING":
        print(f"{machine['name']} temperature is elevated! Current temperature: {machine['temperature']}°C | WARNING")
    else:
        print(f"{machine['name']} is in critical zone! Current temperature: {machine['temperature']}°C | CRITICAL")


# Check whether CSV already contains data
file_has_data = (
    os.path.exists("machine_readings.csv")
    and os.path.getsize("machine_readings.csv") > 0
)

# Save machine readings to CSV
with open("machine_readings.csv", "a", newline="") as file:
    writer = csv.writer(file)

    if not file_has_data:
        writer.writerow(["Machine ID", "Machine Name", "Temperature", "Status"])

    for machine in machines:
        writer.writerow([
            machine["id"],
            machine["name"],
            machine["temperature"],
            machine["status"]
        ])

# Read and display saved CSV records
with open("machine_readings.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(f"{row['Machine Name']} | {row['Temperature']}°C | {row['Status']}")
