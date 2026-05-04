def evaluate_offer(loadboard_rate: float, carrier_offer: float, current_round: int) -> dict:
    if loadboard_rate <= 0:
        return {
            "accepted": False,
            "counter_offer": None,
            "message": "Invalid loadboard rate.",
            "round_number": current_round,
            "max_rounds_reached": False
        }

    max_rounds = 3

    # Carrier offer is at or below loadboard rate - great deal for broker
    if carrier_offer <= loadboard_rate:
        return {
            "accepted": True,
            "counter_offer": None,
            "message": f"Offer of ${carrier_offer:.2f} accepted. Transferring to a sales rep.",
            "round_number": current_round,
            "max_rounds_reached": False
        }

    # Carrier wants more than loadboard rate
    # Define max we can pay per round (increases each round)
    if current_round == 1:
        max_acceptable = loadboard_rate * 1.05
        counter = loadboard_rate * 1.05
    elif current_round == 2:
        max_acceptable = loadboard_rate * 1.10
        counter = loadboard_rate * 1.10
    else:
        max_acceptable = loadboard_rate * 1.15
        counter = None

    # Accept if carrier offer is within our max
    if carrier_offer <= max_acceptable:
        return {
            "accepted": True,
            "counter_offer": None,
            "message": f"Offer of ${carrier_offer:.2f} accepted. Transferring to a sales rep.",
            "round_number": current_round,
            "max_rounds_reached": current_round >= max_rounds
        }

    # Last round - reject
    if current_round >= max_rounds:
        final_max = loadboard_rate * 1.15
        return {
            "accepted": False,
            "counter_offer": None,
            "message": f"We can't go above ${final_max:.2f} on this one. Unfortunately we couldn't reach an agreement.",
            "round_number": current_round,
            "max_rounds_reached": True
        }

    # Counter offer - goes UP each round
    return {
        "accepted": False,
        "counter_offer": round(counter, 2),
        "message": f"We can't do ${carrier_offer:.2f}, but we can offer ${counter:.2f}.",
        "round_number": current_round,
        "max_rounds_reached": False
    }