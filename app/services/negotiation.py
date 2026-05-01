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
    difference_percent = ((loadboard_rate - carrier_offer) / loadboard_rate) * 100

    # Oferta está muy cerca del rate - aceptar
    if carrier_offer >= loadboard_rate * 0.95:
        return {
            "accepted": True,
            "counter_offer": None,
            "message": f"Offer of ${carrier_offer:.2f} accepted. Transferring to a sales rep.",
            "round_number": current_round,
            "max_rounds_reached": False
        }

    # Última ronda
    if current_round >= max_rounds:
        if carrier_offer >= loadboard_rate * 0.85:
            return {
                "accepted": True,
                "counter_offer": None,
                "message": f"Offer of ${carrier_offer:.2f} accepted on final round. Transferring to a sales rep.",
                "round_number": current_round,
                "max_rounds_reached": True
            }
        else:
            return {
                "accepted": False,
                "counter_offer": None,
                "message": f"Unable to agree on a price. The best we can offer is ${loadboard_rate * 0.85:.2f}.",
                "round_number": current_round,
                "max_rounds_reached": True
            }

    # Rondas intermedias - contra-ofertar
    if current_round == 1:
        counter = loadboard_rate * 0.95
    else:
        counter = loadboard_rate * 0.90

    return {
        "accepted": False,
        "counter_offer": counter,
        "message": f"We can't do ${carrier_offer:.2f}, but we can offer ${counter:.2f}. What do you think?",
        "round_number": current_round,
        "max_rounds_reached": False
    }