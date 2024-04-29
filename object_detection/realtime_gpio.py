#object detection;
import cv2
import time
import numpy as np
from time import sleep
import RPi.GPIO as GPIO

#18 numaralı pin seri bağlantı
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

M1 = 20
M2 = 21
PWMA = 25
PWMB = 26

GPIO.setup(M1, GPIO.OUT) #all pins as outputs
GPIO.setup(M2, GPIO.OUT)
GPIO.setup(PWMA, GPIO.OUT)
GPIO.setup(PWMB, GPIO.OUT)

# Load YoloV4-tiny
net = cv2.dnn.readNet("../weights/yolov4-tiny-custom_last.weights", "../cfg/yolov4-tiny-custom.cfg")

classes = []
with open("coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]
layer_names = net.getLayerNames()

# delete [0] index for IndexError: invalid index to scalar variable
output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
colors = np.random.uniform(0, 255, size=(len(classes), 3))

# 0 for main camera(pi) : 1 for webcam or additional
cap = cv2.VideoCapture(1)

# resolution: 640x640 or 640x480
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
 
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
            
            if confidence >= 0.8:
                print("\nYabani Ot tespit edildi!")
                sleep(1)
                print("\nSu pompası çalışacak!\n")
                #GPIO.output(Motor, GPIO.HIGH)
                GPIO.output(M1, GPIO.HIGH)
                GPIO.output(M2, GPIO.LOW)
                GPIO.output(PWMA, GPIO.HIGH)  # Set enable pin to high to start PWM
                GPIO.output(PWMB, GPIO.HIGH)
                print("Su pompası çalıştı!\n")
                sleep(1)
                GPIO.output(M1, GPIO.LOW)
                GPIO.output(M2, GPIO.HIGH)
                GPIO.output(PWMA, GPIO.LOW)  # Set enable pin to low to start PWM
                GPIO.output(PWMB, GPIO.LOW)
                break
            else:
                GPIO.cleanup()
                print("Clean?")
            """
            if confidence > 0.8:
                # distance<10 ise, araç disarm edilmeli; 
                print("\nYabani Ot tespit edildi!\n")
                sleep(5)
                # print("\nSu pompası çalışacak!\n")
                # GPIO.output(Motor, GPIO.HIGH)
                # sleep(3)
                # GPIO.output(Motor, GPIO.LOW)
                break
            else:
                # GPIO.cleanup()
            """
    elapsed_time = time.time() - starting_time
    fps = frame_id / elapsed_time
    cv2.putText(frame, "FPS: " + str(round(fps, 2)), (10, 50), font, 4, (0, 0, 0), 3)
    cv2.imshow("Image", frame)
    
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()