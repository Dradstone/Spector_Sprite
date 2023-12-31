'''
Main file for the tank rover control system.
'''
from flask import Flask, render_template, request
import RPi.GPIO as GPIO
from motor_controller import MotorController
app = Flask(__name__)
motor_controller = MotorController()
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/move', methods=['POST'])
def move():
    direction = request.form['direction']
    motor_controller.move(direction)
    return ''
if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    app.run(host='0.0.0.0', port=8000)