import datetime
from typing import List

from fastapi import APIRouter, Depends
from starlette import status
from starlette.responses import Response

from app.api.dependencies import get_user_db
from app.api.utils import get_id
from app.api.v1.users import current_active_user
from app.models.users import User
from app.schemas.posts import PostRead, PostCreate, PostDB

router = APIRouter()


@router.get('/', response_model=List[PostRead])
async def get_posts(user: User = Depends(current_active_user)):
    return Response(status_code=status.HTTP_200_OK)


@router.post('/create/', response_model=PostRead)
async def create_post(post: PostCreate, user: User = Depends(current_active_user)):
    if post:
        print(post)

    created = PostDB(**post.dict(), created = datetime.datetime.now(), id=get_id())
    return created
