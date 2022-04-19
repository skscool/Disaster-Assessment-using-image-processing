import cv2         
import time
import threading   
import playsound   

har_classifier = cv2.CascadeClassifier('fire_detection.xml') 

web_camera = cv2.VideoCapture(0) 

def initiate_alarm(): 
    playsound.playsound('fire_alarm2.mp3',True) 
    # print("alarm shut down !") 

		
while(True):
    ret, frame = web_camera.read() 
    if ret == True:        
        grayscale_camera_frames = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
        fire = har_classifier.detectMultiScale(grayscale_camera_frames, 1.2, 5) 

        
        for (x,y,w,h) in fire:
            #print("Fire Detected !")
            cv2.rectangle(frame,(x-10,y-10),(x+w+10,y+h+10),(255,0,0), 3)
            print("Fire alarm started !")
            threading.Thread(target=initiate_alarm).start()

        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

web_camera.release()
