from app.database import init_db, SessionLocal
from app.models import Load, Call
from datetime import datetime, timedelta
import random

def seed_loads(db):
    loads = [
        {
            "load_id": "LD-1001",
            "origin": "Chicago, IL",
            "destination": "Dallas, TX",
            "pickup_datetime": datetime.now() + timedelta(days=1),
            "delivery_datetime": datetime.now() + timedelta(days=3),
            "equipment_type": "Dry Van",
            "loadboard_rate": 2500.00,
            "notes": "No hazmat. Dock delivery.",
            "weight": 42000,
            "commodity_type": "Electronics",
            "num_of_pieces": 24,
            "miles": 920,
            "dimensions": "48x40x48"
        },
        {
            "load_id": "LD-1002",
            "origin": "Chicago, IL",
            "destination": "Atlanta, GA",
            "pickup_datetime": datetime.now() + timedelta(days=2),
            "delivery_datetime": datetime.now() + timedelta(days=4),
            "equipment_type": "Reefer",
            "loadboard_rate": 3200.00,
            "notes": "Temperature controlled. Keep at 34F.",
            "weight": 38000,
            "commodity_type": "Frozen Food",
            "num_of_pieces": 18,
            "miles": 716,
            "dimensions": "48x40x60"
        },
        {
            "load_id": "LD-1003",
            "origin": "Los Angeles, CA",
            "destination": "Phoenix, AZ",
            "pickup_datetime": datetime.now() + timedelta(days=1),
            "delivery_datetime": datetime.now() + timedelta(days=2),
            "equipment_type": "Flatbed",
            "loadboard_rate": 1800.00,
            "notes": "Tarps required. Oversized load.",
            "weight": 44000,
            "commodity_type": "Steel Beams",
            "num_of_pieces": 6,
            "miles": 373,
            "dimensions": "60x12x12"
        },
        {
            "load_id": "LD-1004",
            "origin": "Dallas, TX",
            "destination": "Miami, FL",
            "pickup_datetime": datetime.now() + timedelta(days=3),
            "delivery_datetime": datetime.now() + timedelta(days=5),
            "equipment_type": "Dry Van",
            "loadboard_rate": 2800.00,
            "notes": "Liftgate required at delivery.",
            "weight": 35000,
            "commodity_type": "Furniture",
            "num_of_pieces": 40,
            "miles": 1312,
            "dimensions": "48x40x72"
        },
        {
            "load_id": "LD-1005",
            "origin": "Atlanta, GA",
            "destination": "New York, NY",
            "pickup_datetime": datetime.now() + timedelta(days=2),
            "delivery_datetime": datetime.now() + timedelta(days=4),
            "equipment_type": "Dry Van",
            "loadboard_rate": 2200.00,
            "notes": "Appointment required. Call 30 min before.",
            "weight": 30000,
            "commodity_type": "Paper Products",
            "num_of_pieces": 30,
            "miles": 868,
            "dimensions": "48x40x48"
        },
        {
            "load_id": "LD-1006",
            "origin": "Houston, TX",
            "destination": "Chicago, IL",
            "pickup_datetime": datetime.now() + timedelta(days=1),
            "delivery_datetime": datetime.now() + timedelta(days=3),
            "equipment_type": "Reefer",
            "loadboard_rate": 3500.00,
            "notes": "Temp 0F. Frozen pharmaceuticals.",
            "weight": 28000,
            "commodity_type": "Pharmaceuticals",
            "num_of_pieces": 12,
            "miles": 1091,
            "dimensions": "48x40x48"
        },
        {
            "load_id": "LD-1007",
            "origin": "Denver, CO",
            "destination": "Los Angeles, CA",
            "pickup_datetime": datetime.now() + timedelta(days=4),
            "delivery_datetime": datetime.now() + timedelta(days=6),
            "equipment_type": "Flatbed",
            "loadboard_rate": 2600.00,
            "notes": "Chains and binders required.",
            "weight": 46000,
            "commodity_type": "Machinery",
            "num_of_pieces": 3,
            "miles": 1018,
            "dimensions": "72x48x60"
        },
        {
            "load_id": "LD-1008",
            "origin": "Seattle, WA",
            "destination": "San Francisco, CA",
            "pickup_datetime": datetime.now() + timedelta(days=2),
            "delivery_datetime": datetime.now() + timedelta(days=3),
            "equipment_type": "Dry Van",
            "loadboard_rate": 1900.00,
            "notes": "Driver assist unload.",
            "weight": 25000,
            "commodity_type": "Consumer Goods",
            "num_of_pieces": 50,
            "miles": 808,
            "dimensions": "48x40x48"
        },
        {
            "load_id": "LD-1009",
            "origin": "Nashville, TN",
            "destination": "Charlotte, NC",
            "pickup_datetime": datetime.now() + timedelta(days=1),
            "delivery_datetime": datetime.now() + timedelta(days=2),
            "equipment_type": "Dry Van",
            "loadboard_rate": 1400.00,
            "notes": "FCFS. No appointment needed.",
            "weight": 22000,
            "commodity_type": "Auto Parts",
            "num_of_pieces": 15,
            "miles": 330,
            "dimensions": "48x40x36"
        },
        {
            "load_id": "LD-1010",
            "origin": "Chicago, IL",
            "destination": "Detroit, MI",
            "pickup_datetime": datetime.now() + timedelta(days=1),
            "delivery_datetime": datetime.now() + timedelta(days=2),
            "equipment_type": "Dry Van",
            "loadboard_rate": 1100.00,
            "notes": "Short haul. Same day possible.",
            "weight": 20000,
            "commodity_type": "Packaging Materials",
            "num_of_pieces": 60,
            "miles": 282,
            "dimensions": "48x40x48"
        },
        {
            "load_id": "LD-1011",
            "origin": "Miami, FL",
            "destination": "Houston, TX",
            "pickup_datetime": datetime.now() + timedelta(days=3),
            "delivery_datetime": datetime.now() + timedelta(days=5),
            "equipment_type": "Reefer",
            "loadboard_rate": 3100.00,
            "notes": "Temp 38F. Fresh produce.",
            "weight": 40000,
            "commodity_type": "Fresh Produce",
            "num_of_pieces": 22,
            "miles": 1187,
            "dimensions": "48x40x48"
        },
        {
            "load_id": "LD-1012",
            "origin": "Phoenix, AZ",
            "destination": "Denver, CO",
            "pickup_datetime": datetime.now() + timedelta(days=2),
            "delivery_datetime": datetime.now() + timedelta(days=4),
            "equipment_type": "Flatbed",
            "loadboard_rate": 2100.00,
            "notes": "Escort required for oversized.",
            "weight": 48000,
            "commodity_type": "Construction Materials",
            "num_of_pieces": 8,
            "miles": 602,
            "dimensions": "96x48x24"
        },
        {
            "load_id": "LD-1013",
            "origin": "New York, NY",
            "destination": "Boston, MA",
            "pickup_datetime": datetime.now() + timedelta(days=1),
            "delivery_datetime": datetime.now() + timedelta(days=2),
            "equipment_type": "Dry Van",
            "loadboard_rate": 950.00,
            "notes": "Residential delivery. Liftgate needed.",
            "weight": 15000,
            "commodity_type": "Medical Supplies",
            "num_of_pieces": 10,
            "miles": 215,
            "dimensions": "48x40x36"
        },
        {
            "load_id": "LD-1014",
            "origin": "San Francisco, CA",
            "destination": "Portland, OR",
            "pickup_datetime": datetime.now() + timedelta(days=3),
            "delivery_datetime": datetime.now() + timedelta(days=4),
            "equipment_type": "Dry Van",
            "loadboard_rate": 1600.00,
            "notes": "No weekend delivery.",
            "weight": 32000,
            "commodity_type": "Beverages",
            "num_of_pieces": 35,
            "miles": 636,
            "dimensions": "48x40x48"
        },
        {
            "load_id": "LD-1015",
            "origin": "Dallas, TX",
            "destination": "Nashville, TN",
            "pickup_datetime": datetime.now() + timedelta(days=2),
            "delivery_datetime": datetime.now() + timedelta(days=3),
            "equipment_type": "Dry Van",
            "loadboard_rate": 1750.00,
            "notes": "Palletized freight. No stack.",
            "weight": 36000,
            "commodity_type": "Textiles",
            "num_of_pieces": 28,
            "miles": 664,
            "dimensions": "48x40x48"
        },
        {
            "load_id": "LD-1016",
            "origin": "Los Angeles, CA",
            "destination": "Seattle, WA",
            "pickup_datetime": datetime.now() + timedelta(days=2),
            "delivery_datetime": datetime.now() + timedelta(days=4),
            "equipment_type": "Dry Van",
            "loadboard_rate": 2400.00,
            "notes": "No touch freight.",
            "weight": 34000,
            "commodity_type": "Apparel",
            "num_of_pieces": 45,
            "miles": 1135,
            "dimensions": "48x40x48"
        },
        {
            "load_id": "LD-1017",
            "origin": "Denver, CO",
            "destination": "Dallas, TX",
            "pickup_datetime": datetime.now() + timedelta(days=1),
            "delivery_datetime": datetime.now() + timedelta(days=3),
            "equipment_type": "Dry Van",
            "loadboard_rate": 1950.00,
            "notes": "Driver assist required.",
            "weight": 28000,
            "commodity_type": "Home Goods",
            "num_of_pieces": 20,
            "miles": 781,
            "dimensions": "48x40x60"
        },
        {
            "load_id": "LD-1018",
            "origin": "Atlanta, GA",
            "destination": "Miami, FL",
            "pickup_datetime": datetime.now() + timedelta(days=2),
            "delivery_datetime": datetime.now() + timedelta(days=3),
            "equipment_type": "Reefer",
            "loadboard_rate": 1800.00,
            "notes": "Temp 35F. Dairy products.",
            "weight": 38000,
            "commodity_type": "Dairy Products",
            "num_of_pieces": 16,
            "miles": 662,
            "dimensions": "48x40x48"
        },
        {
            "load_id": "LD-1019",
            "origin": "Houston, TX",
            "destination": "Atlanta, GA",
            "pickup_datetime": datetime.now() + timedelta(days=1),
            "delivery_datetime": datetime.now() + timedelta(days=3),
            "equipment_type": "Flatbed",
            "loadboard_rate": 2700.00,
            "notes": "Oversized permit needed.",
            "weight": 45000,
            "commodity_type": "Industrial Equipment",
            "num_of_pieces": 4,
            "miles": 789,
            "dimensions": "84x48x36"
        },
        {
            "load_id": "LD-1020",
            "origin": "New York, NY",
            "destination": "Chicago, IL",
            "pickup_datetime": datetime.now() + timedelta(days=2),
            "delivery_datetime": datetime.now() + timedelta(days=4),
            "equipment_type": "Dry Van",
            "loadboard_rate": 2600.00,
            "notes": "Appointment delivery. 2hr window.",
            "weight": 40000,
            "commodity_type": "Retail Goods",
            "num_of_pieces": 32,
            "miles": 790,
            "dimensions": "48x40x48"
        },
        {
            "load_id": "LD-1021",
            "origin": "San Francisco, CA",
            "destination": "Los Angeles, CA",
            "pickup_datetime": datetime.now() + timedelta(days=1),
            "delivery_datetime": datetime.now() + timedelta(days=2),
            "equipment_type": "Reefer",
            "loadboard_rate": 1200.00,
            "notes": "Temp 32F. Fresh fish.",
            "weight": 22000,
            "commodity_type": "Seafood",
            "num_of_pieces": 10,
            "miles": 382,
            "dimensions": "48x40x48"
        },
        {
            "load_id": "LD-1022",
            "origin": "Dallas, TX",
            "destination": "Denver, CO",
            "pickup_datetime": datetime.now() + timedelta(days=3),
            "delivery_datetime": datetime.now() + timedelta(days=5),
            "equipment_type": "Dry Van",
            "loadboard_rate": 2100.00,
            "notes": "Fragile goods. Handle with care.",
            "weight": 26000,
            "commodity_type": "Glassware",
            "num_of_pieces": 14,
            "miles": 781,
            "dimensions": "48x40x36"
        },
        {
            "load_id": "LD-1023",
            "origin": "Chicago, IL",
            "destination": "Nashville, TN",
            "pickup_datetime": datetime.now() + timedelta(days=1),
            "delivery_datetime": datetime.now() + timedelta(days=2),
            "equipment_type": "Dry Van",
            "loadboard_rate": 1500.00,
            "notes": "FCFS. No appointment.",
            "weight": 30000,
            "commodity_type": "Office Supplies",
            "num_of_pieces": 25,
            "miles": 473,
            "dimensions": "48x40x48"
        },
        {
            "load_id": "LD-1024",
            "origin": "Miami, FL",
            "destination": "New York, NY",
            "pickup_datetime": datetime.now() + timedelta(days=2),
            "delivery_datetime": datetime.now() + timedelta(days=4),
            "equipment_type": "Reefer",
            "loadboard_rate": 3400.00,
            "notes": "Temp 28F. Frozen meat.",
            "weight": 42000,
            "commodity_type": "Frozen Meat",
            "num_of_pieces": 20,
            "miles": 1280,
            "dimensions": "48x40x60"
        },
        {
            "load_id": "LD-1025",
            "origin": "Seattle, WA",
            "destination": "Denver, CO",
            "pickup_datetime": datetime.now() + timedelta(days=3),
            "delivery_datetime": datetime.now() + timedelta(days=5),
            "equipment_type": "Flatbed",
            "loadboard_rate": 2900.00,
            "notes": "Tarps and chains required.",
            "weight": 47000,
            "commodity_type": "Lumber",
            "num_of_pieces": 8,
            "miles": 1321,
            "dimensions": "96x48x12"
        },
    ]

    for load_data in loads:
        existing = db.query(Load).filter(Load.load_id == load_data["load_id"]).first()
        if not existing:
            db.add(Load(**load_data))
    
    db.commit()
    print(f"✓ {len(loads)} loads seeded")


