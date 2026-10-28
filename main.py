from fastapi import FastAPI
from pydantic import BaseModel, Field, model_validator
import joblib
from pathlib import Path
import pandas as pd

MODEL_PATH = Path(__file__).parent / "heart_disease_model.joblib"
loaded_model = joblib.load(MODEL_PATH)

app = FastAPI(
    title="Heart Disease Prediction API",
    description="Educational machine learning demonstration",
    version="1.0.0",
)


class HeartDiseaseInput(BaseModel):
    age: int = Field(gt=0)
    gender: int = Field(ge=1, le=2)
    height: int = Field(gt=0)
    weight: float = Field(gt=0)
    ap_hi: int = Field(gt=0)
    ap_lo: int = Field(gt=0)
    cholesterol: int = Field(ge=1, le=3)
    gluc: int = Field(ge=1, le=3)
    smoke: int = Field(ge=0, le=1)
    alco: int = Field(ge=0, le=1)
    active: int = Field(ge=0, le=1)

    @model_validator(mode="after")
    def check_blood_pressure_order(self):
        if self.ap_hi <= self.ap_lo:
            raise ValueError(
                "ap_hi must be greater than ap_lo"
            )
        return self


@app.get("/")
def home():
    return {
        "message": "Heart Disease Prediction API",
        "docs": "/docs",
        "status": "Model loaded; prediction endpoint available",
    }


@app.post("/predict")
def predict(data: HeartDiseaseInput):
    bmi = data.weight / (data.height / 100) ** 2
    is_male = int(data.gender == 2)
    pulse_pressure = data.ap_hi - data.ap_lo
    map_value = (data.ap_hi + 2 * data.ap_lo) / 3

    input_data = pd.DataFrame([{
        "date": "1/1/2021",
        "country": "Unknown",
        "id": 0,
        "active": data.active,
        "age": data.age,
        "alco": data.alco,
        "ap_hi": data.ap_hi,
        "ap_lo": data.ap_lo,
        "cholesterol": data.cholesterol,
        "gender": data.gender,
        "gluc": data.gluc,
        "height": data.height,
        "occupation": "Unknown",
        "smoke": data.smoke,
        "weight": data.weight,
        "BMI": bmi,
        "is_male": is_male,
        "pulse_pressure": pulse_pressure,
        "map": map_value,
    }])

    input_data = input_data[loaded_model.feature_names_in_]
    prediction = int(loaded_model.predict(input_data)[0])

    return {
        "prediction": prediction,
        "class_label": (
            "positive_class" if prediction == 1 else "negative_class"
        ),
        "disclaimer": (
            "Educational demonstration only; not for medical diagnosis."
        ),
    }
