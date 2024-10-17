from fastapi import APIRouter, Depends

from analyze.analyze_service import analyze_image
from auth.auth_service import check_user
from analyze.dto.analyze_dto import AnalyzeRequestDTO
router = APIRouter(prefix="/analyze", tags=["analyze"])


@router.post("/analyze")
def analyze_product(request: AnalyzeRequestDTO, token: str = Depends(check_user)):
    return analyze_image(request.image)
