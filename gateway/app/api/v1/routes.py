from fastapi import APIRouter

from app.core.config import settings
from app.schemas.health import HealthResponse
from app.schemas.response import APIResponse

router = APIRouter(tags=["Gateway"])


@router.get(
    "/health",
    response_model=APIResponse,
    summary="Gateway Health Check",
)
async def health():

    return APIResponse(
        success=True,
        message="Gateway is healthy",
        data=HealthResponse(
            status="healthy",
            service=settings.APP_NAME,
            version=settings.API_VERSION,
        ),
    )