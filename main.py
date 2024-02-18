import cv2
import face_recognition
import os
import numpy as np
from datetime import datetime
from sendmail import sendingEmail
from time import time
from prettytable import PrettyTable

path = 'Data\\Images'
images = []
classNames = [] 
nameList = []
mylist = os.listdir(path)

table = PrettyTable()
table.field_names = ["Student Name", "Date", "Time"]
table.format = True

for cl in mylist:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])

def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encoded_face = face_recognition.face_encodings(img)[0]
        encodeList.append(encoded_face)
    return encodeList

encoded_face_train = findEncodings(images)

def markAttendance(name):
    if name not in nameList:
        now = datetime.now()
        times = now.strftime('%I:%M:%S:%p')
        date = now.strftime('%d-%B-%Y')
        table.add_row([str(name), date, times])
        nameList.append(name)

        

start=time()
cap  = cv2.VideoCapture(0)


while True:
    success, img = cap.read()
    imgS = cv2.resize(img, (0,0), None, 0.25,0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
    faces_in_frame = face_recognition.face_locations(imgS)
    encoded_faces = face_recognition.face_encodings(imgS, faces_in_frame)
    for encode_face, faceloc in zip(encoded_faces,faces_in_frame):
        matches = face_recognition.compare_faces(encoded_face_train, encode_face)
        faceDist = face_recognition.face_distance(encoded_face_train, encode_face)
        matchIndex = np.argmin(faceDist)
        print(matchIndex)
        if matches[matchIndex]:
            name = classNames[matchIndex].upper().lower()
            y1,x2,y2,x1 = faceloc
            y1, x2,y2,x1 = y1*4,x2*4,y2*4,x1*4
            cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
            cv2.rectangle(img, (x1,y2-35),(x2,y2), (0,255,0), cv2.FILLED)
            cv2.putText(img,name, (x1+6,y2-5), cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
            markAttendance(name)
    end=time()
    
    cv2.imshow('webcam', img)
    if (cv2.waitKey(1) and 0xFF == ord('q')) or end-start>10:
        sendingEmail(table.get_html_string())
        break