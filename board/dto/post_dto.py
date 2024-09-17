from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class PostCreateDTO(BaseModel):
    title: str
    content: str

class PostUpdateDTO(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None

class PostResponseDTO(BaseModel):
    id: int
    title: str
    content: str
    createdAt: datetime
    updatedAt: datetime

class PostListDTO(BaseModel):
    id: int
    title: str