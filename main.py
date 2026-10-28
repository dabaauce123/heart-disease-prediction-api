from fastapi import FastAPI
from pydantic import BaseModel, Field, model_validator

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
        "status": "Model integration pending",
    }
