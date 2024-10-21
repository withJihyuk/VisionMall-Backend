from pydantic import BaseModel


class AnalyzeRequestDTO(BaseModel):
    image: str
