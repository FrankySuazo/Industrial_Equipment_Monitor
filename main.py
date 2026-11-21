from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Industrial Equipment Monitor API"}

@app.get("/machines")
def get_machines():
    return [
        {"id": 1, "name": "Laser Welder"},
        {"id": 2, "name": "Conveyor"},
        {"id": 3, "name": "Cooling System"}
    ]