def seed_calls(db):
    """Calls de ejemplo para que el dashboard tenga datos"""
    outcomes = ["accepted", "rejected", "no_loads", "carrier_not_eligible", "max_negotiations_reached"]
    sentiments = ["positive", "neutral", "negative"]
    mc_numbers = ["MC123456", "MC789012", "MC345678", "MC901234", "MC567890"]
    
    calls = []
    for i in range(25):
        outcome = random.choice(outcomes)
        initial_rate = random.uniform(1000, 4000)
        
        if outcome == "accepted":
            final_rate = initial_rate * random.uniform(0.85, 0.98)
            rounds = random.randint(1, 3)
        elif outcome == "max_negotiations_reached":
            final_rate = initial_rate * random.uniform(0.70, 0.84)
            rounds = 3
        else:
            final_rate = None
            rounds = random.randint(0, 2)

        calls.append(Call(
            carrier_name=f"Carrier {i+1} Trucking",
            mc_number=random.choice(mc_numbers),
            carrier_eligible="yes" if outcome != "carrier_not_eligible" else "no",
            load_id=f"LD-{1001 + (i % 15)}",
            initial_rate=round(initial_rate, 2),
            final_rate=round(final_rate, 2) if final_rate else None,
            negotiation_rounds=rounds,
            outcome=outcome,
            sentiment=random.choice(sentiments),
            notes=f"Sample call {i+1}",
            created_at=datetime.now() - timedelta(days=random.randint(0, 14))
        ))

    db.add_all(calls)
    db.commit()
    print(f"✓ {len(calls)} sample calls seeded")


def main():
    # Drop and recreate all tables for fresh seed
    from app.models import Base
    from app.database import engine
    Base.metadata.drop_all(bind=engine)
    
    init_db()
    db = SessionLocal()
    try:
        seed_loads(db)
        seed_calls(db)
        print("\n✓ Database seeded successfully!")
    finally:
        db.close()


if __name__ == "__main__":
    main()