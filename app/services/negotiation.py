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

    # Carrier wants MORE than loadboard rate - never accept above 110%
    if carrier_offer > loadboard_rate * 1.10:
        if current_round >= max_rounds:
            return {
                "accepted": False,
                "counter_offer": None,
                "message": f"We can't go above ${loadboard_rate:.2f}. Unfortunately we couldn't reach an agreement.",
                "round_number": current_round,
                "max_rounds_reached": True
            }
        counter = loadboard_rate * 1.05 if current_round == 1 else loadboard_rate
        return {
            "accepted": False,
            "counter_offer": counter,
            "message": f"We can't do ${carrier_offer:.2f}, but we can offer ${counter:.2f}.",
            "round_number": current_round,
            "max_rounds_reached": False
        }

    # Carrier offer is within acceptable range (90-110% of loadboard)
    if loadboard_rate * 0.90 <= carrier_offer <= loadboard_rate * 1.10:
        return {
            "accepted": True,
            "counter_offer": None,
            "message": f"Offer of ${carrier_offer:.2f} accepted. Transferring to a sales rep.",
            "round_number": current_round,
            "max_rounds_reached": False
        }

    # Carrier wants LESS than loadboard - always accept (broker pays less)
    return {
        "accepted": True,
        "counter_offer": None,
        "message": f"Offer of ${carrier_offer:.2f} accepted. Transferring to a sales rep.",
        "round_number": current_round,
        "max_rounds_reached": False
    }