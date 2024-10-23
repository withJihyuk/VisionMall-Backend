from pydantic import BaseModel
from typing import List, Optional
from enum import Enum


class StatusEnum(str, Enum):
    ON_SALE = "ON_SALE"
    SOLD_OUT = "SOLD_OUT"

class Option(BaseModel):
    id: int
    productId: int
    name: str
    shoulder: float
    towPiece: float
    chest: float
    sleeve: float

class ProductResponseDTO(BaseModel):
    id: int
    price: int
    rating: int
    status: Optional[StatusEnum]
    title: str
    content: str



def create_product_list(data_list: List[dict]) -> List[ProductResponseDTO]:
    return [
        ProductResponseDTO(
            id=item.id,
            price=item.price,
            rating=item.rating,
            status=item.status,
            title=item.title,
            content=item.content,
        )
        for item in data_list
    ]