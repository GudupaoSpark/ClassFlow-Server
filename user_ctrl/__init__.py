import json_tool
import const
from encrypt import dh, enstr
import hashlib


def get_info(username: str, password: str) -> dict:
    data = json_tool.read(f"{const.BASE_DIR}/data/user_data.json")
    
    for user in data:
        if user["username"] == username:
            if user["pw_hash"] == hashlib.sha256(password.encode()).hexdigest():
                nu = user
                nu.pop("pw_hash")
                nu["success"] = True
                return nu
    
    return {"error": "密码错误或用户不存在","success": False}