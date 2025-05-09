from pydantic import BaseModel, Field
from typing import List, Optional

class TagBaseModel(BaseModel):
    name:str=Field(example="drame")


class MetaTagModel(BaseModel):
    pass
