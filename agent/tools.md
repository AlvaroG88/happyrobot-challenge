# HappyRobot HTTP Tools Configuration

Base URL: https://happyrobot-challenge-production-c876.up.railway.app
Headers for all tools: X-API-Key: hr-dev-key-2024

## Tool 1: verify_carrier
- Name: verify_carrier
- Description: Verify a carrier's MC number against the FMCSA database to check if they are authorized to operate.
- Method: POST
- URL: https://happyrobot-challenge-production-c876.up.railway.app/api/carrier/verify
- Headers: X-API-Key: hr-dev-key-2024, Content-Type: application/json
- Body:
{
  "mc_number": "{{mc_number}}"
}

## Tool 2: search_loads
- Name: search_loads
- Description: Search for available loads based on origin, destination, and equipment type.
- Method: POST
- URL: https://happyrobot-challenge-production-c876.up.railway.app/api/loads/search
- Headers: X-API-Key: hr-dev-key-2024, Content-Type: application/json
- Body:
{
  "origin": "{{origin}}",
  "destination": "{{destination}}",
  "equipment_type": "{{equipment_type}}"
}

## Tool 3: negotiate
- Name: negotiate
- Description: Evaluate a carrier's counter offer on a load. Returns whether to accept, counter-offer, or reject.
- Method: POST
- URL: https://happyrobot-challenge-production-c876.up.railway.app/api/loads/negotiate
- Headers: X-API-Key: hr-dev-key-2024, Content-Type: application/json
- Body:
{
  "load_id": "{{load_id}}",
  "carrier_offer": {{carrier_offer}},
  "current_round": {{current_round}}
}

## Tool 4: log_call
- Name: log_call
- Description: Record the details and outcome of a carrier call.
- Method: POST
- URL: https://happyrobot-challenge-production-c876.up.railway.app/api/calls/
- Headers: X-API-Key: hr-dev-key-2024, Content-Type: application/json
- Body:
{
  "carrier_name": "{{carrier_name}}",
  "mc_number": "{{mc_number}}",
  "carrier_eligible": "{{carrier_eligible}}",
  "load_id": "{{load_id}}",
  "initial_rate": {{initial_rate}},
  "final_rate": {{final_rate}},
  "negotiation_rounds": {{negotiation_rounds}},
  "outcome": "{{outcome}}",
  "sentiment": "{{sentiment}}",
  "notes": "{{notes}}"
}