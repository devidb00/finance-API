from fastapi import APIRouter
from internal.real_time import RealTime

router = APIRouter()


@router.get('/{symbols}', tags=['Real time data - Current'])
def get_symbols_real_time_data(
    symbols: str
) -> dict:
    return RealTime(symbols=symbols).fetch_data()
