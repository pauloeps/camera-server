from imageai.Detection import VideoObjectDetection
import os
import cv2
import request

# gets current working directory
execution_path = os.getcwd()

# default device camera
camera = cv2.VideoCapture(0)

# set up the video detector
detector = VideoObjectDetection()

detector.setModelTypeAsYOLOv3()
detector.setModelPath(os.path.join(execution_path, "yolo.h5"))

detector.loadModel()

# gets executed on every frame of the video detection
def forFrame(frame_number, output_array, output_count):
    if 'person' in output_count:
        request.setLight(1)
    else:
        request.setLight(0)


video_path = detector.detectObjectsFromVideo(
                camera_input=camera,
                output_file_path=os.path.join(execution_path, "camera_detected_video"),
                frames_per_second=20,
                log_progress=True,
                per_frame_function=forFrame,
                minimum_percentage_probability=40)
