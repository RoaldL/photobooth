import RPi.GPIO as GPIO

import threading
import time

class ArcadeButton:

    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(3, GPIO.OUT)
        GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        self.keep_blinking = True

    def start_blink(self):
        self.keep_blinking = True
        self.blink_thread = threading.Thread(target=self._blink).start()

    def stop_blink(self):
        self.keep_blinking = False
        
    def get_status(self):
        return GPIO.input(13)  

    def _blink(self):
        
        while(self.keep_blinking):
            GPIO.output(3, 1)
            time.sleep(1)

            GPIO.output(3, 0)
            time.sleep(1)
