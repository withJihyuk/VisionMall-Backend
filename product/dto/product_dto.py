from pydantic import BaseModel
from enum import Enum

class StatusEnum(str, Enum):
    ON_SALE = "ON_SALE"
    SOLD_OUT = "SOLD_OUT"

class ProductResponseDTO(BaseModel):
    id: int
    price: int
    rating: int
    status : StatusEnum
    title: str
    content: str
