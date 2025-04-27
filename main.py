import asyncio
from fastapi import FastAPI
from pydantic import BaseModel
import simulation

app = FastAPI(title="Digital Twin Simulation")

class SetpointRequest(BaseModel):
    setpoint: float

@app.on_event("startup")
async def startup_event():
    asyncio.create_task(simulation.simulation_loop())

@app.get("/plant/state", tags=["Digital Twin"])
def get_plant_state():
    return simulation.state

@app.post("/plant/setpoint", tags=["Digital Twin"])
def set_plant_setpoint(request: SetpointRequest):
    simulation.state.setpoint = request.setpoint
    return {"setpoint": request.setpoint} 