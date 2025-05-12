

from elrahapi.exception.exceptions_utils import raise_custom_http_exception
from .schemas import TagCreateModel
from sqlalchemy.orm import Session
from .models import Tag
from fastapi import status
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
