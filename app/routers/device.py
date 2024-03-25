from fastapi import APIRouter
from ..models import Device

router = APIRouter()

@router.post("/register/")
async def register_device(device: Device):
    # 实现设备注册逻辑
    return {"message": "Device registered successfully"}
