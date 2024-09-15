from pydantic import BaseModel

from app.core.db import Base


def map_model_to_orm(model: BaseModel, orm: Base):
    for key, val in model.model_dump().items():
        setattr(orm, key, val)
