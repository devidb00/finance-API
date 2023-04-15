from fastapi import APIRouter
from internal.profile import Profile

router = APIRouter()


@router.get('/{ticker}', tags=['Profile'])
def get_ticker_profile(
    ticker: str
) -> dict:
    return Profile(ticker=ticker).fetch_data()
