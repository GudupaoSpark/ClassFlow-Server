"""
用户路由
"""

import fastapi
from pydantic import BaseModel
import user_ctrl

class get_user_Info(BaseModel):
    """
    用户信息
    """
    username: str
    password: str

router = fastapi.APIRouter(prefix="/v1/user", tags=["用户"])

@router.post("/get/user_info")
def get_user_info(body: get_user_Info):
    """
    获取用户信息
    """
    return user_ctrl.get_info(body.username, body.password)
    
    