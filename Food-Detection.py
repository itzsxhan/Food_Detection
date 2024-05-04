from ultralytics import YOLO

model = YOLO("best (1).pt")
results = model(source=0, conf=0.5, show=True)
