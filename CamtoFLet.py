import flet as ft
import torch
from PIL import Image
import numpy as np
import cv2
from io import BytesIO

# Load the pre-trained YOLOv5 model
model = model(source=0, conf=0.5, show=True)

def detect_image(img):
    # Convert Flet's FileData to an image
    image_stream = BytesIO(img.get_bytes())
    image = Image.open(image_stream)
    image = np.array(image)

    # Convert RGB to BGR
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    # Inference
    results = model(image)

    # Convert results to image
    results.render()
    for img in results.imgs:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img_pil = Image.fromarray(img)
        return img_pil

def main(page: ft.Page):
    page.title = "YOLO Object Detection with Flet"
    page.vertical_alignment = "start"

    upload = ft.FileUpload(accept="image/*", multiple=False)
    img_display = ft.Image()
    detect_btn = ft.Button(text="Detect Objects", on_click=lambda _: detect_objects(upload, img_display))

    page.add(upload, detect_btn, img_display)
    page.update()

def detect_objects(upload, img_display):
    if upload.files:
        file = upload.files[0]
        detected_image = detect_image(file)
        img_bytes = BytesIO()
        detected_image.save(img_bytes, format="JPEG")
        img_display.src = "data:image/jpeg;base64," + base64.b64encode(img_bytes.getvalue()).decode()
        img_display.update()

if __name__ == "__main__":
    ft.app(target=main)