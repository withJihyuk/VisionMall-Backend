from fastapi import APIRouter, Depends

from analyze.analyze_service import analyze_image
from analyze.dto.analyze_dto import AnalyzeRequestDTO, AnalyzeResponseDTO
from utils.token_handler import check_user

router = APIRouter(prefix="/analyze", tags=["analyze"])


@router.post("/analyze", response_model=AnalyzeResponseDTO)
def analyze_product(request: AnalyzeRequestDTO, user: str = Depends(check_user)):
    return analyze_image(request.image)
