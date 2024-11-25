from fastapi import APIRouter

from .api_routes import router as tools_router


router_v1 = APIRouter(prefix='/v1')

router_v1.include_router(tools_router, tags=['Tools'])
