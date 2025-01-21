"""
Password Generator

生成随机强密码
"""

import random
import hashlib

pd:dict = {
    "lowercase": "abcdefghijklmnopqrstuvwxyz",
    "uppercase": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "digits": "0123456789",
}

def gen_password(len:int=8, lo:bool=True,up:bool=True,digits:bool=True,other:str="") -> str:
    """
    生成随机强密码
    
    参数：
        len: 密码长度
        lo: 是否包含小写字母
        up: 是否包含大写字母
        digits: 是否包含数字
        other: 其他字符
    
    返回：
        {
            "password": "密码",
            "hash": "密码哈希值（使用小写字母的SHA-256）"
        }
    """
    pwm = "" # 密码模板
    if lo:
        pwm += pd["lowercase"]
    if up:
        pwm += pd["uppercase"]
    if digits:
        pwm += pd["digits"]
    pwm += other
    
    if pwm == "":
        raise ValueError("密码模板为空")
    
    pw = ""
    
    for i in range(len):
        pw += random.choice(pwm)

    return {
        "password": pw,
        "hash": hashlib.sha256(pw.encode("utf-8")).hexdigest()
    }

if __name__ == "__main__":
    from pprint import pprint as pp
    pp(gen_password(100))