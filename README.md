# Concise Video Representation Using Object Detection Method

This project summarizes videos by using object detection to extract and highlight unique frames. It enables users to upload and process videos, view live detections, and visually review unique and common frames.

## Features

- User registration and login
- Video upload and object-based summarization
- Live camera object detection and summary
- Frame viewer for unique and common frames
- Simple web interface using Flask

## Requirements

- Python 3
- Flask
- OpenCV
- NumPy
- imutils
- SQLite3
- Pre-trained YOLOv3 weights and config files (download from [YOLO website](https://pjreddie.com/darknet/yolo/))

## Setup

1. **Clone the repository**
    ```bash
    git clone https://github.com/Suh9019/Concise-Video-Representation-Using-Object-Detection-Method.git
    cd Concise-Video-Representation-Using-Object-Detection-Method
    ```

2. **Install dependencies**
    ```bash
    pip install flask opencv-python numpy imutils
    ```

3. **Download YOLOv3 model files**
    - Download `yolov3.weights`, `yolov3.cfg`, and `coco.names` from the [YOLO website](https://pjreddie.com/darknet/yolo/).
    - Place them in a directory called `yolo-coco/` inside your project.

4. **Create required folders**
    ```
    mkdir -p static/inputvideo static/outputvideo static/unique static/common
    ```

## Usage

1. **Start the Flask application**
    ```
    python app.py
    ```
2. **Open your browser**
    - Go to [http://127.0.0.1:5000](http://127.0.0.1:5000) to use the web interface.

3. **Functionalities**
    - Register and login
    - Summarize uploaded videos based on object detection
    - Run live object detection
    - View extracted unique and common frames

## File Structure

```
app.py               # Main Flask application
LIVE.py              # Live camera detection logic
VIDEO.py             # Video detection logic (not included here)
static/              # Contains video and frame outputs
templates/           # HTML templates for Flask
yolo-coco/           # YOLOv3 model files
user_data.db         # SQLite database for users
```

## Notes

- Make sure your webcam is connected for live detection.
- The YOLOv3 files are needed for both video and live object detection.

## License

This project is for educational purposes.

---

Feel free to modify or expand this README as your project grows!
````
