import tempfile
from yolov5 import detect
import cv2
import torch
import pathlib

img_path = pathlib.Path("test_img.jpg")
model = torch.hub.load('ultralytics/yolov5', 'custom', path='best.pt')


def detect_fire(image_url):
    output_path = tempfile.mktemp(suffix=".jpg")  # Creates a temporary file
    detect.run(source=image_url, weights="yolov5s6.pt", conf_thres=0.25, imgsz=512, project=output_path)