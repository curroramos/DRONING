import cv2
import mediapipe as mp
from djitellopy import Tello

# Inicializar mediapipe y Tello
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
tello = Tello()

##########################################
use_webcam = True # usar webcam ordenador
use_Tello = True # usar tello
fly_Tello = True # si está a True el tello recibirá comandos de vuelo
##########################################

isFlying = False # Check para comprobar que ya ha despegado

# Conectar con el dron
if use_Tello:
    tello.connect()
    tello.streamoff()
    tello.streamon()
    print("Batería: ", tello.get_battery(), "%")


# Configurar fuente de video (webcam o cámara del dron)
if use_webcam:
    cap = cv2.VideoCapture(0)
else:
    cap = tello.get_video_capture()
    cap.set(cv2.CAP_PROP_FPS, 15)
    cap.set(3, 640)
    cap.set(4, 480)


def send_tello_command(gesture, tello, isFlying, fly_Tello):
    # Enviar comandos al dron Tello basados en el gesto detectado
    if use_Tello:

        if gesture == 'takeoff':
            if isFlying == False:
                print("TELLO: taking off")
                isFlying=True
                if fly_Tello == True:
                    tello.takeoff()
                pass
            else:
                print("TELLO: already taken off")
                    
        if isFlying & fly_Tello:
            if gesture == 'down':
                tello.up_down_velocity=-40
                tello.left_right_velocity = 0; tello.for_back_velocity = 0; tello.yaw_velocity = 0
                print("TELLO: moving down")

            elif gesture == 'forward':
                tello.for_back_velocity=40
                tello.left_right_velocity = 0;tello.up_down_velocity = 0; tello.yaw_velocity = 0
                print("TELLO: moving forward")

            elif gesture == 'back':
                tello.for_back_velocity=-40
                print("TELLO: moving backward")

            elif gesture == 'flip':
                # tello.flip('f')
                tello.left_right_velocity = 0; tello.for_back_velocity = 0;tello.up_down_velocity = 0; tello.yaw_velocity = 0
                print("TELLO: flip") 

            elif gesture == 'up':
                tello.up_down_velocity=40
                tello.left_right_velocity = 0; tello.for_back_velocity = 0; tello.yaw_velocity = 0
                print("TELLO: moving up")

            elif gesture == 'land':
                tello.land()

            else:
                tello.left_right_velocity = 0; tello.for_back_velocity = 0;tello.up_down_velocity = 0; tello.yaw_velocity = 0

            # send tello rc control signal
            tello.send_rc_control(tello.left_right_velocity, tello.for_back_velocity, tello.up_down_velocity, tello.yaw_velocity)

    
    else:
        if gesture == 'takeoff':
            print("takeoff")
        elif gesture == 'down':
            print("down")
        elif gesture == 'forward':
            print("forward")
        elif gesture == 'back':
            print("back")
        elif gesture == 'flip':
            print("flip")
        elif gesture == 'up':
            print("up")
        elif gesture == 'land':
            print("land")

    return isFlying

def interpret_gesture(hand_landmarks):
    thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
    thumb_ip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP]
    index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
    index_pip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP]
    middle_tip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
    middle_pip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_PIP]
    pinky_tip = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP]
    pinky_pip = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_PIP]
    palm = hand_landmarks.landmark[mp_hands.HandLandmark.WRIST]
    
    # Despegar el dron con el pulgar hacia arriba
    if thumb_tip.y < index_pip.y < pinky_tip.y:
        print("take off recognised")
        return 'takeoff'

    # Aterrizar el dron cuando el pulgar está hacia abajo
    elif thumb_tip.y > index_tip.y > palm.y and thumb_tip.y > thumb_ip.y:
        return 'land'

    # Acercar el dron con la palma abierta
    elif (thumb_tip.y < thumb_ip.y and index_tip.y < index_pip.y and middle_tip.y < middle_pip.y 
        and pinky_tip.y < pinky_pip.y):
        return 'forward'

    # Alejar el dron con el puño cerrado
    elif (index_tip.y > index_pip.y and middle_tip.y > middle_pip.y 
        and pinky_tip.y > pinky_pip.y):
        return 'back'

    # Dar una vuelta sobre si mismo cuando los dedos anular y medio están doblados
    elif thumb_ip.y > thumb_tip.y and middle_pip.y < middle_tip.y and pinky_tip.y < pinky_pip.y:
        return 'flip'

    #Levantar el dron si el dedo índice está hacia arriba
    elif index_tip.y < middle_tip.y < palm.y and index_tip.y < index_pip.y:
        return 'up'

    # Bajar el dron cuando el índice está hacia abajo
    elif index_tip.y > middle_tip.y > palm.y:
        return 'down'
    
    else:
        return 'none'
    
pass


# Inicializar mediapipe hands
with mp_hands.Hands(
    min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands:
    # Bucle principal
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        # Espejo y cambio de BGR a RGB
        frame = cv2.flip(frame, 1)
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Procesar la imagen
        results = hands.process(frame_rgb)

        # Dibujar puntos y conexiones de la mano
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                # Obtener gesto y enviar comando al dron
                gesture = interpret_gesture(hand_landmarks)
                print("CONTROL: recognised ",gesture)

                # Mandar comandos de  movimiento
                isFlying = send_tello_command(gesture, tello, isFlying, fly_Tello)
        
        else:
            gesture = 'none'
            print("CONTROL: recognised ",gesture)
            isFlying = send_tello_command(gesture, tello, isFlying, fly_Tello)




        # Mostrar imagen
        cv2.imshow('Dron Tello - Control por gestos', frame)

        # Salir con la tecla 'q'
        if cv2.waitKey(5) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
tello.land()
tello.streamoff()
tello.end()








