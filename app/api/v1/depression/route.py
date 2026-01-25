from fastapi import APIRouter
from .service import get_depression
from .schema import DepressionRequest

router = APIRouter()

@router.post("/depression", tags=["Depression"])
def assess_depression(data: DepressionRequest):
    return get_depression(data)

@router.get("/info", tags=["Depression"])
def info():
    return {"service": "Deression Assesment API", "version": "1.0"}

@router.delete("/depression", tags=["Depression"])
def delete_depression_record(record_id: int, data: DepressionUpdate):
    return {"service": "Deression Assesment API", "version": "1.0"}