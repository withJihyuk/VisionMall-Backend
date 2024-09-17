from fastapi import APIRouter, HTTPException
import board.board_service as board
from typing import List
from board.dto.post_dto import PostCreateDTO, PostUpdateDTO, PostResponseDTO, PostListDTO

router = APIRouter(prefix="/board", tags=["board"])

@router.post("/posts", response_model=PostResponseDTO)
async def create_post(request: PostCreateDTO):
    post = await board.create_post(request.title, request.content)
    return post

@router.get("/posts/{post_id}", response_model=PostResponseDTO)
async def get_post(post_id: int):
    post = await board.get_post(post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post

@router.get("/posts", response_model=List[PostResponseDTO])
async def get_all_posts():
    return await board.get_all_posts()

@router.put("/posts/{post_id}", response_model=PostResponseDTO)
async def update_post(post_id: int, request: PostUpdateDTO):
    post = await board.update_post(post_id, request.title, request.content)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post

@router.delete("/posts/{post_id}", response_model=PostResponseDTO)
async def delete_post(post_id: int):
    post = await board.delete_post(post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post