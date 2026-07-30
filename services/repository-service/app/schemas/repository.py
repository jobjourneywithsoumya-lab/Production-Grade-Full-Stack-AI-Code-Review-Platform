from pydantic import BaseModel, HttpUrl


class RepositoryCreate(BaseModel):
    name: str
    url: HttpUrl


class RepositoryResponse(BaseModel):
    id: int
    name: str
    url: HttpUrl

    model_config = {
        "from_attributes": True
    }