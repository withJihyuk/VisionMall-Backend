from fastapi import APIRouter

from analyze.analyze_service import analyze_image
from auth.auth_service import check_user
from analyze.dto.analyze_dto import AnalyzeRequestDTO

router = APIRouter(prefix="/analyze", tags=["analyze"])


@router.post("/analyze")
def get_products(request: AnalyzeRequestDTO):
    return analyze_image(request.image)
