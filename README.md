# Heart Disease Prediction API

## Overview

A beginner machine learning portfolio project that exposes a trained classification model through a REST API built with FastAPI.

The API accepts health-related input features, calculates derived features such as body mass index (BMI), and returns a model prediction.

**Disclaimer:** This project is for educational demonstration only. It is not a medical device and must not be used for diagnosis or treatment decisions.

## Project Goals

- Build a classification model using tabular health data.
- Prepare input features for model inference.
- Serve predictions through FastAPI.
- Validate API inputs with Pydantic.
- Test the API using Swagger UI and HTTP requests.

## Technology Stack

- Python
- pandas
- scikit-learn
- FastAPI
- Pydantic
- Uvicorn
- joblib
- Google Colab

## API Endpoints

### `GET /`

Returns a welcome message and indicates that the model is loaded.

### `POST /predict`

Accepts health-related input features and returns:
- The model's numeric prediction.
- A corresponding class label.
- An educational-use disclaimer.

The endpoint validates input values and calculates derived features, including BMI, pulse pressure, and mean arterial pressure.

## Running the API

The API was tested locally in Google Colab.

To run it in an environment where the required files and dependencies are available:

1. Install the dependencies listed in `requirements.txt`.
2. Place `heart_disease_model.joblib` in the same directory as `main.py`.
3. Start the API with:

   ```bash
   uvicorn main:app --reload
   ```

4. Open `http://127.0.0.1:8000/docs` to explore and test the API.

The saved model file is not included in this repository, so the API cannot run from a fresh clone until the model is obtained or generated separately.

## Dataset

The dataset is not included in this repository. Its source and licence must be verified and documented before redistribution or further use.

## Limitations

- This is an educational project, not a medical device.
- A successful API response does not establish that a prediction is medically accurate.
- Model performance, calibration, and clinical validity have not been established by the API tests described here.
- The saved model artefact is excluded from the repository.

## Current Implementation Status

- [x] FastAPI application structure
- [x] Input validation with Pydantic
- [x] Prediction endpoint integrated into `main.py`
- [x] Saved model loaded by the API
- [x] Local prediction endpoint tested with HTTP requests
- [x] Swagger UI endpoint checked
- [ ] Document dataset source and licence
- [ ] Document model training and evaluation results
- [ ] Provide reproducible instructions for obtaining or generating the model
- [ ] Deploy the API publicly, if desired

## Project Status

Portfolio project in progress.
