from typing import Optional
from pydantic import BaseModel, Field
#from pydantic.class_validators import Optional


class EmissionQueryParams(BaseModel):
    skip: int = Field(0, description="Skip n items", ge=0)
    limit: int = Field(10, description="Limit the results", ge=1, le=100)
    country: Optional[str] = Field(None, description="Filter by country")
    sector: Optional[str] = Field(None, description="Filter by sector")
    parentSector: Optional[str] = Field(None, description="Filter by parent sector")
    year: Optional[int] = Field(None, description="Filter by year", ge=1800, le=9999)
    value: Optional[float] = Field(None, description="Filter by value")
    sort_by: Optional[str] = Field(None, description="Field to sort the results by")
    sort_order: Optional[str] = Field("asc", description="Sort order: 'asc' or 'desc'")


def build_filters(params: EmissionQueryParams):
    filters = {}
    if params.country:
        filters["country"] = params.country.upper()
    if params.sector:
        filters["sector"] = params.sector
    if params.parentSector:
        filters["parentSector"] = params.parentSector
    if params.year is not None or params.value is not None:
        filters["valuesPerYear"] = {
            "$elemMatch": {
                k: v
                for k, v in [("year", params.year), ("value", params.value)]
                if v is not None
            }
        }
    return filters


def apply_sorting(params: EmissionQueryParams):
    sort_by = params.sort_by if params.sort_by else "_id"
    sort_order_int = 1 if params.sort_order.lower() == "asc" else -1
    return sort_by, sort_order_int


