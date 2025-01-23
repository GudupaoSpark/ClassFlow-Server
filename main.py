import fastapi
import fastapi.logger
import json
import init
import router
import const
import base64_tool
import hashlib
from encrypt import enstr

app = fastapi.FastAPI()

app = router.include_routers(app)


@app.middleware("http")
async def middleware(request: fastapi.Request, call_next):
    # 记录请求体
    try:
        request_body = await request.body()
        decoded_body = request_body.decode()
        json_body = json.loads(decoded_body)
        
        print(f"Request body")
        if isinstance(json_body, dict) and "enq" in json_body:
            shk = const.dh.generate_shared_key(base64_tool.base64_to_bytes(json_body['enq']))
            # 重构请求体
            print(f"DH分享密钥：{hashlib.sha256(shk).hexdigest()}")
            json_bodyr = enstr.decrypt_text(json_body["end"], shk)
            print(f"Request body (decrypted): {json_bodyr}")
            en_req = request
            en_req._body = json_bodyr.encode()
            en_req._json = json.loads(json_bodyr)
            # 重建请求体
            
        
        # 处理请求
        response = await call_next(en_req)

        # 记录响应体
        response_body = b""
        async for chunk in response.body_iterator:
            response_body += chunk
        
        print(f"Response body: {response_body.decode()}")
        
        if isinstance(json_body, dict) and "enq" in json_body:
            en_re = {"body":enstr.encrypt_bytes(response_body,shk)}
        else:
            en_re = response_body
        
        print(f"Response body (encrypted): {en_re}")
    
        # 重建响应对象
        return fastapi.responses.JSONResponse(
            content=en_re,
            status_code=response.status_code,
            media_type=response.media_type
        )
            
    except json.JSONDecodeError:
        print(f"Request body (raw): {decoded_body}")
    
    return await call_next(request)
    
    


@app.get("/")
async def root():
    return {"message": "Welcome use ClassFlow!","copyright":"©️2023-present GudupaoSpark Inc. All rights reserved","License":"MIT License"}

if __name__ == "__main__":
    import uvicorn
    import shelllogo
    shelllogo.print_logo()
    init.main()
    
    uvicorn.run(app, host="0.0.0.0", port=8000)