from http import HTTPStatus
from uuid import uuid4

from celery.result import AsyncResult
from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.api.schemas.cadastr import CadastrDataSchema, CadastrServiceResponse
from app.core.worker import create_task

router = APIRouter()


@router.post("/cadastr/calculate", status_code=HTTPStatus.ACCEPTED)
async def import_folders_and_files(
    items_data: CadastrDataSchema,
) -> None:
    task_id = uuid4()
    create_task.delay(task_id)
    await CadastrServiceResponse(result_id=task_id)


@router.get("/cadastr/result/{task_id}")
def get_status(task_id):
    task_result = AsyncResult(task_id)
    result = {"task_id": task_id, "task_status": task_result.status, "task_result": task_result.result}
    return JSONResponse(result)
