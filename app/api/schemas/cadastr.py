from pydantic import UUID4, BaseModel, Field

from app.core.constants.base import Latitude, Longitude
from app.core.constants.regexes import CADASTR_NUMBER_PATTERN, CADASTR_NUMBER_REGEX


class CadastrDataSchema(BaseModel):
    cadastral_number: str = Field(pattern=CADASTR_NUMBER_PATTERN)
    latitude: float = Field(le=Latitude.MAX, ge=Latitude.MIN)
    longitude: float = Field(le=Longitude.MAX, ge=-Longitude.MIN)


class CadastrServiceResponse(BaseModel):
    result_id: UUID4
