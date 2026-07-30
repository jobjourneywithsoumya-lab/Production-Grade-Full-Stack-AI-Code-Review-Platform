from app.schemas.review import (
    ReviewRequest,
    ReviewResponse,
)


class ReviewService:

    def review_code(
        self,
        request: ReviewRequest,
    ) -> ReviewResponse:

        return ReviewResponse(
            summary="AI review not connected yet.",
            issues=[],
            suggestions=[],
        )