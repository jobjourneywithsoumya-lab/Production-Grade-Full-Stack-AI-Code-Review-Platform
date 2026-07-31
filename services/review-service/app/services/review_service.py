from app.repositories.review_repository import ReviewRepository


class ReviewService:

    def __init__(self, db):
        self.repository = ReviewRepository(db)

    def save_review(
        self,
        repository_id: int,
        review: str,
    ):
        return self.repository.create_review(
            repository_id,
            review,
        )