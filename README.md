# Heart Disease Prediction API

## Overview
A beginner machine learning project that exposes a
heart disease prediction model through a REST API.

## Project Goals
- Build a classification model using tabular health data.
- Prepare input features for model inference.
- Serve predictions through FastAPI.
- Validate API inputs with Pydantic.
- Test the API using Swagger UI and HTTP requests.

## Technology Stack
- Python
- pandas and scikit-learn
- FastAPI
- Pydantic
- Uvicorn
- ngrok (for temporary public access)

## API Endpoint
`POST /predict`

The endpoint accepts health-related input features and
returns a model prediction with a disclaimer.

## Limitations
This project is for educational demonstration only.
It is not a medical device and must not be used for
diagnosis or treatment decisions. Model performance
and clinical validity must be evaluated independently.

## Dataset
The dataset is not included in this repository.
Add its source and licence here after verifying them.

## Status
Portfolio project in progress.
