from abc import ABCMeta, abstractmethod


class BaseCadastrServiceClient(metaclass=ABCMeta):
    @abstractmethod
    async def calculate(
        self,
        cadastr_number: str,
        latitude: float,
        longitude: float,
    ) -> dict:
        raise NotImplementedError("This method must be implemented")
