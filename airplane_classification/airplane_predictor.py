import keras
import numpy as np
import json
from tensorflow.keras.models import load_model # type: ignore
# Fix the import paths - use relative imports since the file is in the same package
from .pre_processing import StochasticDepth  # Import the custom layer
from .pre_processing import preprocess_image  # Import the preprocessing function

'''
keras.utils.get_custom_objects().update({"StochasticDepth": StochasticDepth})

# Load the model
model = load_model('airplane_classification/dark-microwave-30.keras')
'''

model = load_model('airplane_classification/efficient-microwave-72.keras')


# label mapping
with open('airplane_classification/label_mapping.json', 'r') as f:
    label_mapping = json.load(f)


def predict_aircraft(image: str) -> tuple[str, float]:
    """
    Predict the aircraft type from an image and include the probability.
    Args:
        image (str): Path to the image file.
    Returns:
        tuple[str, float]: Predicted aircraft type and its probability.
    """
    preprocessed_image = preprocess_image(image)
    predictions = model.predict(preprocessed_image)
    
    predicted_class_idx = np.argmax(predictions, axis=-1)[0]
    predicted_class_name = label_mapping[str(predicted_class_idx)]
    predicted_probability = predictions[0][predicted_class_idx]
    
    return predicted_class_name, predicted_probability


if __name__ == '__main__':
    # Example usage

    image_path = "airplane_classification/test_data/test1.jpg" 
    
    # Use the predict_aircraft function instead of calling model.predict directly
    predicted_class_name = predict_aircraft(image_path)
    
    print(f"Predicted aircraft type: {predicted_class_name}")