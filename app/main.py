import uvicorn
from fastapi import FastAPI
# Settings
from config import AppSettings
# Routers
from routers import metadata

settings = AppSettings()
app = FastAPI(
    title=settings.app_title,
    version=settings.version,
    contact=settings.contact_info,
)

app.include_router(metadata.router)


@app.get('/')
def welcome_hello() -> str:
    return "Hello World!"


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
