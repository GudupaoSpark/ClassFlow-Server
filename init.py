import pwg
import json_tool
import os
from encrypt import dh, enstr
import base64_tool
import const




def main():
    admin = {
            "user_ctrl": 2,
            "class_ctrl": 2,
        }
    config_temp = {
        "port": 54132,
        "host": "0.0.0.0",
    }
    if not os.path.exists(f"{const.BASE_DIR}/config"):
        print("\033[32mINFO\033[0m:     创建配置目录")
        os.mkdir(f"{const.BASE_DIR}/config")
    if not os.path.exists(f"{const.BASE_DIR}/data"):
        print("\033[32mINFO\033[0m:     创建数据存储目录")
        os.mkdir(f"{const.BASE_DIR}/data")
    if not os.path.exists(f"{const.BASE_DIR}/config/config.json"):
        print("\033[32mINFO\033[0m:     创建配置文件")
        json_tool.write(config_temp, f"{const.BASE_DIR}/config/config.json")
    if not os.path.exists(f"{const.BASE_DIR}/data/user_data.json"):
        print("\033[32mINFO\033[0m:     创建默认用户数据文件")
        pw = pwg.gen_password(8)
        
        user_data_temp = [{"username": "admin", "pw_hash": pw["hash"], "role": admin}]
        json_tool.write(user_data_temp, f"{const.BASE_DIR}/data/user_data.json")
        print(
            f"""\033[32mINFO\033[0m:     默认管理员信息：
\033[32mINFO\033[0m:        Name:       admin
\033[32mINFO\033[0m:        Password:   \033[91m{pw['password']}\033[0m（只展示一次）"""
        )
    else:
        now_user_data = json_tool.read(f"{const.BASE_DIR}/data/user_data.json")
        for i in now_user_data:
            if i["username"] == "admin" and i["role"] == admin:
                print("\033[32mINFO\033[0m:     管理员权限正常")
                break
            elif i["username"] == "admin" and i["role"] != admin:
                print("\033[32mINFO\033[0m:     管理员权限被修改，正在恢复")
                i["role"] = admin
                json_tool.write(now_user_data, f"{const.BASE_DIR}/data/user_data.json")
                print("\033[32mINFO\033[0m:     管理员权限恢复完成")
                break
        else:
            print("\033[32mINFO\033[0m:     管理员被删除，正在恢复")
            pw = pwg.gen_password(8)
            now_user_data.append(
                {"username": "admin", "pw_hash": pw["hash"], "role": admin}
            )
            json_tool.write(now_user_data, f"{const.BASE_DIR}/data/user_data.json")
            print(
                f"""\033[32mINFO\033[0m:     恢复完毕，管理员信息：
\033[32mINFO\033[0m:        Name:       admin
\033[32mINFO\033[0m:        Password:   \033[91m{pw['password']}\033[0m（只展示一次）"""
            )


if __name__ == "__main__":
    print(f"{const.BASE_DIR}/config")
    main()
