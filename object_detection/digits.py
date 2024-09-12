import cv2
import time
import logging
from ultralytics import YOLO

model = YOLO('../weights/best.pt')
classes = model.names
print(classes)

# Set logging level to WARNING to suppress INFO and DEBUG messages
logging.getLogger('ultralytics').setLevel(logging.WARNING)

cap = cv2.VideoCapture(0)
frame_count = 0
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

        # Save annotated frame if there are detected objects: TENGİZ
        # if len(result[0].boxes) > 0:
        #     save_path = f"result_{frame_count}.jpg"
        #     cv2.imwrite(save_path, annotated_frame)
        #     frame_count += 1

        for r in result:
        # Get the detected objects - classes from the result
            if r.boxes:
                box = r.boxes[0]
                class_id = int(box.cls) #!!!
                object_name = model.names[class_id]
                print(object_name)

                # save detected object as photo
                if len(box) > 0:
                    save_path = f"../saves/result{frame_count}_{object_name}.jpg"
                    cv2.imwrite(save_path, annotated_frame)
                    frame_count += 1

                print("Classes are done!")

        if cv2.waitKey(1) & 0xFF == 27: #press ESC to exit
            break
    else:
        print("\nNo frame from camera!\n")
        break

cap.release()
cv2.destroyAllWindows()