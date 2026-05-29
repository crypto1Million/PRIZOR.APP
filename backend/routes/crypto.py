from fastapi import APIRouter

router = APIRouter()


@router.post("/wallet/connect")
def connect_wallet():

    return {
        "status": "connected"
    }