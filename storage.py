#import the csv module to save machine readings to a CSV file
import csv
from pathlib import Path 

#function to save machine readings to a CSV file
def save_machine_readings(machines):
    csv_path = Path(__file__).resolve().parent / "machine_readings.csv"

    if csv_path.exists():
        file_has_data = csv_path.stat().st_size > 0
    else:
        file_has_data = False

    with open(csv_path, "a", newline="") as file:
        writer = csv.writer(file)
        if not file_has_data:
            writer.writerow(["Machine ID", "Machine Name", "Temperature", "Status"])

    for machine in machines:
        writer.writerow([
            machine["id"],
            machine["name"],
            machine["tempertature"],
            machine["status"]
        ])