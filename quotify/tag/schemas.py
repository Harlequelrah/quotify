from pydantic import BaseModel, Field
from typing import List, Optional

from .meta_models import TagBaseModel

class TagCreateModel(TagBaseModel):
    pass


class TagUpdateModel(TagBaseModel):
    pass

class TagPatchModel(BaseModel):
    name: Optional[str] = Field(example="drame",default=None)

class TagReadModel(BaseModel):
    id:int
    name:str
    class Config:
        from_attributes=True


class TagFullReadModel(TagReadModel):
    pass
    class Config:
        from_attributes=True
