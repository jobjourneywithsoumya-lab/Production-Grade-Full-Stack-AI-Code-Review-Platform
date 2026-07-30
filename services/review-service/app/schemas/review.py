from pydantic import BaseModel


class ReviewRequest(BaseModel):
    filename: str
    language: str
    code: str


class ReviewResponse(BaseModel):
    summary: str
    issues: list[str]
    suggestions: list[str]