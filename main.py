from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

app = FastAPI()

# 用于存储传感器数据的简单数据库示例
db = []

class SensorData(BaseModel):
    sensor_id: str
    temperature: float
    humidity: float
    timestamp: datetime

@app.post("/data/upload/")
async def upload_data(data: SensorData):
    db.append(data)
    return {"message": "Data uploaded successfully"}

@app.get("/data/query/")
async def query_data(sensor_id: Optional[str] = None, start: Optional[str] = None, end: Optional[str] = None):
    result = db
    if sensor_id:
        result = [d for d in result if d.sensor_id == sensor_id]
    if start:
        start_date = datetime.fromisoformat(start)
        result = [d for d in result if d.timestamp >= start_date]
    if end:
        end_date = datetime.fromisoformat(end)
        result = [d for d in result if d.timestamp <= end_date]
    return result

class Device(BaseModel):
    device_id: str
    location: str
    sensors: List[str]

@app.post("/device/register/")
async def register_device(device: Device):
    # 这里只是简单地返回一个消息，实际应用中应将设备信息存储在数据库中
    return {"message": "Device registered successfully"}
