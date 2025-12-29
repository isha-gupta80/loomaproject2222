from fastapi import Cookie, HTTPException, Request, status

from app.core.config import settings
from app.schemas.user import UserOut
from app.services.auth import get_user_from_session


async def get_current_user(
    request: Request,
) -> UserOut:
    session_token = request.cookies.get(settings.SESSION_COOKIE_NAME)
    if not session_token:
        print("AUTH: Session token does not exist")
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "User not authorized.")
    user = await get_user_from_session(session_token)
    if not user:
        print("AUTH: User does not exist")
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "User not authorized.")

    return UserOut(**user.model_dump())

async def get_current_session(
    request: Request,
) -> str:

    # print("=" * 50)
    # print("REQUEST PATH:", request.url.path)
    # print("ALL COOKIES:", dict(request.cookies))
    # print("LOOKING FOR:", settings.SESSION_COOKIE_NAME)
    # print("=" * 50)
    #
    session_token = request.cookies.get(settings.SESSION_COOKIE_NAME)
    if not session_token:
        print("AUTH: error")
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "User not authorized.")

    return session_token

async def admin_only(request: Request):
    session_token = request.cookies.get(settings.SESSION_COOKIE_NAME)
    if not session_token:
        print("AUTH: error")
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "User not authenticated.")

    user = await get_user_from_session(session_token)
    if not user:
        print("AUTH: User does not exist")
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Invalid Session.")

    if user.role != "admin":
        print("AUTH: error: user is not admin")
        raise HTTPException(status.HTTP_403_FORBIDDEN, "Admin access required.")

async def admin_and_staff(request: Request):
    session_token = request.cookies.get(settings.SESSION_COOKIE_NAME)
    if not session_token:
        print("AUTH: error")
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "User not authenticated.")

    user = await get_user_from_session(session_token)
    if not user:
        print("AUTH: User does not exist")
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Invalid Session.")

    if user.role != "admin" or user.role != "staff":
        print("AUTH: error: user is not admin or staff")
        raise HTTPException(status.HTTP_403_FORBIDDEN, "Admin or staff access required.")

