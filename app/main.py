from fastapi import FastAPI
from .routers import data, device

app = FastAPI()

app.include_router(data.router, prefix="/data", tags=["data"])
app.include_router(device.router, prefix="/device", tags=["device"])
