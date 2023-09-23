import asyncio
import random
from typing import Any, Dict

from app.core.settings import settings
from app.services.clients.base import BaseCadastrServiceClient


class CadastrServiceClient(BaseCadastrServiceClient):
    async def calculate(
        self,
        cadastr_numbder: str,
        latitude: float,
        longitude: float,
    ) -> Any:
        pass


class FakeCadastrServiceClient(BaseCadastrServiceClient):
    TIME_SECOND_RANGE = (10, 60)

    async def calculate(
        self,
        cadastr_number: str,
        latitude: float,
        longitude: float,
    ) -> Dict[Any]:
        await asyncio.sleep(random.randint(*self.TIME_SECOND_RANGE))
        return dict(cadastr_number=cadastr_number, latitude=latitude, longitude=longitude)


cadastr_client = CadastrServiceClient() if settings.is_prod else FakeCadastrServiceClient()
