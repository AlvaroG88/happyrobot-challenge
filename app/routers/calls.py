from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models import Call
from app.schemas import CallCreate, CallResponse

router = APIRouter()


@router.post("/", response_model=CallResponse, status_code=201)
def create_call(call: CallCreate, db: Session = Depends(get_db)):
    data = call.model_dump()

    # Convert numeric fields
    for field in ["initial_rate", "final_rate"]:
        val = data.get(field)
        if val is None or val == "" or val == "null":
            data[field] = None
        else:
            try:
                data[field] = float(val)
            except (ValueError, TypeError):
                data[field] = None

    val = data.get("negotiation_rounds")
    if val is None or val == "" or val == "null":
        data["negotiation_rounds"] = 0
    else:
        try:
            data["negotiation_rounds"] = int(val)
        except (ValueError, TypeError):
            data["negotiation_rounds"] = 0

    db_call = Call(**data)
    db.add(db_call)
    db.commit()
    db.refresh(db_call)
    return db_call


@router.get("/", response_model=List[CallResponse])
def list_calls(db: Session = Depends(get_db)):
    return db.query(Call).order_by(Call.created_at.desc()).all()


@router.get("/{call_id}", response_model=CallResponse)
def get_call(call_id: int, db: Session = Depends(get_db)):
    call = db.query(Call).filter(Call.id == call_id).first()
    if not call:
        raise HTTPException(status_code=404, detail="Call not found")
    return call


@router.patch("/{call_id}", response_model=CallResponse)
def update_call(call_id: int, call_update: CallCreate, db: Session = Depends(get_db)):
    call = db.query(Call).filter(Call.id == call_id).first()
    if not call:
        raise HTTPException(status_code=404, detail="Call not found")

    update_data = call_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(call, field, value)

    db.commit()
    db.refresh(call)
    return call