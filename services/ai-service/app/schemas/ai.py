from pydantic import BaseModel


class AnalyzeRequest(BaseModel):
    filename: str
    language: str
    code: str


class AnalyzeResponse(BaseModel):
    review: str