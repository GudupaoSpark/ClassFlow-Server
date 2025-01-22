"""
路由 注册/管理
"""

import fastapi
from router import admin,encrypt,user


def include_routers(app: fastapi.FastAPI) -> fastapi.FastAPI:
    """
    为 `app` 注册路由。
    """
    router = fastapi.APIRouter(prefix="/api")
    router.include_router(admin.router)
    router.include_router(encrypt.router)
    router.include_router(user.router)
    
    app.include_router(router)
    
    return app