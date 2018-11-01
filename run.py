from photobooth.camera import CameraController
from photobooth.gui import GUI
from photobooth.button import ArcadeButton

import os
import sys
from tkinter import Tk

if __name__ == "__main__":

    # Setup
    path = os.path.join(os.sep, 'home', 'pi', 'projects', 'photobooth', 'images')
    camera = CameraController(path)
    button = ArcadeButton()

    # Run
    root = Tk()
    root.attributes('-fullscreen', True)
    root.bind('<Escape>',lambda e: root.destroy())

    my_gui = GUI(root, camera, button)
    root.mainloop()
    
    