from phue import Bridge
import random

class HueController:

    def __init__(self):
        self.bridge = Bridge('192.168.1.107') # Enter bridge IP here.
        #If running for the first time, press button on bridge and run with b.connect() uncommented
        #bridge.connect()
        self.lights = self.bridge.get_light_objects()
        
        for light in self.lights:
            print(light.brightness)
            print(light.xy)

    def set_for_photo(self):
        for light in self.lights:
            light.brightness = 254
            light.xy = [0.4578, 0.41]

    def set_for_wait(self):
        for light in self.lights:
            light.brightness = 1
            light.xy = [random.random(),random.random()]
