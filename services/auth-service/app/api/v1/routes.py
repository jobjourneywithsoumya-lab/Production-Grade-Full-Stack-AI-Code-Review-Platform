from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.token import LoginRequest, Token
from app.dependencies.database import get_db
from app.schemas.user import UserCreate, UserResponse
from app.services.auth_service import AuthService

router = APIRouter()


@router.post(
    "/auth/register",
    response_model=UserResponse,
    status_code=201,
)
def register(
    user: UserCreate,
    db: Session = Depends(get_db),
):
    auth_service = AuthService(db)

    try:
        return auth_service.register(user)

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e),
        )

@router.post(
    "/auth/login",
    response_model=Token,
)
def login(
    request: LoginRequest,
    db: Session = Depends(get_db),
):
    auth_service = AuthService(db)

    try:
        return auth_service.login(
            request.email,
            request.password,
        )

    except ValueError as e:
        raise HTTPException(
            status_code=401,
            detail=str(e),
        )    