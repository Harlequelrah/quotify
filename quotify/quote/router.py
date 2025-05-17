from fastapi import Depends

from quotify.tag.schemas import TagReadModel
from .fastapi_cruds import myapp_crud , read_quote_tags as rqt , create_quote_tag as cqt,delete_quote_tag as dqt
from ..settings.auth.configs import authentication
from elrahapi.router.router_namespace import DefaultRoutesName, TypeRoute
from typing import List
from elrahapi.router.router_provider import CustomRouterProvider
from sqlalchemy.orm import Session


router_provider = CustomRouterProvider(
    prefix="/quotes",
    tags=["quote"],
    crud=myapp_crud,
    #authentication=authentication,
    with_relations=False
)

app_myapp = router_provider.get_public_router(
    exclude_routes_name=[DefaultRoutesName.BULK_CREATE,DefaultRoutesName.COUNT,DefaultRoutesName.BULK_DELETE]
)
# app_myapp = router_provider.get_protected_router()


@app_myapp.get("/{quote_id}/tags",response_model=List[TagReadModel])
async def read_quote_tags(
    quote_id: int,
    skip: int = 0,
    limit: int = None,
    db: Session = Depends(authentication.get_session)
):
    return await rqt(
        quote_id=quote_id,
        skip=skip,
        limit=limit,
        db=db
    )


@app_myapp.post("/{quote_id}/tags/{tag_id}",status_code=201)
async def create_quote_tag(
    quote_id: int,
    tag_id:int,
    db: Session = Depends(authentication.get_session),
):
    return await cqt(quote_id=quote_id,tag_id=tag_id, db=db)


@app_myapp.delete("/{quote_id}/tags/{tag_id}", status_code=204)
async def create_quote_tag(
    quote_id: int,
    tag_id: int,
    db: Session = Depends(authentication.get_session),
):
    return await dqt(quote_id=quote_id, tag_id=tag_id, db=db)
