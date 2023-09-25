from http import HTTPStatus

from celery.states import SUCCESS
from fastapi import APIRouter, responses

from app.api.schemas.cadastr import CadastrServiceResponse
from app.core.schemas import CadastrCalcResultSchema, CadastrDataSchema
from app.tasks import calculate_cadastr_data
from app.worker import celery

router = APIRouter()


@router.post("/cadastr/calculate", status_code=HTTPStatus.ACCEPTED)
async def import_folders_and_files(
    items_data: CadastrDataSchema,
) -> CadastrServiceResponse:
    task = calculate_cadastr_data.delay(items_data.model_dump())
    return CadastrServiceResponse(result_id=task.id)


@router.get("/cadastr/result/{task_id}")
async def get_status(task_id: str) -> CadastrCalcResultSchema:
    task_result = celery.AsyncResult(task_id)
    if task_result.status == SUCCESS:
        return CadastrCalcResultSchema(result=task_result.result, calculated=True)
    return CadastrCalcResultSchema(calculated=False)
