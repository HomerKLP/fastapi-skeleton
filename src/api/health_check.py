from fastapi import APIRouter

router = APIRouter()


@router.get("/api/ping")
async def health_check():
    return "pong"
