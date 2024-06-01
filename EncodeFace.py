import cv2
import face_recognition
import pickle
import os

folderimages='Resources/images';
pathlist=os.listdir(folderimages)
imagelist=[]
Student_id=[]
for imag in pathlist:
    imagelist.append(cv2.imread(os.path.join(folderimages,imag)))
    Student_id.append(os.path.splitext(imag)[0])
print(Student_id)


def findEncodings(imagelist):
    encodeList=[]
    for image in imagelist:
        image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
        encoded=face_recognition.face_encodings(image)[0]
        encodeList.append(encoded)
    return encodeList
print("Encoding Started...")
encodeListKnown=findEncodings(imagelist)
encodeListWithKnown=[encodeListKnown,Student_id]

print("Encoding List Complete")

file=open("EncodeFile.p",'wb')
pickle.dump(encodeListWithKnown,file)
file.close()
print("File Saved")