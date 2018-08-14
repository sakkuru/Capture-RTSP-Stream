import cv2
import os

os.environ["OPENCV_FFMPEG_CAPTURE_OPTIONS"] = "rtsp_transport;udp"

host = "192.168.100.138"
path = "onvif1"
source = "rtsp://" + host + ":554/" + path
cap = cv2.VideoCapture(source)

while(1):
    ret, frame = cap.read()
    cv2.imshow('VIDEO', frame)
    cv2.waitKey(1)
