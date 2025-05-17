from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
from decimal import Decimal
from datetime import datetime

from quotify.tag.meta_models import MetaTagModel


class QuoteCreateModel(BaseModel):
    content : str = Field(example="le soleil se lève .")

class QuoteUpdateModel(BaseModel):
    content: str = Field(example="le soleil se lève .")

class QuotePatchModel(BaseModel):
    content: Optional[str] = Field(example="le soleil se lève .")

class QuoteReadModel(BaseModel):
    id:int
    content:str
    created_at:datetime
    updated_at:Optional[datetime]
    class Config:
        from_attributes=True


class QuoteFullReadModel(QuoteReadModel):
    tags:List[MetaTagModel]
    class Config:
        from_attributes=True
