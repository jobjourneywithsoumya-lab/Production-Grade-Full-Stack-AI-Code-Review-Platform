from fastapi import APIRouter

from app.schemas.review import (
    ReviewRequest,
    ReviewResponse,
)
from app.services.review_service import ReviewService

router = APIRouter()

service = ReviewService()


@router.post(
    "/review",
    response_model=ReviewResponse,
)
def review_code(request: ReviewRequest):
    return service.review_code(request)