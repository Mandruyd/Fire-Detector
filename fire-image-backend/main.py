from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.responses import FileResponse
import cv2
import numpy as np
import torch
import tempfile
from PIL import Image
import io
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import Response

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


model = torch.hub.load('ultralytics/yolov5', 'custom', path='best.pt')

def get_image_from_bytes(binary_image, max_size=1024):
    input_image = Image.open(io.BytesIO(binary_image)).convert("RGB")
    width, height = input_image.size
    resize_factor = min(max_size / width, max_size / height)
    resized_image = input_image.resize((
        int(input_image.width * resize_factor),
        int(input_image.height * resize_factor)
    ))
    return resized_image

@app.post("/detect_fire/")
async def detect_fire(file: bytes = File(...)):
    try:
        # Read the image from the request
        image = get_image_from_bytes(file)
        results = model(image)
        results.render()  # updates results.imgs with boxes and labels
        for img in results.ims:
            bytes_io = io.BytesIO()
            img_base64 = Image.fromarray(img)
            img_base64.save(bytes_io, format="jpeg")
        return Response(content=bytes_io.getvalue(),
            media_type="image/jpeg")
        
    except Exception as err:
        raise HTTPException(status_code=500, detail=str(err))
