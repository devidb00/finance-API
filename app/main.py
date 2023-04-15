import uvicorn
from fastapi import FastAPI
# Settings
from config import AppSettings
# Routers
from routers import historical, holders, real_time, profile

settings = AppSettings()
app = FastAPI(
    title=settings.app_title,
    version=settings.version,
    contact=settings.contact_info,
)

app.include_router(historical.router, prefix="/historical")
app.include_router(holders.router, prefix="/holders")
app.include_router(real_time.router, prefix="/current")
app.include_router(profile.router, prefix="/profile")

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
