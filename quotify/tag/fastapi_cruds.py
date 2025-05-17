from elrahapi.exception.exceptions_utils import raise_custom_http_exception

from elrahapi.utility.utils import update_entity
from .schemas import TagCreateModel, TagPatchModel, TagUpdateModel
from sqlalchemy.orm import Session
from sqlalchemy import func
from .models import Tag
from fastapi import status

async def count_tags(db:Session)->int:
    return db.query(func.count(Tag.id)).scalar()

async def read_tags(db:Session,skip:int=0,limit:int=None):
        return db.query(Tag).offset(skip).limit(limit).all()

async def read_tag(tag_id:int,db:Session):
    tag= db.query(Tag).filter(Tag.id==tag_id).first()
    if tag is None:
        detail=f"Tag with id {tag_id} is not found"
        raise_custom_http_exception(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=detail
        )
    return tag


async def create_tag(tag:TagCreateModel,db:Session):
    new_tag= Tag(**tag.model_dump())
    try:
        db.add(new_tag)
        db.commit()
        db.refresh(new_tag)
    except Exception as e :
        detail = f"Error occured while creating tag {str(e)}"
        raise_custom_http_exception(
            detail=detail,
            status_code=status.HTTP_400_BAD_REQUEST
        )
    return new_tag

async def update_tag(db:Session,tag_id:int,tag:TagUpdateModel | TagUpdateModel):
    existing_tag= await read_tag(tag_id=tag_id,db=db)
    try :
        existing_tag= update_entity(
            existing_entity=existing_tag,
            update_entity=tag
        )
        db.commit()
        db.refresh(existing_tag)
    except Exception as e :
        detail = f"Error occured while updating entity with id {tag_id} , detail : {str(e)}"
        raise_custom_http_exception(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=detail
        )
    return existing_tag

async def delete_tag(tag_id:int,db:Session):
    existing_tag = await read_tag(tag_id=tag_id,db=db)
    try :
        db.delete(existing_tag)
        db.commit()
    except Exception as e :
        detail = f"Error occurred while deleting tag with id {tag_id} , details : {str(e)}"
        raise_custom_http_exception(
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=detail
        )



