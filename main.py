#import FastAPI and the generate_machine_readings function from the simulator module
from fastapi import FastAPI, HTTPException
from simulator import generate_machine_readings
import csv
from pathlib import Path 


#variable to hold the list of machines
app = FastAPI()


#function to return a welcome message when the root endpoint is accessed
@app.get("/")
def home():
    return {"message": "Industrial Equipment Monitor API"}

@app.get("/machines")
def get_machines():
    return generate_machine_readings()


#function to return the history of machine readings from the CSV file
@app.get("/machines/history")
def get_machine_history():
    csv_path = Path(__file__).resolve().parent / "machine_readings.csv"

    if not csv_path.exists():
        raise HTTPException(
            status_code=404,
            detail="Machine history file not found"
        )

    history = []

    with open(csv_path, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            history.append({
                "id": int(row["Machine ID"]),
                "name": row["Machine Name"],
                "temperature": int(row["Temperature"]),
                "status": row["Status"]
            })

    return history


#function to return the details of a specific machine by its ID
@app.get("/machines/{machine_id}")
def get_machine_by_id(machine_id: int):
    readings = generate_machine_readings()

    for machine in readings:
        if machine["id"] == machine_id:
            return machine

    raise HTTPException(
    status_code=404,
    detail="Machine not found"
)