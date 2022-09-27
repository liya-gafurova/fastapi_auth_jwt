import uvicorn
from fastapi import FastAPI
from starlette import status
from starlette.responses import Response

from app.api.v1.posts import router as posts_router
from app.api.v1.users import fastapi_users, auth_backend
from app.db.session import create_db_tables
from app.schemas.users import UserRead, UserCreate, UserUpdate

app = FastAPI()


@app.on_event('startup')
async def on_start_up():
    await create_db_tables()


@app.get('/root')
async def root():
    return Response(status_code=status.HTTP_200_OK)


app.include_router(router=posts_router, prefix='/posts', tags=['Posts'])

app.include_router(
    fastapi_users.get_auth_router(auth_backend), prefix="/auth/jwt", tags=["auth"]
)
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_reset_password_router(),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_verify_router(UserRead),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"],
)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", log_level="info")
