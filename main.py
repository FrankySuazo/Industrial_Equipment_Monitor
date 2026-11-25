#import FastAPI and the generate_machine_readings function from the simulator module
from fastapi import FastAPI, HTTPException
import csv
from pathlib import Path 
from simulator import generate_machine_readings, get_critical_machines
from storage import save_machine_readings


#variable to hold the list of machines
app = FastAPI()

readings = generate_machine_readings()


#function to return a welcome message when the root endpoint is accessed
@app.get("/")
def home():
    return {"message": "Industrial Equipment Monitor API"}

@app.get("/machines")
def get_machines():
    return readings


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


#function to return the list of machines that are in a critical state
@app.get("/machines/critical")
def get_critical_machine_readings():
    return get_critical_machines(readings)


#----------------- coment to be determined
@app.post("/machines/refresh")
def refresh_machine_readings():
    global readings

    # Generate new machine temperatures
    readings = generate_machine_readings()

    # Save the new readings to the CSV file
    save_machine_readings(readings)

    # Return the updated readings
    return readings

      
#function to return the details of a specific machine by its ID
@app.get("/machines/{machine_id}")
def get_machine_by_id(machine_id: int):

    for machine in readings:
        if machine["id"] == machine_id:
            return machine

    raise HTTPException(
        status_code=404,
        detail="Machine not found"
)


