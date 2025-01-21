import fastapi

app = fastapi.FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome use ClassFlow!","copyright":"©️2023-present GudupaoSpark Inc. All rights reserved","License":"MIT License"}

if __name__ == "__main__":
    import uvicorn
    import shelllogo
    shelllogo.print_logo()
    uvicorn.run(app, host="0.0.0.0", port=8000)