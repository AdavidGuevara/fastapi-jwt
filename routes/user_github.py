from fastapi import APIRouter
from schemas.user import UserGithub
from requests import get
from middlewares.verify_token_routes import VerifyTokenRoute

user_github = APIRouter(route_class=VerifyTokenRoute)


@user_github.post("/user/github")
def github_user(github: UserGithub):
    return get(
        f'https://api.github.com/search/users?q=location:"{github.country}"&page={github.page}'
    ).json()
