from fastapi import APIRouter, Header
from schemas.user import User
from lib.functions_jwt import write_token, validate_token
from fastapi.responses import JSONResponse

auth_route = APIRouter()


@auth_route.post("/login")
def login(user: User):
    if user.username == "andres":
        return write_token(user.dict())
    else:
        return JSONResponse(content={"message": "User not found"}, status_code=404)


@auth_route.post("/verify/token")
def verify_token(Authorization: str = Header(None)):
    token = str(Authorization).split(" ")[1]
    return validate_token(token, output=True)
