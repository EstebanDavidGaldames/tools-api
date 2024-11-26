from typing import Annotated, List

from fastapi import APIRouter, Path, Query

from server.schemas.tools_api_schemas import NewToolRequest, ToolRequest, ToolResponse


router = APIRouter(prefix='/tools')


@router.get(
    '',
    status_code=200,
    responses={
        200: {'description':'Inventario de herramientas.'},
    },
    description= 'Retorna el listado de herramientas disponibles. Si no ha sido inicializado el inventario retorna una lista vacía.',
)
async def get_list(limit: Annotated[int, Query(ge=1, le=500)] = 20, offset: Annotated[int, Query(ge=0)] = 0) -> List[ToolResponse]:
    return []


@router.post(
    '',
    status_code=201,
    responses={
        201: {'description':'Herramienta inventariada.'},
    },
    description= 'Ingresa una herramienta al inventario con los campos pasados por Body Param. Falla si falta alguno de los campos obligatorios.',
)
async def create(new_tool: NewToolRequest) -> ToolResponse:
    return new_tool


@router.get(
    '/{id}',
    status_code=200,
    responses={
        200: {'description':'Herramienta encontrada.'},
        422: {'description':'El ID ingresado no es un número entero válido.'},
    },
    description= 'Retorna una herramienta por ID. Falla si el ID no existe.',
)
async def get_by_id(id: Annotated[int, Path(ge=1)]) -> ToolResponse:
    return {'id':id}


@router.patch(
    '/{id}',
    status_code=200,
    responses={
        200: {'description':'Herramienta actualizada.'},
        422: {'description':'El ID ingresado no es un número entero válido.'},
    },
    description= 'Actualiza el estado de la herramienta con los datos del Body Param. Falla si el ID no existe.',
)
async def update(id: Annotated[int, Path(ge=1)], tool: ToolRequest) -> ToolResponse:
    return tool


@router.delete(
    '/{id}',
    status_code=204,
    responses= {
        204: {'description': 'Herramienta eliminada del inventario.'},
        422: {'description':'El ID ingresado no es un número entero válido.'},
    },
    description= 'Elimina una herramienta del inventario con ID pasado por Path Param. Falla si el ID no existe.',
)
async def delete(id: Annotated[int, Path(ge=1)]) -> None:
    return None
