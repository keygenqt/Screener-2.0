import tkinter as tk
from dataclasses import dataclass
from pathlib import Path

import pyautogui
from PIL import Image, ImageTk, ImageDraw, ImageGrab

root = tk.Tk()


@dataclass
class Point:
    x1: int
    x2: int
    y1: int
    y2: int


def select(save, extension):
    root.attributes('-fullscreen', True)

    s = pyautogui.screenshot()

    global img
    global photo_img
    img = Image.frombytes(s.mode, (s.width, s.height), s.tobytes(), 'raw')
    photo_img = ImageTk.PhotoImage(img)

    canvas1 = tk.Canvas(root, bd=0, highlightthickness=0, relief='ridge')
    canvas1.pack(side="bottom", fill="both", expand="yes")

    def get_im(event):
        root.one = ImageTk.PhotoImage(
            get_round(img.crop((event.x - 50, event.y - 50, event.x + 100 - 50, event.y + 100 - 50))).resize((200, 200), Image.ANTIALIAS))
        return root.one

    def get_round(im):
        bigsize = (im.size[0] * 3, im.size[1] * 3)
        mask = Image.new('L', bigsize, 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0) + bigsize, fill=255)
        mask = mask.resize(im.size, Image.ANTIALIAS)
        im.putalpha(mask)
        return im

    def mod(point):
        new_point = Point(x1=point.x1, y1=point.y1, x2=point.x2, y2=point.y2)

        if point.x1 > point.x2:
            t = new_point.x2
            new_point.x2 = new_point.x1
            new_point.x1 = t

        if point.y1 > point.y2:
            t = new_point.y2
            new_point.y2 = new_point.y1
            new_point.y1 = t

        return new_point

    def draw_glass(event):
        canvas1.create_image(event.x, event.y, image=get_im(event), anchor="nw")
        canvas1.create_line(event.x + 100, event.y, event.x + 100, event.y + 200, width=1, fill='green')
        canvas1.create_line(event.x, event.y + 100, event.x + 200, event.y + 100, width=1, fill='green')

    def draw_border(point):
        canvas1.create_rectangle(point.x1, point.y1, point.x2, point.y2, outline="red")

    def draw_bg(point):
        global g_press
        global img
        global photo_img

        canvas1.delete("all")
        canvas1.create_image(0, 0, image=photo_img, anchor="nw")

        if point.x1 == 0 and not g_press:
            canvas1.create_rectangle(0, 0, s.width, s.height, outline="", fill="#393939", stipple='gray50')
        else:
            canvas1.create_rectangle(0, 0, s.width, point.y1, outline="", fill="#393939", stipple='gray50')
            canvas1.create_rectangle(0, point.y1, point.x1, point.y2, outline="", fill="#393939", stipple='gray50')
            canvas1.create_rectangle(0, point.y2, s.width, s.height, outline="", fill="#393939", stipple='gray50')
            canvas1.create_rectangle(point.x2, point.y1, s.width, point.y2, outline="", fill="#393939", stipple='gray50')
            draw_border(point)

    def motion(event):
        global g_press
        global g_point

        if g_press:
            if g_point.x1 == 0 and g_point.y1 == 0:
                g_point.x1 = event.x
                g_point.y1 = event.y
                g_point.x2 = event.x
                g_point.y2 = event.y
            else:
                g_point.x2 = event.x
                g_point.y2 = event.y

        draw_bg(mod(g_point))
        draw_glass(event)

    def get_count(path):
        return sum(1 for x in path.glob('**/*') if x.is_file())

    def return_release(event):
        global g_point
        global g_image
        point = mod(g_point)
        g_image = '{}/{}.{}'.format(save, get_count(Path(save)) + 1, extension)
        ImageGrab.grab().crop((point.x1 + 1, point.y1 + 1, point.x2, point.y2)).save(g_image)
        root.destroy()

    def close_escape(event):
        root.destroy()

    def button_press(event):
        if event.num == 1:
            global g_press
            global g_point
            g_press = True
            g_point = Point(x1=0, y1=0, x2=s.width, y2=s.height)

    def button_release(event):
        if event.num == 1:
            global g_press
            g_press = False

    global g_press
    global g_point
    global g_image
    g_image = ''
    g_press = False
    g_point = Point(x1=0, y1=0, x2=s.width, y2=s.height)

    draw_bg(g_point)

    root.bind('<ButtonPress>', button_press)
    root.bind('<ButtonRelease>', button_release)
    root.bind("<Escape>", close_escape)
    root.bind("<KeyRelease-Return>", return_release)
    root.bind('<Motion>', motion)

    root.mainloop()

    return g_image
