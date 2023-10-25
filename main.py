'''
Main file for the tank rover control system.
'''
import tkinter as tk
from tkinter import messagebox
import RPi.GPIO as GPIO
from motor_control import move_forward, move_backward, move_left, move_right
# GPIO pin numbers for motor control
LEFT_FORWARD_PIN = 17
LEFT_BACKWARD_PIN = 18
RIGHT_FORWARD_PIN = 27
RIGHT_BACKWARD_PIN = 22
class TankRoverGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tank Rover Control")
        self.root.configure(background="black")
        self.create_widgets()
    def create_widgets(self):
        # Top navbar
        navbar_frame = tk.Frame(self.root, bg="black")
        navbar_frame.pack(side=tk.TOP, fill=tk.X)
        logo_label = tk.Label(navbar_frame, text="Tank Rover", fg="white", bg="black", font=("Arial", 16, "bold"))
        logo_label.pack(side=tk.LEFT, padx=10, pady=10)
        status_label = tk.Label(navbar_frame, text="Connected", fg="white", bg="black", font=("Arial", 12))
        status_label.pack(side=tk.RIGHT, padx=10, pady=10)
        # Main content
        main_frame = tk.Frame(self.root, bg="black")
        main_frame.pack(expand=True, fill=tk.BOTH)
        map_frame = tk.Frame(main_frame, bg="black")
        map_frame.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        control_frame = tk.Frame(main_frame, bg="black")
        control_frame.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)
        # Placeholder for future map
        # Control buttons
        forward_button = tk.Button(control_frame, text="Forwards", command=self.move_forward, width=10, height=2)
        forward_button.pack(pady=10)
        backward_button = tk.Button(control_frame, text="Backwards", command=self.move_backward, width=10, height=2)
        backward_button.pack(pady=10)
        left_button = tk.Button(control_frame, text="Left", command=self.move_left, width=10, height=2)
        left_button.pack(pady=10)
        right_button = tk.Button(control_frame, text="Right", command=self.move_right, width=10, height=2)
        right_button.pack(pady=10)
    def move_forward(self):
        # Code to move the rover forward
        move_forward()
    def move_backward(self):
        # Code to move the rover backward
        move_backward()
    def move_left(self):
        # Code to turn the rover left
        move_left()
    def move_right(self):
        # Code to turn the rover right
        move_right()
def main():
    # Initialize GPIO
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LEFT_FORWARD_PIN, GPIO.OUT)
    GPIO.setup(LEFT_BACKWARD_PIN, GPIO.OUT)
    GPIO.setup(RIGHT_FORWARD_PIN, GPIO.OUT)
    GPIO.setup(RIGHT_BACKWARD_PIN, GPIO.OUT)
    # Create the GUI
    root = tk.Tk()
    tank_rover_gui = TankRoverGUI(root)
    root.mainloop()
    # Cleanup GPIO
    GPIO.cleanup()
if __name__ == "__main__":
    main()