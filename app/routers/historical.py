from fastapi import APIRouter
from internal.historical import Metadata

router = APIRouter()


@router.get('/{ticker}', tags=['Historical data'])
def get_ticker_metadata(
    ticker: str,
    interval: str,
    range: str
) -> dict:
    return Metadata(
        ticker=ticker,
        interval=interval,
        range=range
    ).fetch_data()
