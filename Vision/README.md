## Gate Detection using Conventional Vision

This repository contains files for gate detection using conventional vision techniques, specifically utilizing OpenCV for gate and obstacle detection.

## Overview <a name="overview"></a>

Gate detection plays a crucial role in various fields, such as autonomous navigation, robotics, and computer vision. This project aims to detect gates and obstacles using conventional vision techniques implemented with OpenCV. By leveraging computer vision algorithms, the system can identify and locate gates and obstacles in real-time.

## Installation <a name="installation"></a>

To use this gate detection system, follow the steps below:

1. Clone this repository to your local machine:

   ```
   git clone <repository-url>
   ```

2. Install the required dependencies. Make sure you have Python and OpenCV installed. If not, you can install them using the following commands:

   ```
   pip install opencv-python
   ```

3. Once the dependencies are installed, you are ready to use the gate detection system.

## Code Structure <a name="Code Structure"></a>

The code consists of several functions:

1. empty(a)
This is a placeholder function that does nothing. It is used as a callback for the trackbars.

2. create_trackbar(empty)
This function creates the trackbar windows and initializes the trackbars for setting various parameters. It creates two windows: "HSV" and "Parameters". The "HSV" window contains trackbars for setting the minimum and maximum values of HUE, SATURATION, and VALUE. The "Parameters" window contains trackbars for setting the threshold values and area for contour detection.

3. stackImages(scale, imgArray)
This function takes a list of images and stacks them horizontally or vertically to create a single image grid. It is used to display multiple images in a single window.

4. procesamiento_imagen(img)
This function processes the input image using the parameters set by the trackbars in the "HSV" window. It converts the image to the HSV color space and applies a color range mask to isolate regions of interest. It then performs Gaussian blurring and converts the image to grayscale. It returns the processed image and the grayscale image.

5. getContours(img, imgContour, frameWidth, frameHeight, deadZone)
This function finds contours in the input image and filters them based on their area. It then approximates the contours to polygons and checks if the number of polygon vertices is 4. If so, it considers it as a gate and performs additional calculations to determine its center and shape (rectangle or pole). It draws the detected gates on the imgContour image and returns the gate's center coordinates, the number of gates detected, and the gate's shape.

6. display(img, frameWidth, frameHeight, deadZone)
This function draws visual elements on the image, such as a horizontal and vertical line representing the center of the frame and a dead zone region. It also adds a circle at the center of the frame.

## Usage <a name="usage"></a>

To use the gate detection system, follow these steps:

1. Ensure that the drone is connected to your system.

2. In the main.py script, you can set the tello_cam variable to 1 to use the drone's camera. If you want to use your own, set the variable to 0.

3. In the same script set the num_total_puertas variable to the total gate number.

4. Navigate to the cloned repository on your local machine:

   ```
   cd <path-to-cloned-repo>
   ```

5. Run the gate detection script:

   ```
   python main.py
   ```

6. The system will start capturing frames from the camera and perform gate detection. Detected gates and obstacles will be displayed in the output window.

7. Press `Q` to exit the program.

## Troubleshooting <a name="troubleshooting"></a>

If you encounter any issues or errors while using the gate detection system, consider the following troubleshooting steps:

- Make sure you have the necessary dependencies installed correctly.
- Verify that the camera or video source is properly connected and accessible.
- Check the main file for any incorrect settings or parameters.
- Ensure that the lighting conditions and camera angle are suitable for gate detection.
- If the issue persists, please [create an issue](<repository-url>/issues) in this repository, providing detailed information about the problem you are facing.

Remember to include as much relevant information as possible when seeking assistance. This can include error messages, screenshots, or any other context that can help in troubleshooting the issue.

Happy gate detection!