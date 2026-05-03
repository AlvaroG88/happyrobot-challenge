from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models import Load
from app.schemas import LoadCreate, LoadResponse, LoadSearchRequest
from app.services.states import expand_search_terms
from sqlalchemy import or_ as db_or

router = APIRouter()


@router.post("/search", response_model=List[LoadResponse])
def search_loads(filters: LoadSearchRequest, db: Session = Depends(get_db)):
    query = db.query(Load)

    if filters.origin:
        terms = expand_search_terms(filters.origin)
        origin_filters = [Load.origin.ilike(f"%{t}%") for t in terms]
        query = query.filter(db_or(*origin_filters))

    if filters.destination:
        terms = expand_search_terms(filters.destination)
        dest_filters = [Load.destination.ilike(f"%{t}%") for t in terms]
        query = query.filter(db_or(*dest_filters))

    if filters.equipment_type:
        types = resolve_equipment(filters.equipment_type)
        equip_filters = [Load.equipment_type.ilike(f"%{t}%") for t in types]
        query = query.filter(db_or(*equip_filters))
    if filters.min_rate:
        query = query.filter(Load.loadboard_rate >= filters.min_rate)
    if filters.max_rate:
        query = query.filter(Load.loadboard_rate <= filters.max_rate)

    results = query.all()
    return results


@router.get("/", response_model=List[LoadResponse])
def list_loads(db: Session = Depends(get_db)):
    return db.query(Load).all()


@router.get("/{load_id}", response_model=LoadResponse)
def get_load(load_id: str, db: Session = Depends(get_db)):
    load = db.query(Load).filter(Load.load_id == load_id).first()
    if not load:
        raise HTTPException(status_code=404, detail="Load not found")
    return load


@router.post("/", response_model=LoadResponse, status_code=201)
def create_load(load: LoadCreate, db: Session = Depends(get_db)):
    existing = db.query(Load).filter(Load.load_id == load.load_id).first()
    if existing:
        raise HTTPException(status_code=409, detail="Load already exists")

    db_load = Load(**load.model_dump())
    db.add(db_load)
    db.commit()
    db.refresh(db_load)
    return db_load

from app.services.negotiation import evaluate_offer
from app.schemas import NegotiationRequest, NegotiationResponse


@router.post("/negotiate", response_model=NegotiationResponse)
def negotiate_load(request: NegotiationRequest, db: Session = Depends(get_db)):
    load = db.query(Load).filter(Load.load_id == request.load_id).first()
    if not load:
        raise HTTPException(status_code=404, detail="Load not found")

    result = evaluate_offer(
        loadboard_rate=load.loadboard_rate,
        carrier_offer=request.carrier_offer,
        current_round=request.current_round
    )
    return result
EQUIPMENT_MAP = {
    "dry van": ["dry van", "standard", "normal", "van"],
    "reefer": ["reefer", "refrigerated", "frigorifico", "frigorífico", "cold"],
    "flatbed": ["flatbed", "flat bed", "platform", "plataforma"],
}


def resolve_equipment(raw: str) -> list:
    lower = raw.lower().strip()
    for canonical, aliases in EQUIPMENT_MAP.items():
        if lower in aliases or lower == canonical:
            return [canonical]
    return [lower]