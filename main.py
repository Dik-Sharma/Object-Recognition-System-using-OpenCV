import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox
from gtts import gTTS
from playsound import playsound

#from simple_facerec import SimpleFacerec

# Encode faces from a folder
# sfr = SimpleFacerec()
# sfr.load_encoding_images("Resources/images")

# capture = cv2.VideoCapture(0)
# capture.set(3, 640)
# capture.set(4, 480)
# imgBack = cv2.imread('images/back.jpg')


# while True:l
#   success, img = capture.read()
#  cv2.imshow('Webcame', img)
# cv2.imshow('WebCamera', imgBack)Q
# cv2.waitKey(1)

# Load Encoded file

# file = open('EncodeFile.p', 'rb')
# encodeListWithKnown = pickle.load(file)
# file.close()
# encodeListKnown, studentIds = encodeListWithKnown
# print(studentIds)

labels = []
video_capture = cv2.VideoCapture(0)


def speech(text):
    print(text)
    language = "en"
    output = gTTS(text=text, lang=language, slow=False)
    output.save("./sounds/speech.mp3")
    playsound("./sounds/speech.mp3")


while True:
    labes = ["Knife", "knife", "gun","Cell phone","cell phone","Cellphone","stone", "scissor","scissors","bottle","bottles","weapon", "Gun", "rifle", "Rifle", "Sword","Stone","stone", 'sword']
    labs = []
    success, img = video_capture.read()
    ret, frame = video_capture.read()

    # Detect Faces


    bbox, label, conf = cv.detect_common_objects(frame,confidence=0.32, model='yolov4')
    out_image = draw_bbox(frame, bbox, label, conf)
    for item in label:
        if item in labels:
            pass
        else:
            labels.append(item)
            for its in labes:
                if its == item:
                    labs.append(item)

    cv2.imshow('Object Detection', out_image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break  # image identification  and capture to dataset with label.

i = 0
new_sentences = []
for item in labels: 
    if item not in labes:
        continue
    if i == 0:
        new_sentences.append(f"Warning! I found a {item}, ,")
    else:
        new_sentences.append(f"a {item}")

    i += 1

speech(" ".join(new_sentences))
