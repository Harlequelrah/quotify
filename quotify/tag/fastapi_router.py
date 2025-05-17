from typing import List
from quotify.tag import fastapi_cruds as crud
from fastapi import APIRouter,Depends,status
from sqlalchemy.orm import Session
from ..settings.database import session_manager
from .schemas import TagCreateModel, TagPatchModel, TagReadModel, TagUpdateModel

app_tag=APIRouter(
    prefix="/tags",
    tags=["tags"]
)

@app_tag.get("",response_model=List[TagReadModel])
async def read_tag(skip:int=0,limit:int=None,db:Session=Depends(session_manager.yield_session)):
    return await crud.read_tags(
        skip=skip,
        limit=limit,
        db=db
    )

@app_tag.post("",response_model=TagReadModel)
async def create_tag(tag:TagCreateModel,db:Session=Depends(session_manager.yield_session)):
    return await crud.create_tag(
        tag=tag,
        db=db
    )

@app_tag.get(
        "/{tag_id}",
        response_model=TagReadModel,
        summary="retrive one tag"
        )
async def read_tag(tag_id:int,db:Session=Depends(session_manager.yield_session)):
    return await crud.read_tag(
        tag_id=tag_id,
        db=db
    )

@app_tag.put(
    "/{tag_id}",
    response_model=TagReadModel
)
async def update_tag(tag_id:int,tag:TagUpdateModel,db:Session=Depends(session_manager.yield_session)):
    return await crud.update_tag(
        tag_id=tag_id,
        tag=tag,
        db=db
    )


@app_tag.patch("/{tag_id}", response_model=TagReadModel)
async def update_tag(
    tag_id: int,
    tag: TagPatchModel,
    db: Session = Depends(session_manager.yield_session),
):
    return await crud.update_tag(tag_id=tag_id, tag=tag, db=db)


@app_tag.delete(
    "/{tag_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    description="this endpoint allow to delete one tag passing id as a parameter"
)
async def delete_tag(
    tag_id:int,
    db:Session=Depends(session_manager.yield_session)
):
    return await crud.delete_tag(tag_id=tag_id,db=db)
