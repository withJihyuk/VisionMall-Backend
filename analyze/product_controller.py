from fastapi import APIRouter

from analyze.product_service import analyze_image
from auth.auth_service import check_user
from analyze.dto.product_dto import AnalyzeResponseDTO, AnalyzeRequestDTO

router = APIRouter(prefix="/analyze", tags=["analyze"])

@router.post("/analyze", response_model=AnalyzeResponseDTO)
async def get_products(request: AnalyzeRequestDTO):
    return analyze_image(AnalyzeRequestDTO.image)