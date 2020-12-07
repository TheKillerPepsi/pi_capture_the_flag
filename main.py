import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.OUT) 
GPIO.setup(24, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)


#for i in range(5):
#    GPIO.output(23, GPIO.HIGH)
#    GPIO.output(24, GPIO.HIGH)
#    GPIO.output(18, GPIO.HIGH)
#    GPIO.output(25, GPIO.HIGH)
 #   time.sleep(0.5)
  #  GPIO.output(23, GPIO.LOW)
   # GPIO.output(24, GPIO.LOW)
   # GPIO.output(18, GPIO.LOW)
   # GPIO.output(23, GPIO.LOW)
   # time.sleep(0.5)


#for i in range(5):
 #   GPIO.output(23, GPIO.HIGH)
  #  time.sleep(0.5)
   # GPIO.output(23, GPIO.LOW)
    #time.sleep(0.5)
    #GPIO.output(24, GPIO.HIGH)
#    time.sleep(0.5)
 #   GPIO.output(24, GPIO.LOW)
  #  time.sleep(0.5)
   # GPIO.output(18, GPIO.HIGH)
    #time.sleep(0.5)
    #GPIO.output(18, GPIO.LOW)
    #time.sleep(0.5)
#    GPIO.output(25, GPIO.HIGH)
 #   time.sleep(0.5)
  #  GPIO.output(23, GPIO.LOW)
   # time.sleep(0.5)



y = 299999

for i in range(20):
    if y < 1000:
        GPIO.output(23, GPIO.HIGH)
        time.sleep(0.05)
        GPIO.output(23, GPIO.LOW)
        time.sleep(0.05)

    elif y < 2000:
        GPIO.output(23, GPIO.HIGH)
        GPIO.output(24, GPIO.HIGH)
        time.sleep(0.05)
        GPIO.output(23, GPIO.LOW)
        GPIO.output(24, GPIO.LOW)
        time.sleep(0.05)

    elif y < 3000:
        GPIO.output(23, GPIO.HIGH)
        GPIO.output(24, GPIO.HIGH)
        GPIO.output(18, GPIO.HIGH)
        time.sleep(0.05)
        GPIO.output(23, GPIO.LOW)
        GPIO.output(24, GPIO.LOW)
        GPIO.output(18, GPIO.LOW)
        time.sleep(0.05)

    elif y < 4000:
        GPIO.output(23, GPIO.HIGH)
        GPIO.output(24, GPIO.HIGH)
        GPIO.output(18, GPIO.HIGH)
        GPIO.output(25, GPIO.HIGH)
        time.sleep(0.03)
        GPIO.output(23, GPIO.LOW)
        GPIO.output(24, GPIO.LOW)
        GPIO.output(18, GPIO.LOW)
        GPIO.output(25, GPIO.LOW)
        time.sleep(0.03)

    else:
        print ("error")
