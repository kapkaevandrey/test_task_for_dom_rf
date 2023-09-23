from abc import ABCMeta, abstractmethod
from typing import Any, Dict


class BaseCadastrServiceClient(metaclass=ABCMeta):
    @abstractmethod
    async def calculate(
        self,
        cadastaral_numbder: str,
        latitude: float,
        longitude: float,
    ) -> Dict[Any]:
        raise NotImplementedError("This method must be implemented")
