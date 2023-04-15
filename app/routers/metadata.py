from fastapi import APIRouter

router = APIRouter()


@router.get('/{ticker}/data', tags=['metadata'])
def get_ticket_metadata(ticker: str):
    return ticker
