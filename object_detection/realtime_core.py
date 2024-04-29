import cv2
import time
import numpy as np

# Load Yolo -> Raspberry Pi 4 (4GB) can't handle YOLOv3!
#net = cv2.dnn.readNet("../weights/yolov3_training_last.weights", "../cfg/yolov3_testing.cfg")
net = cv2.dnn.readNet("../weights/yolov4-tiny-custom_last.weights", "../cfg/yolov4-tiny-custom.cfg")

classes = []
with open("coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]
layer_names = net.getLayerNames()

# For Raspberry Pi, use with [0] index!
# Delete [0] index for IndexError: invalid index to scalar variable
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]
colors = np.random.uniform(0, 255, size=(len(classes), 3))

# 0 for main camera(pc) : 1 for webcam
cap = cv2.VideoCapture(1)

# resolution: 640x640 or 640x480
#cap.set(cv2.CAP_PROP_FRAME_WIDTH, 608)
#cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 608)

# fps veya frame için denenebilir;
#cap.set(cv2.CAP_PROP_FPS, )

font = cv2.FONT_HERSHEY_PLAIN
starting_time = time.time()
frame_id = 0

while True:
    _, frame = cap.read()
    frame_id += 1

    height, width, channels = frame.shape

        # Detecting objects : macOS = 416, 324 or 320 / PC, raspberrypi or yolov4-tiny = 320 
    blob = cv2.dnn.blobFromImage(frame, 0.00392, (320, 320), (0, 0, 0), True, crop=False)

    net.setInput(blob)
    outs = net.forward(output_layers)

    # Showing informations on the screen
    class_ids = []
    confidences = []
    boxes = []
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:
                # Object detected
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                # Rectangle coordinates
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)
                
    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.8, 0.3)

    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            confidence = confidences[i]
            color = colors[class_ids[i]]
            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
            cv2.putText(frame, label + " " + str(round(confidence, 2)), (x, y + 30), font, 3, color, 3)

    elapsed_time = time.time() - starting_time
    fps = frame_id / elapsed_time
    cv2.putText(frame, "FPS: " + str(round(fps, 2)), (10, 50), font, 4, (0, 0, 0), 3)
    cv2.imshow("Image", frame)
    
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()