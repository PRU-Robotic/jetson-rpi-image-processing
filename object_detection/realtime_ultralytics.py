import cv2
import time
from ultralytics import YOLO

model = YOLO('../weights/best.pt')
classes = model.names

cap = cv2.VideoCapture(1)
prev_time = time.time()

width, height = 640, 480
font = cv2.FONT_HERSHEY_SIMPLEX

while cap.isOpened():
    success, frame = cap.read()

    if success:
        frame = cv2.resize(frame, (width, height))

        current_time = time.time()
        fps = 1 / (current_time - prev_time)
        prev_time = current_time

        result = model.predict(source=frame, conf=0.6)
        annotated_frame = result[0].plot()

        cv2.putText(annotated_frame, f"FPS: {int(fps)}", (10, 20), font, 0.5, (0, 255, 0), 2)
        cv2.imshow("YOLOv8 Detection", annotated_frame)

        if cv2.waitKey(1) & 0xFF == 27: #press ESC to exit
            break
    else:
        print("\nNo frame from camera!\n")
        break

cap.release()
cv2.destroyAllWindows()