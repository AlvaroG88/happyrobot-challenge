from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.database import get_db
from app.models import Call
from app.schemas import MetricsResponse

router = APIRouter()


@router.get("/", response_model=MetricsResponse)
def get_metrics(db: Session = Depends(get_db)):
    total_calls = db.query(Call).count()

    if total_calls == 0:
        return MetricsResponse(
            total_calls=0,
            accepted_calls=0,
            rejected_calls=0,
            acceptance_rate=0.0,
            avg_negotiation_rounds=0.0,
            avg_discount_percent=0.0,
            sentiment_breakdown={},
            outcome_breakdown={},
            calls_over_time=[]
        )

    # Conteos por outcome
    accepted = db.query(Call).filter(Call.outcome == "accepted").count()
    rejected = db.query(Call).filter(Call.outcome == "rejected").count()

    # Promedio de rondas de negociación
    avg_rounds = db.query(func.avg(Call.negotiation_rounds)).scalar() or 0

    # Promedio de descuento: diferencia entre initial_rate y final_rate
    calls_with_rates = db.query(Call).filter(
        Call.initial_rate.isnot(None),
        Call.final_rate.isnot(None),
        Call.initial_rate > 0
    ).all()

    if calls_with_rates:
        discounts = [
            ((c.initial_rate - c.final_rate) / c.initial_rate) * 100
            for c in calls_with_rates
        ]
        avg_discount = sum(discounts) / len(discounts)
    else:
        avg_discount = 0.0

    # Desglose de sentimiento
    sentiment_counts = (
        db.query(Call.sentiment, func.count(Call.id))
        .filter(Call.sentiment.isnot(None))
        .group_by(Call.sentiment)
        .all()
    )
    sentiment_breakdown = {s: c for s, c in sentiment_counts}

    # Desglose de outcome
    outcome_counts = (
        db.query(Call.outcome, func.count(Call.id))
        .filter(Call.outcome.isnot(None))
        .group_by(Call.outcome)
        .all()
    )
    outcome_breakdown = {o: c for o, c in outcome_counts}

    # Llamadas por día
    calls_by_day = (
        db.query(
            func.date(Call.created_at).label("date"),
            func.count(Call.id).label("count")
        )
        .group_by(func.date(Call.created_at))
        .order_by(func.date(Call.created_at))
        .all()
    )
    calls_over_time = [{"date": str(d), "count": c} for d, c in calls_by_day]

    return MetricsResponse(
        total_calls=total_calls,
        accepted_calls=accepted,
        rejected_calls=rejected,
        acceptance_rate=round((accepted / total_calls) * 100, 1),
        avg_negotiation_rounds=round(float(avg_rounds), 1),
        avg_discount_percent=round(avg_discount, 1),
        sentiment_breakdown=sentiment_breakdown,
        outcome_breakdown=outcome_breakdown,
        calls_over_time=calls_over_time
    )