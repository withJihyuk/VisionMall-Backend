from fastapi import APIRouter

from analyze.analyze_service import analyze_image
from auth.auth_service import check_user
from analyze.dto.analyze_dto import AnalyzeResponseDTO, AnalyzeRequestDTO

router = APIRouter(prefix="/analyze", tags=["analyze"])


@router.post("/analyze", response_model=AnalyzeResponseDTO)
async def get_products(request: AnalyzeRequestDTO):
    return analyze_image(request.image)
