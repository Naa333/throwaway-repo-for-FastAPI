from fastapi import APIRouter
from datetime import datetime

router = APIRouter()

@router.get("/health")
def get_health():
    
    return datetime.now()