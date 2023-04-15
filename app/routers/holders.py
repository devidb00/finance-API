from fastapi import APIRouter
from internal.holders import Holders

router = APIRouter()


@router.get('/{ticker}/holders', tags=['Holders'])
def get_ticker_metadata(
    ticker: str
) -> dict:
    return Holders(ticker=ticker).fetch_data()
