from elrahapi.crud.crud_models import CrudModels
from .models import Quote  #remplacer par l'entité SQLAlchemy
from .schemas import QuoteCreateModel, QuoteUpdateModel,QuotePatchModel,QuoteReadModel,QuoteFullReadModel #remplacer par les modèles Pydantic
from elrahapi.crud.crud_forgery import CrudForgery
from ..settings.database import session_manager

myapp_crud_models = CrudModels(
    entity_name="quote",
    primary_key_name="id",  #remplacer au besoin par le nom de la clé primaire
    SQLAlchemyModel=Quote, #remplacer par l'entité SQLAlchemy
    ReadModel=QuoteReadModel,
    CreateModel=QuoteCreateModel, #Optionel
    UpdateModel=QuoteUpdateModel, #Optionel
    PatchModel=QuotePatchModel, #Optionel
    FullReadModel=QuoteFullReadModel #Optionel
)
myapp_crud = CrudForgery(
    crud_models=myapp_crud_models,
    session_manager=session_manager
)


