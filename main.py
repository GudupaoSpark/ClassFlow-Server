import fastapi

app = fastapi.FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

if __name__ == "__main__":
    import uvicorn
    import shelllogo
    shelllogo.print_logo()
    uvicorn.run(app, host="0.0.0.0", port=8000)