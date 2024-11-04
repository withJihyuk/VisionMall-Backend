from pydantic import BaseModel


class AnalyzeRequestDTO(BaseModel):
    image: str

class AnalyzeResponseDTO(BaseModel):
    result: str

def create_analyze_response(result_msg: str) -> AnalyzeResponseDTO:
    return AnalyzeResponseDTO(result=result_msg)