# Tank Rover Control System Setup Guide
This guide provides step-by-step instructions for setting up the tank rover control system.
## Raspberry Pi Setup
1. Install the Raspberry Pi OS on the Raspberry Pi Zero W.
2. Connect the Raspberry Pi Zero W to a monitor, keyboard, and mouse.
3. Configure the Raspberry Pi Zero W to connect to your local Wi-Fi network.
## Web Server Deployment
1. Install the required dependencies:
   - Python 3
   - Flask (pip install flask)
   - RPi.GPIO (pip install RPi.GPIO)
   - tkinter (sudo apt-get install python3-tk)
2. Copy the main.py and motor_control.py files to the Raspberry Pi Zero W.
3. Run the main.py script to start the web server.
## L298N Connections
1. Connect the L298N Motor Driver Controller Board to the Raspberry Pi Zero W using the following GPIO pins:
   - LEFT_FORWARD_PIN: 17
   - LEFT_BACKWARD_PIN: 18
   - RIGHT_FORWARD_PIN: 27
   - RIGHT_BACKWARD_PIN: 22
2. Connect the motors to the L298N Motor Driver Controller Board.
## Boot Configurations for Headless Operation
1. Configure the Raspberry Pi Zero W to boot in headless mode:
   - Enable SSH.
   - Disable the desktop environment.
2. Add the main.py script to the autostart configuration to start the web server on boot.
## Additional Notes
- Make sure to provide a reliable power supply for the Raspberry Pi Zero W and the motors.
- Test the control system thoroughly before deploying it in a real environment.