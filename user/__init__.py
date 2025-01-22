import json_tool
import const
from encrypt import dh, enstr


def get_info(username: str, en_pw: str, dh_pub_key: str) -> dict: ...
    