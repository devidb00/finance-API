from fastapi import APIRouter
from internal.metadata import Metadata

router = APIRouter()

@router.get('/{ticker}/data', tags=['metadata'])
def get_ticket_metadata(
    ticker: str,
    interval: str,
    range: str
) -> dict:
    return Metadata(
        ticker=ticker,
        interval=interval,
        range=range
    ).to_json()
