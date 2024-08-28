!pip install ultralytics

from ultralytics import YOLO

# Load a model
model = YOLO("yolov8n.yaml")  # build a new model from scratch

# Use the model
model.train(data="/content/google_colab_config.yaml", epochs=5)  # train the model


# prediction on new image
s_result = model("your_image_path")
