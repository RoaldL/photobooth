from tkinter import * 



     


root = Tk()
anim = MyLabel
anim.pack()

def stop_it():
    anim.after_cancel(anim.cancel)

Button(root, text='stop', command=stop_it).pack()

root.mainloop()

