# DRONING

# Repository Name

## Overview
This repository contains the project files for the development of an Autonomous Racing Drone based on vision. The project focuses on implementing control systems, perception systems for gate detection using conventional vision and artificial intelligence, and utilizing a simulator for testing and refinement. The repository is organized into the following directories:

## Directories

- Control: Contains the code and documentation related to the control systems of the drone. Please refer to the `Control/README.md` file for detailed information about the control algorithms, maneuvering, stabilization, and flight characteristics.

- Exhibition: The Exhibition directory holds the code and documentation for the vision-based perception systems with AI of the drone. Please refer to the `Exhibition/README.md` file for details about past and upcoming exhibitions, as well as any related documentation.

- MBSE: The MBSE (Model-Based Systems Engineering) directory houses documentation and models related to the overall system architecture, requirements, and system-level design. Please refer to the `MBSE/README.md` file for more information on the MBSE approach and the contents of this directory.

- Simulator: This directory contains the code and documentation for the simulator used to test and refine the drone's control and perception systems in a virtual environment. Please refer to the `Simulator/README.md` file for instructions on setting up and using the simulator.

- Vision: The Vision directory holds the code and documentation for the vision-based perception systems of the drone using OpenCV. Please refer to the `Vision/README.md` file for detailed information on the vision-based algorithms, gate recognition techniques, and instructions for using these systems.



## Directory Structure

```sh
.
├── Control
│   ├── README.md
│   ├── control_utils.py
│   ├── main.py
│   └── opencv_utils.py
├── Exhibition
│   ├── README.md
│   ├── hands_detection.py
│   └── hands_utils.py
├── MBSE
│   ├── MBSE_system.slx
│   └── README.md
├── Simulator
│   └── README.md
└── Vision
    ├── README.md
    ├── example_opencv.py
    ├── main.py
    └── opencv_utils.py

```

## Getting Started

To get started with this project, please navigate to the respective directories mentioned above and refer to the corresponding `README.md` files for detailed instructions, setup guidelines, and documentation related to each aspect of the project.

## License

This project is licensed under the [MIT License](LICENSE). Please review the license file for more information.

## Contributing

Contributions to this project are welcome. If you have any suggestions, bug fixes, or improvements, please submit a pull request.