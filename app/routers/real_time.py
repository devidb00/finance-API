from fastapi import APIRouter
from internal.real_time import RealTime

router = APIRouter()


@router.get('/{symbols}/now', tags=['Real time data - Now'])
def get_symbols_real_time_data(
    symbols: str
) -> dict:
    return RealTime(symbols=symbols).fetch_data()
