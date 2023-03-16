from typing import Optional, List
from pydantic import BaseModel, conint, validator


class Value(BaseModel):
    year: conint(ge=1800, le=9999)
    value: float


class Sector(BaseModel):
    country: str
    sector: str
    parentSector: Optional[str] = None
    valuesPerYear: List[Value]

    @validator('country')
    def country_is_uppercase(cls, v):
        if v is not None:
            return v.upper()
        return v
