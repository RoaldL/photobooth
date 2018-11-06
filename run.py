from photobooth.camera import CameraController
from photobooth.gui import GUI
from photobooth.button import ArcadeButton

import os
import sys
from tkinter import Tk

if __name__ == "__main__":

    # Setup
    root = os.path.join(os.sep, 'home', 'pi', 'projects', 'photobooth')
    path = os.path.join(root, 'images')
    
    camera = CameraController(path)
    button = ArcadeButton()

    # Run
    gui = Tk()
    gui.attributes('-fullscreen', True)
    gui.bind('<Escape>',lambda e: gui.destroy())

    my_gui = GUI(gui, root, camera, button)
    gui.mainloop()
    
    