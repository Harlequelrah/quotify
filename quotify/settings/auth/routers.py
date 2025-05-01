from elrahapi.router.router_default_routes_name import DefaultRoutesName
from elrahapi.router.router_provider import CustomRouterProvider
from .cruds import user_crud,user_privilege_crud,role_crud,privilege_crud,role_privilege_crud,user_role_crud
from .configs import authentication
from elrahapi.router.relation_model import ModelRelation

user_router_provider = CustomRouterProvider(
    prefix="/users",
    tags=["users"],
    crud=user_crud,
    authentication=authentication,
    with_relations= True,
    relations=[
    ModelRelation(
            relationship_name="user_roles",
            relationship_crud_models=user_role_crud.crud_models,
            result_crud_models=role_crud.crud_models,
            relationship_key1_name='user_id',
            relationship_key2_name='role_id',
            result_model_key_name='id',
    )
    ]
)

user_privilege_router_provider=CustomRouterProvider(
    prefix='/users/privileges',
    tags=["user_privileges"],
    crud=user_privilege_crud,
    authentication=authentication,
)

role_router_provider = CustomRouterProvider(
    prefix="/roles",
    tags=["roles"],
    crud=role_crud,
    authentication=authentication,
)

privilege_router_provider = CustomRouterProvider(
    prefix="/privileges",
    tags=["privileges"],
    crud=privilege_crud,
    authentication=authentication,
)

role_privilege_router_provider=CustomRouterProvider(
    prefix='/roles/privileges',
    tags=["role_privileges"],
    crud=role_privilege_crud,
    authentication=authentication,
    )

user_role_router_provider=CustomRouterProvider(
    prefix='/users/roles',
    tags=["user_roles"],
    crud=user_role_crud,
    authentication=authentication,
    )


# user_router = user_router_provider.get_protected_router()
user_router = user_router_provider.get_mixed_router(
    public_routes_name=[
        DefaultRoutesName.CREATE,
        DefaultRoutesName.READ_ALL,
    ],
    protected_routes_name=[
        DefaultRoutesName.DELETE,
        DefaultRoutesName.UPDATE,
        DefaultRoutesName.PATCH,
        DefaultRoutesName.READ_ONE,
    ],
)

user_privilege_router=user_privilege_router_provider.get_protected_router()

user_role_router=user_role_router_provider.get_protected_router()

role_router=role_router_provider.get_protected_router()

privilege_router=privilege_router_provider.get_protected_router()

role_privilege_router=role_privilege_router_provider.get_protected_router()
