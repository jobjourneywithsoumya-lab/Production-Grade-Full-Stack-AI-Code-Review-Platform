from app.repositories.repository_repository import RepositoryRepository
from app.schemas.repository import (
    RepositoryCreate,
    RepositoryResponse,
)


class RepositoryService:
    def __init__(self, db):
        self.repository = RepositoryRepository(db)

    def create(self, repo: RepositoryCreate):
        existing = self.repository.get_by_url(str(repo.url))

        if existing:
            raise ValueError("Repository already exists")

        repository = self.repository.create_repository(
            name=repo.name,
            url=str(repo.url),
        )

        return RepositoryResponse.model_validate(repository)

    def get_all(self):
        return self.repository.get_all()

    def get_by_id(self, repo_id: int):
        repository = self.repository.get_by_id(repo_id)

        if repository is None:
            raise ValueError("Repository not found")

        return repository