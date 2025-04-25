# Aircraft Classification API

## Overview

This project provides a FastAPI-based web service for classifying aircraft images. The API uses a machine learning model to predict the type of aircraft in uploaded images and returns the prediction with a confidence score.

- **The API will be available at:** http://localhost:8000.
- **Swagger docs will be availible at:** http://localhost:8000/docs.
- **The Gradio will be available at:** http://localhost:7860.

## Features

- RESTful API for aircraft image classification
- Health check endpoint for monitoring
- Simple and intuitive API interface
- Lightweight and easy to deploy
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
altgen-nn/
├── airplane_classification/
│   ├── __init__.py                  # Package initialization
│   ├── airplane_predictor.py        # Core prediction logic
│   ├── create_labels.py             # Label generation script
│   ├── dark-microwave-30.keras      # Trained Keras model
│   ├── label_mapping.json           # Class index-to-name mapping
│   ├── pre_processing.py            # Image preprocessing utilities
├── notebooks/
│   └── NyModell.ipynb               # Jupyter notebook for model development
├── venv/                            # Virtual environment (excluded from version control)
├── .gitignore                       # Git ignore rules
├── gradio_app.py                    # Gradio interface entry point
├── main.py                          # FastAPI entry point
├── README.md                        # Project documentation
└── requirements.txt                 # Python dependencies
```

## Error Handling

The API returns appropriate HTTP status codes:
- 200: Successful prediction
- 500: Server-side errors with details in the response
