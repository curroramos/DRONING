# Hand Detection and Drone Control

This repository contains files for hand detection and control of a drone based on detected hand gestures using the webcam. The implementation uses the `mediapipe` library for hand tracking and gesture recognition.

## Overview <a name="overview"></a>

Hand detection and control are essential in various applications, including human-computer interaction, robotics, and augmented reality. This project focuses on detecting hand gestures using computer vision techniques and controlling a drone based on those gestures. By leveraging the `mediapipe` library, the system can accurately track the user's hand movements and translate them into commands for drone control.

## Installation <a name="installation"></a>

To use this hand detection and drone control system, follow the steps below:

1. Clone this repository to your local machine:

   ```
   git clone <repository-url>
   ```

2. Install the required dependencies. Make sure you have Python 3.10, `mediapipe`, `opencv`and `djitellopy` installed. You can install them using the following commands:

   ```
   pip install opencv-python mediapipe djitellopy
   ```

## Usage <a name="usage"></a>

To use the hand detection and drone control system, follow these steps:

1. Connect the Tello drone to your computer (if using Tello) and ensure it is charged.

2. Navigate to the cloned repository on your local machine:

   ```
   cd <path-to-cloned-repo>
   ```
3. Edit the following configuration variables in the code according to your requirements:

use_webcam: Set to True to use the computer's webcam, or False to use the Tello drone.
use_Tello: Set to True if you want to control the Tello drone, or False to use only the gesture recognition without sending commands to the drone.
fly_Tello: Set to True if you want the Tello drone to respond to flight commands, or False to only recognize gestures without executing flight actions.

3. Run the hand detection and control script:

   ```
   python hands_detection.py
   ```

4. A video window will open showing the webcam feed or the Tello drone's camera feed, depending on your configuration. You will see hand landmarks and connections being drawn on the screen.

5. Based on the recognized gestures, the system will generate corresponding commands to control the drone's movements.

6. Make hand gestures within the camera's view to control the drone:

Thumb up gesture: Takeoff the drone (if not already flying).
Thumb down gesture: Land the drone.
Open palm gesture: Move the drone forward.
Closed fist gesture: Move the drone backward.
Ring and middle fingers bent gesture: Perform a flip.
Index finger up gesture: Move the drone up.
Index finger down gesture: Move the drone down.
The recognized gesture will be displayed in the terminal window.

7. Press `q` to exit the program and safely land the drone.

## Troubleshooting <a name="troubleshooting"></a>

If you encounter any issues or errors while using the hand detection and drone control system, consider the following troubleshooting steps:

- Make sure you have the necessary dependencies installed correctly.
- Verify that your webcam or the drone's camera are properly connected and accessible.
- Check the configuration file for any incorrect settings or parameters.
- Ensure proper lighting conditions and hand positioning for accurate hand detection.
- If the issue persists, please [create an issue](<repository-url>/issues) in this repository, providing detailed information about the problem you are facing.

When seeking assistance, provide as much relevant information as possible, including error messages, screenshots, or any other context that can help in troubleshooting the issue.

Enjoy controlling the drone with your hand gestures!


