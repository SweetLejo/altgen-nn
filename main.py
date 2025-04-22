import json
import os
import numpy as np
from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.responses import JSONResponse
from airplane_classification.airplane_predictor import predict_aircraft
import uvicorn

app = FastAPI(
    title="Aircraft Classification API",
    description="API for classifying aircraft images",
    version="1.0.0",
)



# Health check endpoint
@app.get("/health")

async def health_check():
    """
    Health check endpoint to verify if the API is running
    """
    return {"status": "healthy"}



@app.post("/predict", response_class=JSONResponse)
async def predict_image(file: UploadFile = File(...)):
    """
    Predict aircraft type from an uploaded image
    """
    try:
        # Create temp directory if it doesn't exist
        os.makedirs("temp", exist_ok=True)
        
        # Save the uploaded file temporarily
        temp_image_path = os.path.join("temp", file.filename)
        with open(temp_image_path, "wb") as buffer:
            buffer.write(await file.read())
        
        # Make prediction
        predicted_aircraft = predict_aircraft(temp_image_path)
        
        os.remove(temp_image_path)

        aircraft_type, probability = predicted_aircraft
        
        return {
            "success": True,
            "predicted_aircraft": aircraft_type,
            "probability": float(probability),
            "filename": file.filename
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction error: {str(e)}")


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)