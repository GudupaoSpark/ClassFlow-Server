import fastapi

router = fastapi.APIRouter(prefix="/v1/admin", tags=["管理"])

@router.get("/")
async def root():
    return {"message": "Welcome use ClassFlow Admin!"}