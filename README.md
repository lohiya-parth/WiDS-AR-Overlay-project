# WiDS-AR-Overlay-project

Week 0:Image Processing using OpenCV and Pillow

This project demonstrates basic image processing operations in Python
using Pillow, NumPy, and OpenCV.

## Features
- Load images using Pillow
- Convert Pillow images to OpenCV format
- RGB to BGR color conversion
- Image resizing
- Image sharpening using convolution

## Requirements
- Python 3.x

Install dependencies using:
```bash
pip install -r requirements.txt

Week 1: Background Manipulation using GrabCut

This project demonstrates **background removal and replacement** using Python and OpenCV's **GrabCut** algorithm.  
It allows you to extract a person (foreground) from an image and overlay them onto a new background.

---

## Features

- Load foreground (person) and background images
- Remove background using **GrabCut**
- Resize extracted foreground
- Overlay foreground onto a new background at a custom position
- Display and save the final composite image


# Week 2: Face Landmark Overlay using MediaPipe

This project overlays a custom image (PNG with transparency) onto a person's face in a video
using **MediaPipe Face Mesh** and **OpenCV**. The overlay scales dynamically based on the
distance between the eyes, providing realistic placement.

---

## Features

- Detect facial landmarks in a video
- Dynamically position overlay based on eye landmarks
- Resize overlay proportionally
- Smooth alpha blending for seamless integration
- Display video in real-time and save processed output

# Week 3: Live Webcam AR Overlay using MediaPipe

This project demonstrates a **real-time AR overlay** on a live webcam feed using **MediaPipe Face Mesh** and **OpenCV**.  
Users can dynamically place an overlay image (PNG with transparency) on the forehead, nose, or mouth.

---

## Features

- Real-time face landmark detection
- Overlay image follows selected facial landmark
- Alpha blending for smooth integration
- Dynamic overlay position switching:
  - **1** → Forehead
  - **2** → Nose
  - **3** → Mouth
- Press **q** to quit the webcam feed


