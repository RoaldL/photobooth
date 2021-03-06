from photobooth.camera import CameraController
from photobooth.gui import GUI
from photobooth.button import ArcadeButton
from photobooth.hue import HueController, HueStubController

import os
import sys
from tkinter import Tk

if __name__ == "__main__":

    # Setup
    root = os.path.join(os.sep, 'home', 'pi', 'projects', 'photobooth')
    path = os.path.join(os.sep, 'media', 'pi', 'photobooth')
    
    camera = CameraController(path)
    button = ArcadeButton()
    
    try:
        hue = HueController()
    except:
        hue = HueStubController()

    # Run
    gui = Tk()
    gui.attributes('-fullscreen', True)
    gui.bind('<Escape>',lambda e: gui.destroy())

    my_gui = GUI(gui, root, camera, button, hue, False)
    gui.mainloop()
    
    
