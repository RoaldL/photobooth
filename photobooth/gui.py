from tkinter import Tk, Frame, Label, Button, PhotoImage, CENTER
from PIL import Image, ImageTk

import os
import itertools
import random

class GUI:
    def __init__(self, master, camera_controller):
        self.master = master
        self.camera = camera_controller

        master.title("A simple GUI")

        master.configure(background='#313131')

        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)

        self.shoot_number = 0
        self.state = 'idle'

        self.render()

    def render(self):
        
        try:
            self.frame.destroy()
        except:
            pass
        
        self.frame=Frame(self.master)
        self.frame.grid()

        if self.state == 'idle':
            self.greet_button = Button(self.frame, text="Start photoshoot", command=self.start_photoshoot)
            self.greet_button.grid(row=0, column=0)

            self.close_button = Button(self.frame, text="Close", command=self.master.quit)
            self.close_button.grid(row=0, column=1)

            self.photos = {}

            for idx, picture in enumerate(self.camera.pictures[-6:]):
                image = Image.open(picture)
                image.thumbnail([500, 500], Image.ANTIALIAS)
                photo = ImageTk.PhotoImage(image)
                self.photos[idx] = Label(self.frame, image=photo)
                self.photos[idx].image = photo # keep a reference!
                if idx <=2:
                    self.photos[idx].grid(row=1, column=idx)
                else:
                    self.photos[idx].grid(row=2, column=idx-3)

        if self.state == 'countdown':
            self.countdown_label = GIF(self.frame, 'gif/countdown/countdown.gif', 200)
            self.countdown_label.pack()            
            self.photoshoot()

        if self.state == 'black':
            self.master.after(2000, self.funny_gif)

        if self.state == 'wait':

            funny_gifs_path = os.path.join('gif', 'funny')
            funny_gifs = [os.path.join(funny_gifs_path, f) for f in os.listdir(funny_gifs_path) if os.path.isfile(os.path.join(funny_gifs_path, f))]
            self.reaction = GIF(self.frame, random.choice(funny_gifs), 100)
            self.reaction.pack()

            self.master.after(3000, self.wait_for_camera)

    def start_photoshoot(self):
        self.shoot_number = 0
        self.state = 'countdown'        
        self.render()

    def photoshoot(self):
        if self.countdown_label.idx == (len(self.countdown_label.frames) - 10):
            self.camera.get_picture()
            self.shoot_number = self.shoot_number + 1
        
        if self.countdown_label.idx == (len(self.countdown_label.frames) - 1):  
            self.state = 'black'
            self.render()
            return
        
        self.master.after(200, self.photoshoot)

    def funny_gif(self):
        self.state = 'wait'
        self.render()

    def wait_for_camera(self):
        self.camera.wait_for_camera()

        if self.shoot_number < 1:
            self.state = 'countdown' 
        else:
            self.state = 'idle'

        self.render()

class GIF(Label):
    def __init__(self, master, filename, delay):
        im = Image.open(filename)
        seq =  []
        try:
            while 1:
                seq.append(im.copy())
                im.seek(len(seq)) # skip to next frame
        except EOFError:
            pass # we're done

        try:
            self.delay = delay
        except KeyError:
            self.delay = 100

        first = seq[0].convert('RGBA')
        self.frames = [ImageTk.PhotoImage(first)]

        Label.__init__(self, master, image=self.frames[0])

        temp = seq[0]
        for image in seq[1:]:
            temp.paste(image)
            frame = temp.convert('RGBA')
            self.frames.append(ImageTk.PhotoImage(frame))

        self.idx = 0

        self.cancel = self.after(self.delay, self.play)

    def play(self):
        self.config(image=self.frames[self.idx])
        self.idx += 1
        if self.idx == len(self.frames):
            self.idx = 0
        self.cancel = self.after(self.delay, self.play)  
