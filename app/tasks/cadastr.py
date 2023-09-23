import asyncio

from app.core.schemas import CadastrCalcResultSchema, CadastrDataSchema
from app.services.clients.cadastr_client import cadastr_client
from app.worker import celery


@celery.task(name="calculate_cadastr_data")
async def calculate_cadastr_data(data: CadastrDataSchema) -> CadastrCalcResultSchema:
    result = asyncio.get_event_loop().run_until_complete(cadastr_client.calculate())
    return CadastrCalcResultSchema(**result, calculated=True)
