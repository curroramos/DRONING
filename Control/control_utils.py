import cv2 
import numpy as np



def direction_control(cx,cy,object_detected, frameWidth, frameHeight, deadZone, imgContour):
    error=0
    if object_detected==1:
        if (cx <int(frameWidth/2)-deadZone):
            cv2.putText(imgContour, " GO LEFT " , (20, 50), cv2.FONT_HERSHEY_COMPLEX,1,(0, 0, 255), 3)
            cv2.rectangle(imgContour,(0,int(frameHeight/2-deadZone)),(int(frameWidth/2)-deadZone,int(frameHeight/2)+deadZone),(0,0,255),cv2.FILLED)
            dir = 1
            error =abs( cx - int(frameWidth/2)-deadZone)
        elif (cx > int(frameWidth / 2) + deadZone):
            cv2.putText(imgContour, " GO RIGHT ", (20, 50), cv2.FONT_HERSHEY_COMPLEX,1,(0, 0, 255), 3)
            cv2.rectangle(imgContour,(int(frameWidth/2+deadZone),int(frameHeight/2-deadZone)),(frameWidth,int(frameHeight/2)+deadZone),(0,0,255),cv2.FILLED)
            dir = 2
            error =abs( cx -( int(frameWidth / 2) + deadZone))
        elif (cy < int(frameHeight / 2) - deadZone-190): # ponemos 50 para corregir la subida extra
            cv2.putText(imgContour, " GO UP ", (20, 50), cv2.FONT_HERSHEY_COMPLEX,1,(0, 0, 255), 3)
            cv2.rectangle(imgContour,(int(frameWidth/2-deadZone-100),0),(int(frameWidth/2+deadZone),int(frameHeight/2)-deadZone-100),(0,0,255),cv2.FILLED)
            dir = 3
            error =abs(cy - (int(frameHeight / 2) - deadZone-100))
        elif (cy > int(frameHeight / 2) + deadZone):
            cv2.putText(imgContour, " GO DOWN ", (20, 50), cv2.FONT_HERSHEY_COMPLEX, 1,(0, 0, 255), 3)
            cv2.rectangle(imgContour,(int(frameWidth/2-deadZone),int(frameHeight/2)+deadZone),(int(frameWidth/2+deadZone),frameHeight),(0,0,255),cv2.FILLED)
            dir = 4
            error =abs(cy - (int(frameHeight / 2) + deadZone))
        else: 
            # Objeto centrado
            cv2.putText(imgContour, " GO FORWARD " , (20, 50), cv2.FONT_HERSHEY_COMPLEX,1,(0, 0, 255), 3)
            cv2.rectangle(imgContour,(int(frameWidth/2+deadZone),int(frameHeight/2-deadZone)),(int(frameWidth/2)-deadZone,int(frameHeight/2)+deadZone),(0,0,255),cv2.FILLED)
            dir=-1
    else:
        # Objeto no encontrado
        dir = 0

    return dir, error

def movement_control(drone, dir, contador_seguridad, num_puertas, atrav_puerta, difference):
    if contador_seguridad < 0:
        contador_seguridad = 0
    elif contador_seguridad > 11:
        contador_seguridad = 10
    
    if atrav_puerta:
        print("Sigo atravesando puerta...")
        if contador_seguridad<1:
            atrav_puerta = 0
            num_puertas += 1
            print()
            print("PUERTAS ATRAVESADAS: ", num_puertas)
            drone.for_back_velocity = 4
    
    vel=int(0.2*float(difference))
    print(vel)

    if dir == -1:
        contador_seguridad +=1
        print("Contador seguridad: ", contador_seguridad)
        if contador_seguridad == 10 and (not atrav_puerta):
            atrav_puerta = 1
            print("Atravesando puerta ...")
            drone.left_right_velocity = 0; drone.for_back_velocity = 0;drone.up_down_velocity = 0; drone.yaw_velocity = 0
            drone.for_back_velocity = 60
        else:
            if not atrav_puerta:
                drone.left_right_velocity = 0; drone.for_back_velocity = 0;drone.up_down_velocity = 0; drone.yaw_velocity = 0
    elif dir == 1:
        contador_seguridad -=1
        drone.yaw_velocity = -vel
        drone.left_right_velocity = -vel
    elif dir == 2:
        contador_seguridad -=1
        drone.yaw_velocity = vel
        drone.left_right_velocity = vel
    elif dir == 3:
        contador_seguridad -=1
        drone.up_down_velocity= vel*2 # CAMBIO
    elif dir == 4:
        contador_seguridad -=1
        drone.up_down_velocity= -vel*2
    else:
        contador_seguridad -=1
        drone.left_right_velocity = 0; drone.for_back_velocity = 0;drone.up_down_velocity = 0; drone.yaw_velocity = 0

    # SEND VELOCITY VALUES TO TELLO
    if drone.send_rc_control:
        drone.send_rc_control(drone.left_right_velocity, drone.for_back_velocity, drone.up_down_velocity, drone.yaw_velocity)

    return contador_seguridad, num_puertas, atrav_puerta

def movement_control_sim(dir, contador_seguridad, num_puertas, atrav_puerta):
    if contador_seguridad < 0:
        contador_seguridad = 0
    elif contador_seguridad > 11:
        contador_seguridad = 10

    if atrav_puerta:
        print("Sigo atravesando puerta...")
        if contador_seguridad<1:
            atrav_puerta = 0
            num_puertas += 1
            print()
            print("PUERTAS ATRAVESADAS: ", num_puertas)
    
    if dir == -1:
        contador_seguridad +=1
        print("Contador seguridad: ", contador_seguridad)
        if contador_seguridad == 10 and (not atrav_puerta):
            atrav_puerta = 1
            print("Atravesando puerta ...")
    elif dir == 1:
        contador_seguridad -=1
        print("Girando izquierda")
    elif dir == 2:
        contador_seguridad -=1
        print("Girando derecha")
    elif dir == 3:
        contador_seguridad -=1
        print("Subiendo")
    elif dir == 4:
        contador_seguridad -=1
        print("Bajando")
    else:
        contador_seguridad -=1
        print("Dron quieto")
    
    return contador_seguridad, num_puertas, atrav_puerta
