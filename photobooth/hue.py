from phue import Bridge
import random

class HueController:

    def __init__(self):
        self.bridge = Bridge() # Enter bridge IP here.
        #If running for the first time, press button on bridge and run with b.connect() uncommented
        #bridge.connect()
        self.lights = self.bridge.get_light_objects()

    def set_for_photo(self):
        for light in self.lights:
            light.brightness = 254
            light.xy = [random.random(),random.random()]

    def set_for_wait(self):
        for light in self.lights:
            light.brightness = 0
            light.xy = [random.random(),random.random()]
