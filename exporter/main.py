from typing import List
from a2wsgi import ASGIMiddleware
from fastapi import FastAPI, Depends
from db.database import get_mongo_client
from model.emissions_model import Sector
from params.emissions_query_params import EmissionQueryParams, build_filters, apply_sorting
import json

app = FastAPI()


client = get_mongo_client()


@app.get("/emissions", response_model=List[Sector])
async def ge_emissions(params: EmissionQueryParams = Depends()):
    filters = build_filters(params)
    sorting = apply_sorting(params)

    cursor = list(client.find(filters).skip(params.skip).limit(params.limit).sort([sorting]))
    return cursor


@app.get("/emissions/ping")
async def ping():
    return {"message": "pong"}

