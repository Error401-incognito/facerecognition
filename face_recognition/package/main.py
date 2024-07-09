import face_recognition as fr
import cv2
import numpy as np
import os
import tkinter as tk
from tkinter import messagebox
from PIL import Image,ImageTk

known_names = []
known_name_encodings = []
def train():
    path = "./train/"
    images = os.listdir(path)
    
    for _ in images:
        image = fr.load_image_file(path + _)
        image_path = path + _
        encoding = fr.face_encodings(image)[0]

        known_name_encodings.append(encoding)
        known_names.append(os.path.splitext(os.path.basename(image_path))[0].capitalize())
        
    messagebox.showinfo("Message", "Training Completed")

def test():
    test_image = "./test/test.jpg"
    image = cv2.imread(test_image)
    face_locations = fr.face_locations(image)
    face_encodings = fr.face_encodings(image, face_locations)
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = fr.compare_faces(known_name_encodings, face_encoding)
        name = ""
        face_distances = fr.face_distance(known_name_encodings, face_encoding)
        best_match = np.argmin(face_distances)
        if matches[best_match]:
            name = known_names[best_match]
        cv2.rectangle(image, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.rectangle(image, (left, bottom - 15), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(image, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
    cv2.imshow("Result", image)
    cv2.imwrite("./output.jpg", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    cap = cv2.VideoCapture(0)

    while True:
        success, img = cap.read()
    
        imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

        facesCurFrame = fr.face_locations(imgS)
        encodesCurFrame = fr.face_encodings(imgS, facesCurFrame)

        for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
            matches = fr.compare_faces(known_name_encodings, encodeFace)
            faceDis = fr.face_distance(known_name_encodings, encodeFace)
    
            matchIndex = np.argmin(faceDis)

            if matches[matchIndex]:
                name = known_names[matchIndex].upper()
    
                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                

        cv2.imshow('Webcam', img)
        c = cv2.waitKey(1)
        if c == 27:
            break
        
    cap.release()
    cv2.destroyAllWindows()