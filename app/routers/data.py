from fastapi import APIRouter
from ..models import SensorData

router = APIRouter()

@router.post("/upload/")
async def upload_data(data: SensorData):
    # 实现数据上传逻辑
    return {"message": "Data uploaded successfully"}

@router.get("/query/")
async def query_data():
    # 实现数据查询逻辑
    return {"message": "Data queried successfully"}
