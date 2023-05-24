from fastapi import FastAPI, UploadFile, File, HTTPException
from pydantic import BaseModel, Field
from sklearn.linear_model import LinearRegression

from predictor.model.model import get_model
from predictor.preprocessing.preprocessing import preprocess_data
from joblib import dump, load
import os

app = FastAPI()


class InputData(BaseModel):
    country: str = Field(..., min_length=3, max_length=3)
    year: int


model: LinearRegression = None


@app.on_event("startup")
async def startup_event():
    global model
    if os.path.exists('model.joblib'):
        model = load('model.joblib')
    else:
        model = None


@app.post('/train')
async def train(file: UploadFile = File(...)):
    global model

    # Preprocess the data and get the training data
    # TODO: pass the file/file path or retrieve it from the same location
    X_train_final, y_train = preprocess_data(file.file)

    # Train the model
    model = get_model()
    model.fit(X_train_final, y_train)
    # Save the model
    dump(model, 'model.joblib')

    return


@app.post('/predict')
async def predict(input_data: InputData):
    if model is None:
        raise HTTPException(status_code=400, detail="Model not trained yet")

    # Convert the input_data to a suitable format for prediction
    prediction_input = prepare_input(input_data.data)
    prediction = model.predict(prediction_input)

    return {"prediction": prediction.tolist()}
