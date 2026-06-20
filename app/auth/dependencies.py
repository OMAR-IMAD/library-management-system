from fastapi import Header, HTTPException

from app.auth.auth_handler import decode_access_token


def get_current_user(authorization: str = Header(None)):

    print("AUTH HEADER =", authorization)

    if not authorization:

        raise HTTPException(
            status_code=401,
            detail="Authorization header missing"
        )

    token = authorization

    if authorization.startswith("Bearer "):
        token = authorization.replace(
            "Bearer ",
            ""
        )

    payload = decode_access_token(token)

    if not payload:

        raise HTTPException(
            status_code=401,
            detail="Invalid or expired token"
        )

    return payload