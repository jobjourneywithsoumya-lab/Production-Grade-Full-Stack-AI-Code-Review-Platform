from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.dependencies.database import get_db
from app.schemas.repository import (
    RepositoryCreate,
    RepositoryResponse,
)
from app.services.repository_service import RepositoryService

router = APIRouter()


@router.get("/")
def root():
    return {
        "service": "Repository Service",
        "status": "running",
    }


@router.post(
    "/repositories",
    response_model=RepositoryResponse,
    status_code=201,
)
def create_repository(
    repository: RepositoryCreate,
    db: Session = Depends(get_db),
):
    service = RepositoryService(db)

    try:
        return service.create(repository)

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e),
        )


@router.get(
    "/repositories",
    response_model=list[RepositoryResponse],
)
def get_repositories(
    db: Session = Depends(get_db),
):
    service = RepositoryService(db)
    return service.get_all()


@router.get(
    "/repositories/{repo_id}",
    response_model=RepositoryResponse,
)
def get_repository(
    repo_id: int,
    db: Session = Depends(get_db),
):
    service = RepositoryService(db)

    try:
        return service.get_by_id(repo_id)

    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e),
        )