from phue import Bridge
import threading
import random
import time

class HueController:

    def __init__(self):
        self.bridge = Bridge('192.168.1.107') # Enter bridge IP here.
        #If running for the first time, press button on bridge and run with b.connect() uncommented
        #bridge.connect()
        self.lights = self.bridge.get_light_objects()
        
        for light in self.lights:
            print(light.brightness)
            print(light.xy)

        self.state = 'off'
        self.on_off_toggle = False

    def set_off(self):
        self.stop_blink()
        self.bridge.set_group(1, 'on', False)
        self.state = 'off'

    def set_on(self):
        self.stop_blink()
        self.bridge.set_group(1, 'on', True)
        self.bridge.set_group(1, 'xy', [0.4578, 0.41])
        self.bridge.set_group(1, 'brightness', 254)

        self.state = 'photo'

    def start_blink(self):
        self.keep_blinking = True
        self.blink_thread = threading.Thread(target=self._blink).start()

    def stop_blink(self):
        self.keep_blinking = False

    def _blink(self):
        print('blinkieblinkie')
        while(self.keep_blinking):
            for light in self.lights:
                if self.on_off_toggle:
                    light.on = True
                    light.xy = [random.random(),random.random()]
                else:
                    light.on = False
                time.sleep(0.05)
                self.on_off_toggle = not self.on_off_toggle
                if not self.keep_blinking:
                    break
