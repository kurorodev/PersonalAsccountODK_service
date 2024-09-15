from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core import db
from app.core.settings import settings
from app.exceptions import EntityAlreadyExistsException



@asynccontextmanager
async def lifespan(app: FastAPI):
    db.initialize()

    if settings.initial_user_schema is not None:
        try:
            user_service.create(settings.initial_user_schema)
        except EntityAlreadyExistsException:
            print("Initial user already exist. Skipping.")

    yield

    db.release()


def create_app():
    app = FastAPI(redoc_url=None, title="PersonalAccountODK", lifespan=lifespan)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.allow_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return app
