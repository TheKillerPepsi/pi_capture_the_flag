from flask import Flask, redirect, url_for, request
import RPi.GPIO as GPIO
app = Flask(__name__)

GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.OUT) #erste
GPIO.setup(24, GPIO.OUT) #zweite
GPIO.setup(18, GPIO.OUT) #dritte
GPIO.setup(25, GPIO.OUT) #grün

x = 3000

def main_function(input):
    if input < 80:
        #grüne Lampe an
        GPIO.output(25, GPIO.HIGH)
    else:
        #grüne Lampe aus
        GPIO.output(25, GPIO.LOW)
    if input < 500:
        #dritte Lampe an
        GPIO.output(18, GPIO.HIGH)
    else:
        #dritte Lampe aus
        GPIO.output(18, GPIO.LOW)
    if input < 750:
        #zweite Lampe an
        GPIO.output(24, GPIO.HIGH)
    else:
        #zweite Lampe aus
        GPIO.output(24, GPIO.LOW)
    if input < 1000:
        #erste Lampe an
        GPIO.output(23, GPIO.HIGH)
    else:
        #erste Lampe aus
        GPIO.output(23, GPIO.LOW)

@app.route('/interface', methods=['GET', 'POST'])
def interface():
    if request.method == 'POST':
        x = request.form['dis']
	main_function(x)