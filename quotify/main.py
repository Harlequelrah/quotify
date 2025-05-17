from fastapi import FastAPI
from .settings.database import engine,session_manager
from .settings.models_metadata import target_metadata
from elrahapi.middleware.error_middleware import ErrorHandlingMiddleware
from .settings.auth.configs import authentication_router
from .settings.auth.routers import user_router,role_router,privilege_router,user_role_router,role_privilege_router
from .settings.logger.router import app_logger
from .tag.fastapi_router import app_tag
from .quote.router import app_myapp as app_quote
# from .myapp.router import app_myapp

app = FastAPI()

target_metadata.create_all(bind=engine)

@app.get("/")
async def hello():
    return {"message":"hello"}

app.include_router(app_tag)
app.include_router(app_quote)

# app.include_router(app_myapp)
# app.include_router(authentication_router)
# app.include_router(user_router)
# app.include_router(privilege_router)
# app.include_router(role_router)
# app.include_router(user_role_router)
# app.include_router(role_privilege_router)
# app.include_router(app_logger)
app.add_middleware(
    ErrorHandlingMiddleware,
)
