import gradio as gr
from airplane_classification.airplane_predictor import predict_aircraft

def classify_aircraft(image):
    prediction = predict_aircraft(image)
    aircraft_type, probability = prediction
    return {"aircraft": aircraft_type, "confidence": float(probability)}

demo = gr.Interface(
    fn=classify_aircraft,
    inputs=gr.Image(type="filepath"),
    outputs=gr.JSON(),
    title="Aircraft Classification Demo",
    description="Upload an image of an aircraft to identify its type."
)

if __name__ == "__main__":
    demo.launch(share=True)