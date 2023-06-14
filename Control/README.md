# Control
Welcome to the Control subfolder of the autonomous racing drone project repository. This subfolder contains all the necessary information and instructions related to the control systems of the drone. 

## Contents

1. [Overview](#overview)
2. [Installation](#installation)
3. [Configuration](#configuration)
4. [Usage](#usage)
5. [Troubleshooting](#troubleshooting)

## Overview

The control systems in the autonomous racing drone project are responsible for ensuring precise maneuvering, stabilization, and responsive flight characteristics. These systems play a crucial role in controlling the drone's movements and ensuring its safe and efficient operation.

## Installation

To set up the control systems in your environment, follow these steps:

1. Install the necessary software drivers for the flight controller.
2. Download the control system software from the Control subfolder of this repository.
3. Install any required dependencies or libraries specified in the installation instructions.
4. Configure the control system software according to the provided guidelines.

## Configuration

Proper configuration of the control systems is essential for optimal performance. Follow these steps to configure the control systems:

1. Open the control system software.
2. Adjust the control parameters, such as PID gains, to fine-tune the drone's response.
3. Verify the control system's stability and responsiveness through test flights.

## Usage

Once the control systems are installed and configured, follow these guidelines for using them effectively:

In order to facilitate adjusting parameters and developing the code, you can choose to use tello's camera or the computer's default camera. This can be changed in "main.py" by setting the "tello_cam" variable to either 1 or 0.

The same applies to the usage of the drone's motors. The variable "using_tello" can be set to 1 or 0. If the drone's motors aren't being used, the "movement_control_sim" function will be used to simulate what orders are being sent to the drone.

If neither the camera or motors from the drone are being used, the main program can be ran without additional steps. However, if the drone is being used, these will be the steps to follow:

1. Power on the drone.
2. A WiFi network will be created by the drone, the computer must be connected to it.
3. Once conected, the "main.py" program can be ran.
4. A screen will appear, where the vision parameters can be tuned in order to detect the desired color.
6. Once the parameters are set, the drone must be placed in a horizontal and still place (if it is being used).
7. The "R" key must be pressed for the drone to take off, and it will autonomously detect and pass through the desired gates.

## Troubleshooting

If you encounter any issues or errors with the control systems, try the following troubleshooting steps:

1. Check all the connections between the physical components, such as the battery.
2. Check for any error messages or warnings in the control system software.
3. Check for the battery level, which is shown every time the program is launched.
4. Review and adjust the parameters if needed.
5. Consult the project team members responsible for the control systems for further assistance.



