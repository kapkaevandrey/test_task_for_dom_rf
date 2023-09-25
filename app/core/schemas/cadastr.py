from typing import Optional

from pydantic import BaseModel, Field

from app.core.constants.base import Latitude, Longitude
from app.core.constants.regexes import CADASTR_NUMBER_PATTERN


class CadastrDataSchema(BaseModel):
    cadastr_number: str = Field(pattern=CADASTR_NUMBER_PATTERN)
    latitude: float = Field(le=Latitude.MAX, ge=Latitude.MIN)
    longitude: float = Field(le=Longitude.MAX, ge=Longitude.MIN)


class CadastrCalcResultSchema(BaseModel):
    result: Optional[dict] = None
    calculated: bool = True
