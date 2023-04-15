import uvicorn
from fastapi import FastAPI

from routers import metadata

app = FastAPI(
    title="Yahoo Finance API",
    version="0.0.1",
    contact={
        "name": "Tarik ID BELLOUCH",
        "email": "tarik.id-bellouch@yucode.fr",
    },
)

app.include_router(metadata.router)


@app.get('/', description="Welcome buddy ;)")
def welcome_hello():
    return "Hello World!"


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
