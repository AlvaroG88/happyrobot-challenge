from pydantic import BaseModel
from typing import Optional
from datetime import datetime


# --- Loads ---

class LoadBase(BaseModel):
    origin: str
    destination: str
    pickup_datetime: datetime
    delivery_datetime: datetime
    equipment_type: str
    loadboard_rate: float
    notes: Optional[str] = ""
    weight: Optional[float] = None
    commodity_type: Optional[str] = None
    num_of_pieces: Optional[int] = None
    miles: Optional[float] = None
    dimensions: Optional[str] = None


class LoadCreate(LoadBase):
    load_id: str


class LoadResponse(LoadBase):
    load_id: str

    class Config:
        from_attributes = True


class LoadSearchRequest(BaseModel):
    origin: Optional[str] = None
    destination: Optional[str] = None
    equipment_type: Optional[str] = None
    min_rate: Optional[float] = None
    max_rate: Optional[float] = None


# --- Carrier ---

class CarrierVerifyRequest(BaseModel):
    mc_number: str


class CarrierVerifyResponse(BaseModel):
    mc_number: str
    legal_name: Optional[str] = None
    is_eligible: bool
    reason: str


# --- Calls ---

class CallCreate(BaseModel):
    carrier_name: Optional[str] = None
    mc_number: str
    carrier_eligible: Optional[str] = "pending"
    load_id: Optional[str] = None
    initial_rate: Optional[float] = None
    final_rate: Optional[float] = None
    negotiation_rounds: Optional[int] = 0
    outcome: Optional[str] = None
    sentiment: Optional[str] = None
    notes: Optional[str] = ""


class CallResponse(CallCreate):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


# --- Negotiation ---

class NegotiationRequest(BaseModel):
    load_id: str
    carrier_offer: float
    current_round: int


class NegotiationResponse(BaseModel):
    accepted: bool
    counter_offer: Optional[float] = None
    message: str
    round_number: int
    max_rounds_reached: bool


# --- Metrics ---

class MetricsResponse(BaseModel):
    total_calls: int
    accepted_calls: int
    rejected_calls: int
    acceptance_rate: float
    avg_negotiation_rounds: float
    avg_discount_percent: float
    sentiment_breakdown: dict
    outcome_breakdown: dict
    calls_over_time: list