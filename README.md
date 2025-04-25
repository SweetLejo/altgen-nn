# Aircraft Classification API

## Overview

This project provides a FastAPI-based web service for classifying aircraft images. The API uses a machine learning model to predict the type of aircraft in uploaded images and returns the prediction with a confidence score.

The API will be available at http://localhost:8000.
Swagger docs will be availible at http://localhost:8000/docs.
The Gradio will be available at http://localhost:7860.

## Features

- RESTful API for aircraft image classification
- Health check endpoint for monitoring
- Simple and intuitive API interface

## Prerequisites

- Python 3.11.7

## Installation

### Local Development

1. Clone the repository:
```bash
git clone <repository-url>
cd NNAltGen
```

2. Set up a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python main.py
```
4.5. Run the application on gradio:
```bash
python gradio_app.py
```

The API will be available at http://localhost:8000.
The Gradio will be available at http://localhost:7860.

## API Endpoints

### Health Check

```
GET /health
```

Returns the current health status of the API service.

**Response:**
```json
{
  "status": "healthy"
}
```

### Predict Aircraft

```
POST /predict
```

Accepts an image file and returns the predicted aircraft type.

**Request:**
- Content-Type: multipart/form-data
- Body: form-data with key "file" containing the image file

**Response:**
```json
{
  "success": true,
  "predicted_aircraft": "Boeing 737",
  "probability": 0.95,
  "filename": "uploaded_image.jpg"
}
```

## Project Structure

```
NNAltGen/
├── main.py                        # FastAPI application entry point
├── airplane_classification/       # Classification module
│   ├── __init__.py                # Package initialization
│   ├── airplane_predictor.py      # Prediction implementation
│   ├── pre_processing.py          # Image preprocessing utilities
│   └── dark-microwave-30.keras    # ML model (not in repo)
├── requirements.txt               # Python dependencies
└── README.md                      # Project documentation
```

## Error Handling

The API returns appropriate HTTP status codes:
- 200: Successful prediction
- 500: Server-side errors with details in the response
