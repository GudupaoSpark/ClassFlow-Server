import fastapi
import encrypt.enstr
import json_tool,base64_tool
import const
import hashlib

router = fastapi.APIRouter(prefix="/v1/encrypt", tags=["加密"])

@router.get("/get/dh/public_key")
async def get_public_dh_key():
    """
    获取服务器DH公钥
    """
    
    pub_key = const.dh.get_public_key()
    print(f"DH公钥：{hashlib.sha256(const.dh.get_public_key()).hexdigest()}")
    return {"public_key": base64_tool.bytes_to_base64(pub_key)}