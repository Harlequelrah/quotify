from elrahapi.exception.exceptions_utils import raise_custom_http_exception

from elrahapi.utility.utils import update_entity
from .schemas import QuoteCreateModel, QuotePatchModel, QuoteUpdateModel
from sqlalchemy.orm import Session
from sqlalchemy import func
from .models import Quote
from fastapi import status
from .cruds import myapp_crud
from quotify.tag.fastapi_cruds import read_tag

async def read_quote_tags(db:Session,quote_id:int,skip:int=0,limit:int=None):
    quote = await myapp_crud.read_one(pk=quote_id,db=db)
    return quote.tags

async def create_quote_tag(db:Session,quote_id:int,tag_id:int):
    quote = await myapp_crud.read_one(pk=quote_id,db=db)
    tag = await read_tag(tag_id=tag_id,db=db)
    quote.tags.append(tag)
    db.commit()
    db.refresh(quote)


async def delete_quote_tag(db: Session, quote_id: int, tag_id: int):
    quote = await myapp_crud.read_one(pk=quote_id, db=db)
    tag = await read_tag(tag_id=tag_id, db=db)
    quote.tags.remove(tag)
    db.commit()
    db.refresh(quote)
