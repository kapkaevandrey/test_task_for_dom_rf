import asyncio

from app.services.clients.cadastr_client import cadastr_client
from app.worker import celery


@celery.task(bind=True)
def calculate_cadastr_data(self, data: dict) -> dict:
    result = asyncio.get_event_loop().run_until_complete(cadastr_client.calculate(**data))
    return result
