#import the csv module to save machine readings to a CSV file
import csv
from pathlib import Path 

#function to save machine readings to a CSV file
def save_machine_readings(machines):
    csv_path = Path(__file__).resolve().parent / "machine_readings.csv"
