from pydantic import UUID4, BaseModel


class CadastrServiceResponse(BaseModel):
    result_id: UUID4
