# Tank Rover Control System User Manual

## Introduction

The Tank Rover Control System is a software application that allows users to control a tank rover using a Raspberry Pi Zero W. The system consists of a locally hosted web interface that can be accessed by other computers on the same network. Users can control the tank rover's movements using the web interface.

This user manual provides detailed instructions on how to install and use the Tank Rover Control System.

## Table of Contents

1. System Requirements
2. Installation
3. Setup Guide
4. Using the Tank Rover Control System
5. Troubleshooting
6. Frequently Asked Questions (FAQs)

## 1. System Requirements

To use the Tank Rover Control System, you will need the following:

- Raspberry Pi Zero W
- L298N Motor Driver Controller Board
- Micro Speed Reduction Motors
- Local Wi-Fi network
- Separate computer connected to the same network

## 2. Installation

To install the Tank Rover Control System, follow these steps:

1. Connect the Raspberry Pi Zero W to the L298N Motor Driver Controller Board and the Micro Speed Reduction Motors according to the provided wiring guide.
2. Connect the Raspberry Pi Zero W to your local Wi-Fi network.
3. Download and install the required dependencies by running the following command:

   ```
   pip install -r requirements.txt
   ```

4. Download the Tank Rover Control System code from the provided source.
5. Transfer the code to the Raspberry Pi Zero W.

## 3. Setup Guide

To set up the Tank Rover Control System, follow these steps:

1. Configure the Raspberry Pi Zero W for headless mode. Refer to the Raspberry Pi documentation for instructions.
2. Auto-start the server script on boot. Add the following line to the Raspberry Pi's boot configuration file:

   ```
   python /path/to/main.py &
   ```

   Replace `/path/to/main.py` with the actual path to the `main.py` file.
3. Start the Tank Rover Control System by running the following command on the Raspberry Pi Zero W:

   ```
   python /path/to/main.py
   ```

   Replace `/path/to/main.py` with the actual path to the `main.py` file.
4. The Tank Rover Control System should now be accessible on the Raspberry Pi Zero W's IP address, on port 8000. Open a web browser on the separate computer connected to the same network and enter the following URL:

   ```
   http://<raspberry_pi_ip_address>:8000
   ```

   Replace `<raspberry_pi_ip_address>` with the actual IP address of the Raspberry Pi Zero W.

## 4. Using the Tank Rover Control System

Once the Tank Rover Control System is set up and running, you can use it to control the tank rover's movements. Follow these instructions:

1. Open the web interface on a separate computer by entering the URL mentioned in the Setup Guide.
2. The web interface will display a map image placeholder on the left and tank control buttons (forwards, backwards, left, right) on the right.
3. To control the tank rover's movements, click on the corresponding buttons or use the keyboard arrows.
4. The tank rover should respond to the commands and move accordingly.

## 5. Troubleshooting

If you encounter any issues while using the Tank Rover Control System, try the following troubleshooting steps:

1. Ensure that the Raspberry Pi Zero W is properly connected to the L298N Motor Driver Controller Board and the Micro Speed Reduction Motors.
2. Check that the Raspberry Pi Zero W is connected to the local Wi-Fi network.
3. Verify that the server script is running on the Raspberry Pi Zero W.
4. Make sure that the separate computer is connected to the same network as the Raspberry Pi Zero W.
5. Check for any error messages or logs that may indicate the cause of the issue.

If the issue persists, refer to the provided documentation or contact technical support for further assistance.

## 6. Frequently Asked Questions (FAQs)

**Q: Can I control multiple tank rovers using the Tank Rover Control System?**

A: The Tank Rover Control System is designed to control a single tank rover. If you want to control multiple tank rovers, you will need to set up separate instances of the Tank Rover Control System for each rover.

**Q: Can I customize the design and layout of the web interface?**

A: Yes, you can customize the design and layout of the web interface by modifying the provided HTML and CSS files. Refer to the documentation for more information on how to customize the web interface.

**Q: Can I use a different motor driver or motors with the Tank Rover Control System?**

A: The Tank Rover Control System is specifically designed to work with the L298N Motor Driver Controller Board and Micro Speed Reduction Motors. If you want to use a different motor driver or motors, you will need to modify the code accordingly.

For more frequently asked questions and additional information, please refer to the provided documentation.

---

Congratulations! You have successfully installed and set up the Tank Rover Control System. Enjoy controlling your tank rover using the web interface! If you have any further questions or need assistance, please refer to the documentation or contact our technical support team.