import cv2
import numpy as np
from fastapi import FastAPI
from keras.models import load_model
from fastapi import FastAPI, File, UploadFile
from tensorflow.keras.applications import resnet50


app = FastAPI()

#Loading the Model
model = load_model('object_classifier.h5', compile=False)

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    # Read and decode image
    contents = await file.read()
    nparr = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(nparr, 1)

    # Resize image
    img = cv2.resize(img, (224, 224))
    img.shape = (1,224,224,3)
    
    # Make prediction
    predictions = model.predict(img)
    predicted_classes = resnet50.decode_predictions(predictions, top=5)

    result = []
    for imagenet_id, name, likelihood in predicted_classes[0]:
        result.append({"name": name, "likelihood": float(likelihood)})

    return result