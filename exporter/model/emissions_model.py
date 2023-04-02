from typing import Optional, List

from bson import ObjectId
from pydantic import BaseModel, conint, validator


class Value(BaseModel):
    year: conint(ge=1800, le=9999)
    value: float


class Sector(BaseModel):
    country: str
    sector: str
    parentSector: Optional[str] = None
    valuesPerYear: List[Value]

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        orm_mode = True
        schema_extra = {
            "example": {
                "name": "Jane Doe",
                "email": "jdoe@example.com",
                "course": "Experiments, Science, and Fashion in Nanophotonics",
                "gpa": "3.0",
            }
        }


    @validator('country')
    def country_is_uppercase(cls, v):
        if v is not None:
            return v.upper()
        return v
