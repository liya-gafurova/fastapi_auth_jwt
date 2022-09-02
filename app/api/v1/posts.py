from typing import List

from fastapi import APIRouter
from starlette import status
from starlette.responses import Response

from app.schemas.posts import PostRead

router = APIRouter()


@router.get('/', response_model=List[PostRead])
async def get_posts():
    return Response(status_code=status.HTTP_200_OK)
