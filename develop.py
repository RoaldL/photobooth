from photobooth.camera import Canon100mController, StubController
from photobooth.gui import GUI

import os
import sys
from tkinter import Tk

if __name__ == "__main__":

    # Setup
    path = os.path.join(os.sep, 'home', 'roald', 'projects', 'photobooth', 'images')
    camera_controller = Canon100mController(path)

    # Run
    root = Tk()
    root.attributes('-fullscreen', True)
    root.bind('<Escape>',lambda e: root.destroy())

    my_gui = GUI(root, camera_controller)
    root.mainloop()
    
    