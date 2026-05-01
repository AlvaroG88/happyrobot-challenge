from fastapi import APIRouter
from app.schemas import CarrierVerifyRequest, CarrierVerifyResponse
from app.services.fmcsa import verify_carrier

router = APIRouter()


@router.post("/verify", response_model=CarrierVerifyResponse)
async def verify_carrier_endpoint(request: CarrierVerifyRequest):
    result = await verify_carrier(request.mc_number)
    return result