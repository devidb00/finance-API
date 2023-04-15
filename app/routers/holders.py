from fastapi import APIRouter
from internal.holders import Holders

router = APIRouter()


@router.get('/{ticker}', tags=['Holders'])
def get_ticker_holders(
    ticker: str
) -> dict:
    return Holders(ticker=ticker).fetch_data()
