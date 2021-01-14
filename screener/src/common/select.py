from tkinter import *

import pyautogui
from PIL import Image, ImageTk

root = Tk()


def select():
    root.attributes('-fullscreen', True)

    def close_escape(event=None):
        print("escaped")
        root.destroy()

    s = pyautogui.screenshot()
    img = ImageTk.PhotoImage(Image.frombytes(s.mode, (s.width, s.height), s.tobytes(), 'raw'))
    a = Label(root, image=img)
    a.pack(side="bottom", fill="both", expand="yes")
    a.pack()

    root.bind("<Escape>", close_escape)

    root.mainloop()

    return '/image/id.jpg/png'
