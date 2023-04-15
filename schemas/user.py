from pydantic import BaseModel


class User(BaseModel):
    username: str
    email: str


class UserGithub(BaseModel):
    country: str
    page: str
