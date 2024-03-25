from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

app = FastAPI()

# 用于存储传感器数据的简单数据库示例
db = []

class SensorData(BaseModel):
    """
    定义传感器数据模型。

    args:
        sensor_id (str): 传感器的唯一标识符。
        temperature (float): 传感器测量的温度值。
        humidity (float): 传感器测量的湿度值。
        timestamp (datetime): 数据的时间戳。

    这个模型用于接收和存储从传感器上传的数据。
    """
    sensor_id: str
    temperature: float
    humidity: float
    timestamp: datetime

@app.post("/data/upload/")
async def upload_data(data: SensorData):
    """
    处理传感器数据的上传。

    args:
        data (SensorData): 传感器数据对象，包含传感器ID、温度、湿度和时间戳。

    returns:
        dict: 包含操作消息的字典。

    当传感器数据上传到这个接口时，它将数据添加到简单数据库中。
    """
    db.append(data)
    return {"message": "Data uploaded successfully"}

@app.get("/data/query/")
async def query_data(sensor_id: Optional[str] = None, start: Optional[str] = None, end: Optional[str] = None):
    """
    根据传感器ID和时间范围查询传感器数据。

    args:
        sensor_id (Optional[str]): 要查询的传感器的ID。如果未提供，则返回所有传感器的数据。
        start (Optional[str]): 查询开始的时间（ISO格式）。如果未提供，不限制开始时间。
        end (Optional[str]): 查询结束的时间（ISO格式）。如果未提供，不限制结束时间。

    returns:
        List[SensorData]: 符合条件的传感器数据列表。

    此函数允许用户根据传感器ID和/或时间范围筛选数据。
    """
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
    """
    定义设备模型。

    args:
        device_id (str): 设备的唯一标识符。
        location (str): 设备所在位置的描述。
        sensors (List[str]): 设备上安装的传感器ID列表。

    这个模型用于接收和存储设备注册信息。
    """
    device_id: str
    location: str
    sensors: List[str]

@app.post("/device/register/")
async def register_device(device: Device):
    """
    处理设备的注册。

    args:
        device (Device): 设备对象，包含设备ID、位置和传感器列表。

    returns:
        dict: 包含操作消息的字典。

    这个接口用于设备的注册。在实际应用中，应将设备信息存储在数据库中。
    """
    # 这里只是简单地返回一个消息，实际应用中应将设备信息存储在数据库中
    return {"message": "Device registered successfully"}
