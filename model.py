import cv2         # Library for openCV
import time
import threading   # Library for threading -- which allows code to run in backend
import playsound   # Library for alarm sound

har_classifier = cv2.CascadeClassifier('fire_detection.xml') # To access xml file which includes positive and negative images of fire. (Trained images)
                                                                         # File is also proweb_cameraed with the code.

web_camera = cv2.VideoCapture(0) # To start camera this command is used "0" for laptop inbuilt camera and "1" for USB attahed camera

def initiate_alarm(): # defined function to play alarm post fire detection using threading
    playsound.playsound('fire_alarm2.mp3',True) # to play alarm # mp3 audio file is also proweb_cameraed with the code.
    # print("alarm shut down !") # to print in console

		
while(True):
    ret, frame = web_camera.read() # Value in ret is True # To read web_cameraeo frame
    if ret == True:        
        grayscale_camera_frames = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # To convert frame into gray color
        fire = har_classifier.detectMultiScale(grayscale_camera_frames, 1.2, 5) # to proweb_camerae frame resolution

        ## to highlight fire with square 
        for (x,y,w,h) in fire:
            #print("Fire Detected !")
            cv2.rectangle(frame,(x-10,y-10),(x+w+10,y+h+10),(255,0,0), 3)
            print("Fire alarm started !")
            threading.Thread(target=initiate_alarm).start()  # To call alarm thread

        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

web_camera.release()