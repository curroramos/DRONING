from djitellopy import Tello
import cv2
import numpy as np
from opencv_utils import *
from control_utils import *

##################
using_tello = 0 # poner a 1 si se tiene el dron (a 0 para que no despegue)
tello_cam = 1 # poner a 1 si se tiene el dron y sólo se quiere usar la cámara
detector = 0 # 0: color, 1: mano
num_total_puertas = 1000 # número total de puertas en el circuito  
##################

# Configuración de imagen
width = 640 
height = 480  
deadZone = 100
frameWidth = width
frameHeight = height

# Variable global para la imagen
global imgContour

# Contadores para control de dron
startCounter = 0
cnt_sec = 0
num_puertas = 0

# Conectar dron
if using_tello or tello_cam:
    drone = Tello()
    drone.connect()
    drone.for_back_velocity = 0
    drone.left_right_velocity = 0
    drone.up_down_velocity = 0
    drone.yaw_velocity = 0
    drone.speed = 0
    print("Batería: ", drone.get_battery(), "%")

# Configuración de camara
if tello_cam == 0:
    cap = cv2.VideoCapture(0) 
    cap.set(3, frameWidth)
    cap.set(4, frameHeight)
else:
    drone.streamoff()
    drone.streamon()

# Crear ventana con trackbars
if detector == 0:
    create_trackbar(empty)

# Bucle principal
while True:
    # Lectura de imagen
    if tello_cam == 1:
        frame_read = drone.get_frame_read()
        myFrame = frame_read.frame
        img = cv2.resize(myFrame, (width, height))
        pass
    else:
        _, img = cap.read()

    imgContour = img.copy()
    
    # Uso de detector
    if detector == 0:
        # Usar trackbars y filtros para preprocesamiento de imagen
        result, imgDil = procesamiento_imagen(img)

        # Detección de contornos
        cx,cy,object_detected = getContours(imgDil, imgContour, frameWidth, frameHeight, deadZone)
        display(imgContour, frameWidth, frameHeight, deadZone)
        print(cx, cy, object_detected)

    elif detector ==1:
        # Implementar detector de mano, cara, cuerpo
        pass

    # Control de dirección
    dir = direction_control(cx,cy,object_detected, frameWidth, frameHeight, deadZone, imgContour)
    print("Movimiento:", dir)

    # Control de movimiento 
    if using_tello:
        # Despegar dron
        if startCounter == 0:
            drone.takeoff()
            startCounter = 1
        # Actuar según dirección del objeto detectado
        cnt_sec, num_puertas = movement_control(drone, dir, cnt_sec, num_puertas)
    else:
        cnt_sec, num_puertas = movement_control_sim(dir,cnt_sec, num_puertas)

    # Display 
    if detector == 0:
        stack = stackImages(0.9, ([img, result], [imgDil, imgContour]))
        cv2.imshow('Horizontal Stacking', stack)

    if cv2.waitKey(1) & 0xFF == ord('q') or num_puertas==num_total_puertas:
        if using_tello:
            # Aterrizaje y fin de misión
            drone.land()
        break

# cap.release()
cv2.destroyAllWindows()