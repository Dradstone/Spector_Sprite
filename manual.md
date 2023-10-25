# Tank Rover Control System User Manual

## Introduction
The Tank Rover Control System is a software solution that allows users to control a tank rover using a Raspberry Pi Zero W. The system consists of a locally hosted web interface on the Pi Zero W, which enables users to control two Micro Speed Reduction Motors via the L298N Motor Driver Controller Board.

## Features
- Web interface for controlling the tank rover
- Responsive and clean design with a futuristic, military-inspired theme
- Control the rover using mouse clicks or keyboard arrows
- Reliable hosting environment for the web interface and seamless processing of commands
- Headless operation with auto-start server script on boot

## Installation
To install the Tank Rover Control System, follow these steps:

1. Set up the Raspberry Pi Zero W with the Raspberry Pi OS.
2. Connect the Raspberry Pi Zero W to a monitor, keyboard, and mouse.
3. Configure the Raspberry Pi Zero W to connect to your local Wi-Fi network.
4. Install the required dependencies by running the following command:
   ```
   pip install flask RPi.GPIO
   ```
5. Copy the `main.py` and `motor_control.py` files to the Raspberry Pi Zero W.
6. Connect the L298N Motor Driver Controller Board to the Raspberry Pi Zero W using the specified GPIO pins.
7. Connect the motors to the L298N Motor Driver Controller Board.
8. Configure the Raspberry Pi Zero W to boot in headless mode by enabling SSH and disabling the desktop environment.
9. Add the `main.py` script to the autostart configuration to start the web server on boot.

## Usage
To use the Tank Rover Control System, follow these steps:

1. Power on the Raspberry Pi Zero W.
2. Wait for the Raspberry Pi Zero W to connect to the local Wi-Fi network.
3. Open a web browser on a device connected to the same network.
4. Enter the IP address of the Raspberry Pi Zero W in the address bar of the web browser.
5. The web interface for controlling the tank rover will be displayed.
6. Use the control buttons or keyboard arrows to activate rover movement.
7. The rover will respond to the commands and move accordingly.

## Troubleshooting
If you encounter any issues while using the Tank Rover Control System, try the following troubleshooting steps:

1. Ensure that the Raspberry Pi Zero W is properly connected to the Wi-Fi network.
2. Check the connections between the Raspberry Pi Zero W and the L298N Motor Driver Controller Board.
3. Verify that the motors are connected correctly to the L298N Motor Driver Controller Board.
4. Make sure that the required dependencies are installed on the Raspberry Pi Zero W.
5. Restart the Raspberry Pi Zero W and try again.

## Conclusion
The Tank Rover Control System provides a user-friendly interface for controlling a tank rover using a Raspberry Pi Zero W. With its responsive design and intuitive controls, users can easily navigate and command the rover. The system's reliability and headless operation ensure a seamless experience. Enjoy exploring and controlling your tank rover with the Tank Rover Control System!