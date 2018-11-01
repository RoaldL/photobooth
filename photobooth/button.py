import threading
import time

class ArcadeButton:

    def __init__(self):
        print('init button')
        self.keep_blinking = True

    def start_blink(self):
        print('start blink')
        self.keep_blinking = True
        self.blink_thread = threading.Thread(target=self._blink).start()

    def stop_blink(self):
        print('set off')
        self.keep_blinking = False

    def _blink(self):
        
        while(self.keep_blinking):
            print('on')
            time.sleep(1)

            print('off')
            time.sleep(1)
