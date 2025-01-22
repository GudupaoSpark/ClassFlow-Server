"""
用户路由
"""

import fastapi
from pydantic import BaseModel

class get_user_Info(BaseModel):
    """
    用户信息
    """
    username: str
    password: str

router = fastapi.APIRouter(prefix="/v1/user")

@router.post("/get/user_info")
def get_user_info(body: get_user_Info):
    """
    获取用户信息
    """
    