import fastapi
import encrypt.enstr
import json_tool,base64_tool
import const

router = fastapi.APIRouter(prefix="/v1/encrypt", tags=["加密"])

@router.get("/get/dh/public_key")
async def get_public_dh_key():
    """
    获取服务器DH公钥
    """
    
    pub_key = base64_tool.bytes_to_base64(const.dh.get_private_key())
    return {"public_key": pub_key}