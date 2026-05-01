from fastapi import FastAPI, Security, HTTPException, Depends
from fastapi.security import APIKeyHeader
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.database import init_db
from app.routers import loads, carrier, calls, metrics
from fastapi.staticfiles import StaticFiles

app = FastAPI(
    title="HappyRobot Carrier Sales API",
    description="API for inbound carrier load sales automation",
    version="1.0.0"
)

# CORS - necesario para que el dashboard pueda llamar a la API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Seguridad - API Key
api_key_header = APIKeyHeader(name="X-API-Key")


async def verify_api_key(api_key: str = Security(api_key_header)):
    if api_key != settings.API_KEY:
        raise HTTPException(status_code=403, detail="Invalid API key")
    return api_key


# Routers
app.include_router(
    loads.router,
    prefix="/api/loads",
    tags=["Loads"],
    dependencies=[Depends(verify_api_key)]
)
app.include_router(
    carrier.router,
    prefix="/api/carrier",
    tags=["Carrier"],
    dependencies=[Depends(verify_api_key)]
)
app.include_router(
    calls.router,
    prefix="/api/calls",
    tags=["Calls"],
    dependencies=[Depends(verify_api_key)]
)
app.include_router(
    metrics.router,
    prefix="/api/metrics",
    tags=["Metrics"],
    dependencies=[Depends(verify_api_key)]
)

app.mount("/dashboard", StaticFiles(directory="app/static", html=True), name="dashboard")

@app.on_event("startup")
def on_startup():
    init_db()


@app.get("/health")
def health_check():
    return {"status": "ok"}