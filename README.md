<div align="center">
<img src="https://cdn-icons-png.flaticon.com/512/919/919855.png" width="150" height="150" alt="icon">
<img src="https://cdn-icons-png.flaticon.com/512/882/882731.png" width="150" height="150" alt="icon">
</div>

<h1 align="center">Image Processing | Object Detection</h1>

* [Purpose](#purpose)
* [Features](#features)
    * [Prerequisites](#prerequisites)
    * [Notes](#notes)
* [Project Structure](#project-structure)
* [Raspberry Pi](#raspberry-pi)
    * [How To Run?](#how-to-run)
* [Jetson Nano](#jetson-nano)
* [Licence](#licence)

## Purpose
<div align="justify">

Base Image Processing and custom Object Detection repo focuses on YOLO (You Only Look Once) used in Jetson Nano & Raspberry Pi 4.

It also contains real time applications and related with electrical components such as Pixhawk and Servo motors.

Main purpose of this repo is creating an image processing software base in mainboards for practicing and adapting the current experiences for the next generation of our technical project members.

## Features
### Prerequisites
* Raspberry Pi 4 - 4GB (at least)
* Jetson Nano 4GB
* USB Camera
* SD Card (32GB at least) and reader

### Notes
1. Install an OS for Raspberry and Jetson then use: `!Warning: Need to install the 64-bit OS for Raspberry Pi due to YOLO's ultralytics library configurations in python.`
  
2. Using USB Camera for higher FPS and better software quality rather than CSI cameras. Further, 64-bit OS is not suitable with CSI cameras in general.

</div>

## Project Structure

The project follows this directory structure:

```
jetson-rpi-image-processing/
│
├── cfg/
│   ├── yolov3_testing.cfg
│   └── yolov4-tiny-custom.cfg
│
├── components/
│   ├── gpio_guide.py
│   ├── mav_pixhawk.py
│   ├── mavlink_object-detect.py
│   ├── mesafe_sensor.py
│   └── servo.py
│
├── object_detection/
│   ├── coco.names
│   ├── object_detection.py
│   ├── realtime_core.py
│   ├── realtime_gpio.py
│   ├── realtime_ultralytics.py
│   └── realtime_v1.py
│
├── test_images/
│   └── ...
│
├── training/
│   └── train_YoloV3 .ipynb
│
├── weights/
│   ├── best.pt
│   ├── yolov8n.pt
│   ├── yolov3_training_last.weights
│   └── yolov4-tiny-custom_last.weights
│
├── gitignore
├── README.md
└── requirements.txt
```

- cfg/: Contains config files for yolov3 and yolov4-tiny.
- components/: Contains code samples related with electrical components such as Pixhawk and Servo motors.
- object_detection/: Contains image processing and object detection codes in both real time and normal.
- test_images/: PNG or JPG image files for testing.
- training/: Google Colab yolov3 training notebook.
- weights/: Custom trained weight files for yolov3, yolov4-tiny and yolov5+
- requirements.txt: Lists project dependencies.

## Raspberry Pi

### How To Run?
1. Virtual environment setup:
```
python3 -m venv yolovenv
```

2. To activate the virtual environment (Windows):
```
yolovenv/Scripts/activate
```

3. To activate the virtual environment (Linux / MacOS):
```
source yolovenv/bin/activate
```

4. Install dependencies:

- If you are running repository on hardware platforms other than Raspberry Pi or Jetson, you should remove `RPi.GPIO` library from `requirements.txt` file; because this library is designed specifically for devices equipped with GPIO pins and may not be compatible with other platforms.
- The `ultralytics` library may not be compatible with all Python environments depending on your device but it's essential for certain features, particularly on Raspberry Pi with 64-bit OS.

```
pip install -r requirements.txt
```
or
```
pip3 install -r requirements.txt
```

5. Run:
```
python file_name.py
```
or
```
python3 file_name.py
```

## Jetson Nano

## Licence

This project is licensed under the MIT License - see the [LICENSE](https://github.com/PRU-Robotic/jetson-rpi-image-processing?tab=MIT-1-ov-file#readme) file for details.