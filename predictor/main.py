import numpy as np
from fastapi import FastAPI, UploadFile, File, HTTPException
from pydantic import BaseModel, Field
from sklearn.linear_model import LinearRegression
from predictor.model.model import get_model
from predictor.preprocessing.preprocessing_predict import get_encoder
from predictor.preprocessing.preprocessing_train import preprocess_data
from joblib import dump, load
import os
from pathlib import Path

app = FastAPI()


class InputData(BaseModel):
    country: str = Field(..., min_length=3, max_length=3)
    year: int


model: LinearRegression = None

# Ensure the temp_files directory exists
temp_files_dir = Path(os.getcwd() + "/predictor/temp_files")
temp_files_dir.mkdir(parents=True, exist_ok=True)


@app.on_event("startup")
async def startup_event():
    global model
    if os.path.exists(os.getcwd() + "/predictor/model/model.joblib"):
        model = load(os.getcwd() + "/predictor/model/model.joblib")
    else:
        model = None


@app.post('/train')
async def train(file: UploadFile = File(...)):
    global model

    # Save the uploaded file to disk
    file_path = temp_files_dir / file.filename
    with open(file_path, "wb+") as file_object:
        file_object.write(file.file.read())

    X_train_final, y_train = preprocess_data(file_path)


    # Train the model
    print("Training the model...")
    model = get_model()
    model.fit(X_train_final, y_train)
    print("Model trained successfully")

    directory = Path(os.getcwd() + "/predictor/model")
    directory.mkdir(parents=True, exist_ok=True)


    print("Saving the model...")
    # Save the model
    dump(model, directory / 'model.joblib')
    print("Model saved successfully")

    return {"message": "Model trained successfully"}


@app.post('/predict')
async def predict(input_data: InputData):
    if os.path.exists(os.getcwd() + "/predictor/model/model.joblib"):
        model = load(os.getcwd() + "/predictor/model/model.joblib")
    else:
        raise HTTPException(status_code=400, detail="Model not trained yet")

    # Convert the input_data to a suitable format for prediction
    encoder = get_encoder()
    country_encoded = encoder.transform([[input_data.country]])

    user_input_transformed = np.append(country_encoded, [[input_data.year]], axis=1)
    prediction = model.predict(user_input_transformed)

    return {"prediction": prediction.tolist()}
