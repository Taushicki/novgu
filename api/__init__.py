from fastapi import FastAPI
from api.routers.student import router as user_routers


def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(user_routers)
    return app


app = create_app()
