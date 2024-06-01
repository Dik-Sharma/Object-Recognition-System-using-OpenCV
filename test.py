import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox
import pickle

capture = cv2.VideoCapture(0)
capture.set(3, 640)
capture.set(4, 480)
imgBack = cv2.imread('images/back.jpg')

while True:
    success, img = capture.read()
    cv2.imshow('Webcame', img)
    cv2.imshow('WebCamera', imgBack)
    cv2.waitKey(1)

# Load Encoded file

file = open('EncodeFile.p', 'rb')
encodeListWithKnown = pickle.load(file)
file.close()
encodeListKnown, studentIds = encodeListWithKnown
print(studentIds)

labels = []
video_capture = cv2.VideoCapture(0)
while True:

    success, img = capture.read()

    ret, frame = video_capture.read()
    bbox, label, conf = cv.detect_common_objects(frame)
    out_image = draw_bbox(frame, bbox, label, conf)

    for item in label:
        if item in labels:
            pass
        else:
            labels.append(item)

    cv2.imshow('Object Detection', out_image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

print(labels)
