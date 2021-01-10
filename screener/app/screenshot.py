from tkinter import *

import click
import pyautogui
from PIL import Image, ImageTk

root = Tk()


@click.group(name='screenshot')
def cli_screenshot():
    """This script prints some colors.  If colorama is installed this will
    also work on Windows.  It will also automatically remove all ANSI
    styles if data is piped into a file.
    Give it a try!
    """
    pass


def close_escape(event=None):
    print("escaped")
    root.destroy()


@cli_screenshot.command()
def hello():
    root.attributes('-fullscreen', True)

    s = pyautogui.screenshot()
    img = ImageTk.PhotoImage(Image.frombytes(s.mode, (s.width, s.height), s.tobytes(), 'raw'))
    a = Label(root, image=img)
    a.pack(side="bottom", fill="both", expand="yes")
    a.pack()

    root.bind("<Escape>", close_escape)

    root.mainloop()
