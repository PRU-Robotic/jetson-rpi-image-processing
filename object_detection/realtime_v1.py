from cvlib.object_detection import YOLO
import cv2

"""
PURPOSE: Simple mechanism to control the frequency of object detection and annotation, 
    ensuring that it happens only once every 10 frames captured from the webcam.
"""

cap = cv2.VideoCapture(0)

# Load YOLO with custom weights, configuration, and labels
weights = "../weights/yolov4-tiny-custom_last.weights"
config = "../cfg/yolov4-tiny-custom.cfg"
labels = "coco.names"

# Counter to control frame subsampling
count = 0

while True:
    ret, img = cap.read()

    # Skip frames that are not at every 10th position
    count += 1
    if count % 10 != 0:
        continue
    
    img = cv2.resize(img,(680,460))

    yolo = YOLO(weights, config, labels)
    bbox, label, conf = yolo.detect_objects(img)

    img_with_boxes = yolo.draw_bbox(img, bbox, label, conf)
    cv2.imshow("img_with_boxes", img)

    # Press ESC to exit
    if cv2.waitKey(1)&0xFF==27:
        break