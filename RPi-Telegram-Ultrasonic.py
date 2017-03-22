import RPi.GPIO as GPIO
import time
import os
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

TRIG = 12
ECHO = 16
LED = 11
previous = 0
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(LED, GPIO.OUT)

try:
 print "Sensor Siap!!"
 while True:
  GPIO.output(TRIG, False)
  GPIO.output(TRIG, True)
  time.sleep(1)
  GPIO.output(TRIG, False)
  GPIO.output(LED, False)

  while GPIO.input(ECHO) == 0:
   start = time.time()
  while GPIO.input(ECHO) == 1:
   end = time.time()

  duration = end - start
  distance = duration * 17150
  distance = round (distance, 1)
  
  if distance < 20 and distance > 10 and previous ==0:
    print "Terdeteksi"
    print distance
    GPIO.output(LED, GPIO.HIGH)
    os.system('fswebcam -r 640x360 /home/zulfahmi/Foto/photo.jpg')
    GPIO.output(LED, GPIO.LOW)
    os.system('/home/zulfahmi/tg/bin/telegram-cli -k server.pub -WR -e  "send_photo Zeef /home/zulfahmi/Foto/photo.jpg"')
    previous = 1  
  
  elif previous ==1:
    print "Sensor Siap!!"
    previous = 0
    time.sleep(1)
except KeyboardInterrupt:
 GPIO.cleanup()
