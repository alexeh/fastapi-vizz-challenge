from fastapi import FastAPI, File, UploadFile, Depends
from a2wsgi import ASGIMiddleware
from db.database import get_mongo_client
from middlewares.file_validator import file_validator
from middlewares.request_validator import RequestValidatorMiddleware
from utils.csv_parser import parse_csv_file
import os
from pathlib import Path

app = FastAPI()
app.add_middleware(RequestValidatorMiddleware)



client = get_mongo_client()

# Ensure the temp_files directory exists
temp_files_dir = Path(os.getcwd() + "/temp_files")
temp_files_dir.mkdir(parents=True, exist_ok=True)


@app.post("/upload", dependencies=[Depends(file_validator)])
async def create_upload_file(file: UploadFile = File(...)):

    # Save the uploaded file to disk in the temp_files directory
    file_path = temp_files_dir / file.filename
    with open(file_path, "wb+") as file_object:
        file_object.write(file.file.read())

    parsed_data = parse_csv_file(file_path)

    # Insert the data into the MongoDB collection
    result = client.insert_many(parsed_data)

    # Remove the uploaded file from disk
    os.remove(file_path)

    # Return a JSON response with the number of documents inserted
    return {"message": f"{len(result.inserted_ids)} documents inserted."}


@app.get("/upload/ping")
async def ping():
    return {"message": "pong"}


