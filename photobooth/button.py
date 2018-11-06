import os    
import threading
import time


if os.uname()[1] == 'raspberrypi':
    import RPi.GPIO as GPIO

class ArcadeButton:

    def __init__(self):
        if os.uname()[1] == 'raspberrypi':
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(3, GPIO.OUT)
            GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        self.keep_blinking = True
        self.count = 0

    def start_blink(self):
        self.keep_blinking = True
        self.blink_thread = threading.Thread(target=self._blink).start()

    def stop_blink(self):
        self.keep_blinking = False
        
    def get_status(self):
        if os.uname()[1] == 'raspberrypi':
            return GPIO.input(13)  
        else:
            if self.count <= 5:
                time.sleep(1)
                self.count = self.count + 1
                return True
            else:
                self.count = 0
                return False

    def _blink(self):
        
        while(self.keep_blinking):
            if os.uname()[1] == 'raspberrypi':
                GPIO.output(3, 1)
                time.sleep(1)

                GPIO.output(3, 0)
                time.sleep(1)
            else:
                print('blink on')
                time.sleep(1)

                print('blink off')
                time.sleep(1)
