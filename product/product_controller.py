from typing import List

from fastapi import APIRouter, HTTPException
import product.product_service as product
from product.dto.product_dto import ProductResponseDTO, create_product_list

router = APIRouter(prefix="/product", tags=["product"])


@router.get("/products/{products_id}", response_model=ProductResponseDTO)
async def get_products(products_id: int):
    products = await product.get_product(products_id)
    if not products:
        raise HTTPException(status_code=404, detail="상품을 찾을 수 없어요.")
    return products


@router.get("/products", response_model=List[ProductResponseDTO])
async def get_all_products():
    return create_product_list(await product.get_all_product())
