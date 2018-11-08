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
        try:
            self.stop_blink()
            self.bridge.set_group(1, 'on', False)
            self.state = 'off'
        except:
            pass

    def set_on(self):
        try:
            self.stop_blink()
            self.bridge.set_group(1, 'on', True)
            self.bridge.set_group(1, 'xy', [0.4578, 0.41])
            self.bridge.set_group(1, 'brightness', 254)

            self.state = 'photo'
        except:
            pass

    def start_blink(self):
        try:
            self.keep_blinking = True
            self.blink_thread = threading.Thread(target=self._blink).start()
        except:
            pass

    def stop_blink(self):
        self.keep_blinking = False

    def _blink(self):
        try:
            while(self.keep_blinking):
                for light in self.lights:
                    if self.on_off_toggle:
                        light.transitiontime = 0
                        light.on = True
                        light.xy = [random.random(),random.random()]
                    else:
                        light.transitiontime = 0
                        light.on = False
                    time.sleep(0.05)
                    self.on_off_toggle = not self.on_off_toggle
                    if not self.keep_blinking:
                        break
        except:
            pass

class HueStubController:

    def __init__(self):
        print('hue - init')

    def set_off(self):
        print('hue - set off')

    def set_on(self):
        print('hue - set on')

    def start_blink(self):
        print('hue - start blink')

    def stop_blink(self):
        print('hue - stop blink')
