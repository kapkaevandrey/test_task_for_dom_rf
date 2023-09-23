from http import HTTPStatus
from uuid import uuid4

from celery.result import AsyncResult
from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.api.validators.cadastral import validate_cadastr_data
from app.core.worker import create_task

router = APIRouter()


@router.post("/cadastr/create", status_code=HTTPStatus.ACCEPTED)
async def import_folders_and_files(
    items_data: dict,
) -> None:
    validate_cadastr_data(items_data)
    task = create_task.delay(uuid4())


@router.get("/cadastr/result/{task_id}")
def get_status(task_id):
    task_result = AsyncResult(task_id)
    result = {"task_id": task_id, "task_status": task_result.status, "task_result": task_result.result}
    return JSONResponse(result)
