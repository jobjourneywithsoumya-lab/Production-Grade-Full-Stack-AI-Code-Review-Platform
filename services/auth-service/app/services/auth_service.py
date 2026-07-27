from sqlalchemy.orm import Session

from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate
from app.security.hashing import hash_password


class AuthService:

    def __init__(self):
        self.user_repository = UserRepository()

    def register_user(
        self,
        db: Session,
        user_data: UserCreate,
    ):
        existing_user = self.user_repository.get_by_email(
            db,
            user_data.email,
        )

        if existing_user:
            raise ValueError("Email already registered")

        user = User(
            username=user_data.username,
            email=user_data.email,
            hashed_password=hash_password(user_data.password),
        )

        return self.user_repository.create(
            db,
            user,
        )