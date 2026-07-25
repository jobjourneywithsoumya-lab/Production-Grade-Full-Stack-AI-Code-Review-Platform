from fastapi import APIRouter

from app.core.config import settings
from app.schemas.health import HealthResponse
from app.schemas.response import APIResponse

router = APIRouter(tags=["Auth Service"])


@router.get(
    "/health",
    response_model=APIResponse,
    summary="Auth Service Health Check",
)
async def health():
    return APIResponse(
        success=True,
        message="Auth Service is healthy",
        data=HealthResponse(
            status="healthy",
            service=settings.APP_NAME,
            version=settings.API_VERSION,
        ),
    )