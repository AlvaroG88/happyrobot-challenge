from sqlalchemy import Column, String, Float, Integer, DateTime, Text, Enum
from sqlalchemy.orm import declarative_base
import enum
from datetime import datetime

Base = declarative_base()


class CallOutcome(str, enum.Enum):
    ACCEPTED = "accepted"
    REJECTED = "rejected"
    NO_LOADS = "no_loads"
    CARRIER_NOT_ELIGIBLE = "carrier_not_eligible"
    MAX_NEGOTIATIONS = "max_negotiations_reached"


class CallSentiment(str, enum.Enum):
    POSITIVE = "positive"
    NEUTRAL = "neutral"
    NEGATIVE = "negative"


class Load(Base):
    __tablename__ = "loads"

    load_id = Column(String, primary_key=True)
    origin = Column(String, nullable=False)
    destination = Column(String, nullable=False)
    pickup_datetime = Column(DateTime, nullable=False)
    delivery_datetime = Column(DateTime, nullable=False)
    equipment_type = Column(String, nullable=False)
    loadboard_rate = Column(Float, nullable=False)
    notes = Column(Text, default="")
    weight = Column(Float, nullable=True)
    commodity_type = Column(String, nullable=True)
    num_of_pieces = Column(Integer, nullable=True)
    miles = Column(Float, nullable=True)
    dimensions = Column(String, nullable=True)


class Call(Base):
    __tablename__ = "calls"

    id = Column(Integer, primary_key=True, autoincrement=True)
    carrier_name = Column(String, nullable=True)
    mc_number = Column(String, nullable=False)
    carrier_eligible = Column(String, default="pending")
    load_id = Column(String, nullable=True)
    origin = Column(String, nullable=True)          # NUEVO
    destination = Column(String, nullable=True)      # NUEVO
    initial_rate = Column(Float, nullable=True)
    final_rate = Column(Float, nullable=True)
    negotiation_rounds = Column(Integer, default=0)
    outcome = Column(String, nullable=True)
    sentiment = Column(String, nullable=True)
    notes = Column(Text, default="")
    created_at = Column(DateTime, default=datetime.utcnow)