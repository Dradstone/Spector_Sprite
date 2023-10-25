'''
Main file for the tank rover control system.
'''
from flask import Flask, render_template, request
import RPi.GPIO as GPIO
from motor_controller import MotorController
import time

app = Flask(__name__)
motor_controller = MotorController()

# Define the buzzer pin
buzzer_pin = 18  # Change this to the pin your buzzer is connected to

# Set up the buzzer pin
GPIO.setup(buzzer_pin, GPIO.OUT)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/move', methods=['POST'])
def move():
    direction = request.form['direction']
    motor_controller.move(direction)
    return ''

def beep_buzzer():
    GPIO.output(buzzer_pin, GPIO.HIGH)
    time.sleep(0.5)  # Beep for half a second
    GPIO.output(buzzer_pin, GPIO.LOW)

if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    beep_buzzer()  # Beep the buzzer once when the script starts
    app.run(host='0.0.0.0', port=8000)