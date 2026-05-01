import httpx
from app.config import settings


async def verify_carrier(mc_number: str) -> dict:
    """
    Verifica un carrier en la API pública de FMCSA.
    Docs: https://mobile.fmcsa.dot.gov/qc/services
    """
    base_url = "https://mobile.fmcsa.dot.gov/qc/services/carriers"
    
    # Limpiar el MC number (quitar prefijo MC si lo manda)
    clean_mc = mc_number.replace("MC", "").replace("mc", "").replace("-", "").strip()

    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get(
                f"{base_url}/docket-number/{clean_mc}",
                params={"webKey": settings.FMCSA_API_KEY},
                headers={"Accept": "application/json"}
            )

            if response.status_code != 200:
                return {
                    "mc_number": mc_number,
                    "legal_name": None,
                    "is_eligible": False,
                    "reason": "Carrier not found in FMCSA database"
                }

            data = response.json()
            content = data.get("content", [])

            if not content:
                return {
                    "mc_number": mc_number,
                    "legal_name": None,
                    "is_eligible": False,
                    "reason": "No records found for this MC number"
                }

            carrier = content[0].get("carrier", {})
            legal_name = carrier.get("legalName", "Unknown")
            status = carrier.get("allowedToOperate", "N")

            if status == "Y":
                return {
                    "mc_number": mc_number,
                    "legal_name": legal_name,
                    "is_eligible": True,
                    "reason": "Carrier is authorized to operate"
                }
            else:
                return {
                    "mc_number": mc_number,
                    "legal_name": legal_name,
                    "is_eligible": False,
                    "reason": f"Carrier not authorized. Status: {status}"
                }

    except httpx.TimeoutException:
        return {
            "mc_number": mc_number,
            "legal_name": None,
            "is_eligible": False,
            "reason": "FMCSA API timeout - try again later"
        }
    except Exception as e:
        return {
            "mc_number": mc_number,
            "legal_name": None,
            "is_eligible": False,
            "reason": f"Error verifying carrier: {str(e)}"
        }