from pydantic import BaseModel


class AnalyzeRequestDTO(BaseModel):
    image: str

class AnalyzeResponseDTO(BaseModel):
    result: str