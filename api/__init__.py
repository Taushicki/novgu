from fastapi import FastAPI
from api.routers.user import router as user_routers
from database.settings import DataBaseSettings


def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(user_routers)
    DataBaseSettings.setup(app)
    return app


app = create_app()
