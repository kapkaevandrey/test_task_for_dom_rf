import asyncio
import random

from app.core.settings import settings
from app.services.clients.base import BaseCadastrServiceClient


class CadastrServiceClient(BaseCadastrServiceClient):
    async def calculate(
        self,
        cadastr_number: str,
        latitude: float,
        longitude: float,
    ) -> dict:
        pass


class FakeCadastrServiceClient(BaseCadastrServiceClient):
    TIME_SECOND_RANGE = (10, 60)

    async def calculate(
        self,
        cadastr_number: str,
        latitude: float,
        longitude: float,
    ) -> dict:
        await asyncio.sleep(random.randint(*self.TIME_SECOND_RANGE))
        return dict(cadastr_number=cadastr_number, latitude=latitude, longitude=longitude)


cadastr_client = CadastrServiceClient if settings.is_prod else FakeCadastrServiceClient()
