import pwg
import json_tool
import os

the_path = os.path.dirname(os.path.abspath(__file__))



def main():
    config_temp = {
        "port":54132,
        "host":"0.0.0.0",
    }
    if not os.path.exists(f"{the_path}/config"):
        os.mkdir(f"{the_path}/config")
    if not os.path.exists(f"{the_path}/data"):
        os.mkdir(f"{the_path}/data")
    if not os.path.exists(f"{the_path}/data/config.json"):
        json_tool.write(config_temp,f"{the_path}/data/config.json")
    if not os.path.exists(f"{the_path}/data/user_data.json"):
        pw = pwg.gen_password(8)
        user_data_temp = [
            {
                "username":"admin",
                "pw_hash":pw["hash"],
            }
        ]
        json_tool.write(user_data_temp,f"{the_path}/data/user_data.json")
    
        return pw["password"]
    else:
        return ""

if __name__ == "__main__":
    print(f"{the_path}/config")
    main()