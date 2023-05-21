import cv2 
import numpy as np

def empty(a):
    pass

def create_trackbar(empty):
# Create trackbar window
    cv2.namedWindow("HSV")
    cv2.resizeWindow("HSV",640,240)
    # cv2.createTrackbar("HUE Min","HSV",360,0,empty)
    # cv2.createTrackbar("HUE Max","HSV",360,0,empty)
    # cv2.createTrackbar("SAT Min","HSV",100,0,empty)
    # cv2.createTrackbar("SAT Max","HSV",100,0,empty)
    # cv2.createTrackbar("VALUE Min","HSV",100,0,empty)
    # cv2.createTrackbar("VALUE Max","HSV",100,0,empty)

    cv2.createTrackbar("HUE Min","HSV",0,179,empty)
    cv2.createTrackbar("HUE Max","HSV",179,179,empty)
    cv2.createTrackbar("SAT Min","HSV",130,255,empty)
    cv2.createTrackbar("SAT Max","HSV",163,255,empty)
    cv2.createTrackbar("VALUE Min","HSV",167,255,empty)
    cv2.createTrackbar("VALUE Max","HSV",210,255,empty)

    cv2.namedWindow("Parameters")
    cv2.resizeWindow("Parameters",640,240)
    cv2.createTrackbar("Threshold1","Parameters",166,255,empty)
    cv2.createTrackbar("Threshold2","Parameters",171,255,empty)
    cv2.createTrackbar("Area","Parameters",1750,30000,empty)

def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver

def procesamiento_imagen(img):
    imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Obtención parámetros de ventana

    h_min = cv2.getTrackbarPos("HUE Min","HSV")
    h_max = cv2.getTrackbarPos("HUE Max", "HSV")
    s_min = cv2.getTrackbarPos("SAT Min", "HSV")
    s_max = cv2.getTrackbarPos("SAT Max", "HSV")
    v_min = cv2.getTrackbarPos("VALUE Min", "HSV")
    v_max = cv2.getTrackbarPos("VALUE Max", "HSV")
    '''
    h_min = 0
    h_max = 179
    s_min = 134
    s_max = 243
    v_min = 203
    v_max = 255
    '''
    # Procesamiento de imagen
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv2.inRange(imgHsv,lower,upper)
    result = cv2.bitwise_and(img,img, mask = mask)
    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)

    imgBlur = cv2.GaussianBlur(result, (7, 7), 1)
    imgGray = cv2.cvtColor(imgBlur, cv2.COLOR_BGR2GRAY)
    threshold1 = cv2.getTrackbarPos("Threshold1", "Parameters")
    threshold2 = cv2.getTrackbarPos("Threshold2", "Parameters")
    imgCanny = cv2.Canny(imgGray, threshold1, threshold2)
    kernel = np.ones((5, 5))
    imgDil = cv2.dilate(imgCanny, kernel, iterations=1)
    #return result, imgDil
    return result, imgGray


def getContours(img,imgContour, frameWidth, frameHeight, deadZone):
    global dir
    cx = -1
    cy = -1
    object_detected=0
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        areaMin = cv2.getTrackbarPos("Area", "Parameters")
        if area > areaMin:

            cv2.drawContours(imgContour, cnt, -1, (255, 0, 255), 7)
            peri = cv2.arcLength(cnt, True)

            #####################
            #Parte del rectángulo
            #####################
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)

            if len(approx) == 4:
                object_detected+=1
                x , y , w, h = cv2.boundingRect(approx)
                cx = int(x + (w / 2))  # CENTER X OF THE OBJECT
                cy = int(y + (h / 2))  # CENTER Y OF THE OBJECT
                
                #Dibuja linea que une centro con centro del objeto
                cv2.line(imgContour, (int(frameWidth/2),int(frameHeight/2)), (cx,cy),(0, 0, 255), 3)
                
                cv2.rectangle(imgContour, (x, y), (x + w, y + h), (0, 255, 0), 5)
                cv2.putText(imgContour, "Points: " + str(len(approx)), (x + w + 20, y + 20), cv2.FONT_HERSHEY_COMPLEX, .7,(0, 255, 0), 2)
                cv2.putText(imgContour, "Area: " + str(int(area)), (x + w + 20, y + 45), cv2.FONT_HERSHEY_COMPLEX, 0.7,(0, 255, 0), 2)
                cv2.putText(imgContour, " " + str(int(x)) + " " + str(int(y)), (x - 20, y - 45), cv2.FONT_HERSHEY_COMPLEX,0.7,(0, 255, 0), 2)
            else:
                pass
            #if abs(radius-distance) < 0.9*radius:
                #(x,y), radius = cv2.minEnclosingCircle(cnt)
                #center = (int(x),int(y))
                #radius = int(radius)
                #print("La curva se asemeja a un círculo.")
                #if error < 0.9*radius:
                #print("La calidad del ajuste es aceptable.")
                #cv2.circle(imgContour, (x,y), radius, (0, 0, 255), 5)
                #cv2.line(imgContour, (int(frameWidth/2),int(frameHeight/2)), (x,y),(0, 0, 255), 3)

                ##################
                #Parte del círculo
                ##################

                # distance = 0
                # for point in cnt:
                #     distance += np.sqrt((point[0][0]-x)**2+(point[0][1]-y)**2)
                # distance /= len(cnt)

                # (x,y),radius = cv2.minEnclosingCircle(cnt)
                # center = (int(x),int(y))
                # radius = int(radius)

                # circumference = 2*np.pi*radius
                # error = 0
                # for point in cnt:
                #     error += abs(np.sqrt((point[0][0]-x)**2+(point[0][1]-y)**2) - circumference/len(cnt))
                # error /= len(cnt)

                #Evaluamos si la curva se asemeja a un círculo y si es suficientemente buena aproximación
            

            #print(len(approx))  
        else:
            pass    

    return cx, cy, object_detected
    

def display(img,  frameWidth, frameHeight, deadZone):
    cv2.line(img,(int(frameWidth/2)-deadZone,0),(int(frameWidth/2)-deadZone,frameHeight),(255,255,0),3)
    cv2.line(img,(int(frameWidth/2)+deadZone,0),(int(frameWidth/2)+deadZone,frameHeight),(255,255,0),3)
    cv2.circle(img,(int(frameWidth/2),int(frameHeight/2)),5,(0,0,255),5)
    cv2.line(img, (0,int(frameHeight / 2) - deadZone), (frameWidth,int(frameHeight / 2) - deadZone), (255, 255, 0), 3)
    cv2.line(img, (0, int(frameHeight / 2) + deadZone), (frameWidth, int(frameHeight / 2) + deadZone), (255, 255, 0), 3)