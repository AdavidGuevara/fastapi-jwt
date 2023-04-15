from fastapi import FastAPI
from dotenv import load_dotenv
from routes.auth import auth_route
from routes.user_github import user_github

app = FastAPI()

app.include_router(auth_route, prefix="/api")
app.include_router(user_github, prefix="/api")

load_dotenv()
