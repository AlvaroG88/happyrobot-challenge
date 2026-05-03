STATE_MAP = {
    "alabama": "AL", "alaska": "AK", "arizona": "AZ", "arkansas": "AR",
    "california": "CA", "colorado": "CO", "connecticut": "CT", "delaware": "DE",
    "florida": "FL", "georgia": "GA", "hawaii": "HI", "idaho": "ID",
    "illinois": "IL", "indiana": "IN", "iowa": "IA", "kansas": "KS",
    "kentucky": "KY", "louisiana": "LA", "maine": "ME", "maryland": "MD",
    "massachusetts": "MA", "michigan": "MI", "minnesota": "MN", "mississippi": "MS",
    "missouri": "MO", "montana": "MT", "nebraska": "NE", "nevada": "NV",
    "new hampshire": "NH", "new jersey": "NJ", "new mexico": "NM", "new york": "NY",
    "north carolina": "NC", "north dakota": "ND", "ohio": "OH", "oklahoma": "OK",
    "oregon": "OR", "pennsylvania": "PA", "rhode island": "RI", "south carolina": "SC",
    "south dakota": "SD", "tennessee": "TN", "texas": "TX", "utah": "UT",
    "vermont": "VT", "virginia": "VA", "washington": "WA", "west virginia": "WV",
    "wisconsin": "WI", "wyoming": "WY"
}


def expand_search_terms(location: str) -> list:
    """
    Given a location string, returns a list of search terms to try.
    E.g., "Illinois" -> ["Illinois", "IL"]
    E.g., "Chicago" -> ["Chicago"]
    """
    terms = [location]
    lower = location.lower().strip()

    # State name → abbreviation
    if lower in STATE_MAP:
        terms.append(STATE_MAP[lower])

    # Abbreviation → already short, add as-is
    if upper := location.upper().strip():
        if upper in STATE_MAP.values():
            # Find full name and add it
            for name, abbr in STATE_MAP.items():
                if abbr == upper:
                    terms.append(name.title())
                    break

    return terms