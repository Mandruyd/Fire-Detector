from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.responses import FileResponse
import cv2
import numpy as np
import torch
import tempfile
from PIL import Image
import io
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


model = torch.hub.load('ultralytics/yolov5', 'custom', path='best.pt')

@app.post("/detect_fire/")
async def detect_fire(file: UploadFile = File(...)):
    try:
        # Read the image from the request
        image_data = await file.read()
        image = Image.open(io.BytesIO(image_data))
        
        # Convert the image to OpenCV format
        image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

        # Pass the image to the YOLO model
        results = model(image)

        # Render the results back to an image
        rendered_image = results.render()[0]

        # Save the resulting image
        output_path = tempfile.mktemp(suffix=".jpg")
        cv2.imwrite(output_path, rendered_image)

        # Return the image
        return FileResponse(path=output_path, media_type='image/jpeg')
        
    except Exception as err:
        raise HTTPException(status_code=500, detail=str(err))
