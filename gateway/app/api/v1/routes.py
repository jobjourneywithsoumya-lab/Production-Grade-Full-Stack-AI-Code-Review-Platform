from fastapi import APIRouter

router = APIRouter()


@router.get(
    "/health",
    tags=["Health"],
    summary="Gateway Health Check",
)
async def health():

    return {
        "status": "healthy",
        "service": "gateway",
        "version": "v1"
    }