from fastapi import APIRouter


router = APIRouter(prefix='/tools')

@router.get('')
async def get_all():
    return []
