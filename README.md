<div align="center">
<img src="https://cdn-icons-png.flaticon.com/512/919/919855.png" width="150" height="150" alt="icon">
<img src="https://cdn-icons-png.flaticon.com/512/882/882731.png" width="150" height="150" alt="icon">
</div>

<h1 align="center">Image Processing | Object Detection</h1>

* [Purpose](#hash-purpose)
* [Features](#hash-features)
* [Raspberry Pi](#hash-raspberry-pi)
    *  [How To Run?](##hash-how-to-run)
* [Jetson Nano](#hash-jetson-nano)
    *  [How To Run?](##hash-how-to-run)

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
* SD Card and reader

### Notes
1. Install an OS for Raspberry and Jetson then use: `!Warning: Need to install the 64-bit OS for Raspberry Pi due to YOLO's ultralytics library configurations in python.`
  
2. Using USB Camera for higher FPS and better software quality rather than CSI cameras. Further, 64-bit OS is not suitable with CSI cameras in general.

</div>


## Raspberry Pi

### How To Run?
1. Virtual environment setup:
```
python3 -m venv environment_name
```

2. To activate the virtual environment (Windows):
```
environment_name/Scripts/activate
```

3. To activate the virtual environment (Linux / MacOS):
```
source environment_name/bin/activate
```

4. Install dependencies:
```
pip install -r requirements.txt
```
or
```
pip3 install -r requirements.txt
```

5. Run:
...

## Jetson Nano

### How To Run?