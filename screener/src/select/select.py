import tkinter as tk

from screener.src.select.point import Point
from screener.src.select.select_image import SelectImage


class Select:
    def __init__(self, ctx):
        self.root = None
        self.canvas = None
        self.data_tk = None
        self.image = SelectImage(ctx)
        self.point = Point(x1=0, y1=0, x2=self.image.data.width, y2=self.image.data.height)
        self.press = False

    def desktop(self):
        """Take screenshot desktop."""
        self.image.save()
        if self.image.is_save:
            return self.image
        else:
            return None

    def area(self):
        """Take screenshot area."""
        self.root = tk.Tk()
        self.root.attributes('-fullscreen', True)
        self.canvas = tk.Canvas(self.root, bd=0, highlightthickness=0, relief='ridge')
        self.canvas.pack(side="bottom", fill="both", expand="yes")

        self.data_tk = self.image.get_image_tk()

        self.root.bind('<ButtonPress>', self.bind_start)
        self.root.bind('<ButtonRelease>', self.bind_end)
        self.root.bind("<Escape>", self.bind_exit)
        self.root.bind("<KeyRelease-Return>", self.bind_done)
        self.root.bind('<Motion>', self.bind_move)

        self.draw_bg_for_area(self.point)

        self.root.mainloop()

        if self.image.is_save:
            return self.image
        else:
            return None

    def bind_start(self, event):
        if event.num == 1:
            self.press = True
            self.point = Point(x1=0, y1=0, x2=self.image.data.width, y2=self.image.data.height)

    def bind_end(self, event):
        if event.num == 1:
            self.press = False

    def bind_exit(self, event):
        self.root.destroy()

    def bind_done(self, event):
        self.image.save(self.point)
        self.root.destroy()

    def bind_move(self, event):
        if self.press:
            if self.point.x1 == 0 and self.point.y1 == 0:
                self.point = Point(x1=event.x, y1=event.y, x2=event.x, y2=event.y)
            else:
                self.point.x2 = event.x
                self.point.y2 = event.y

        mod_point = self.__mod(self.point)
        self.draw_bg_for_area(mod_point)
        self.draw_glass_for_area(event)

    def draw_glass_for_area(self, event):
        """Draw preview zoom for select."""
        # prepare image
        im_crop = SelectImage.get_crop_for_preview(event, self.image.data)
        im_zoom = SelectImage.get_zoom_for_preview(im_crop)
        im_round = SelectImage.get_round_img(im_zoom)
        im_tk = SelectImage.get_crop_tkimage_from_img(self.root, im_round)
        # draw
        self.canvas.create_image(event.x, event.y, image=im_tk, anchor="nw")
        self.canvas.create_line(event.x + 100, event.y, event.x + 100, event.y + 200, width=1, fill='green')
        self.canvas.create_line(event.x, event.y + 100, event.x + 200, event.y + 100, width=1, fill='green')

    def draw_bg_for_area(self, point):
        """Draw background with shadow."""
        # clear
        self.canvas.delete("all")

        # put bg
        self.canvas.create_image(0, 0, image=self.data_tk, anchor="nw")

        w = self.image.data.width
        h = self.image.data.height

        # draw
        if point.x1 == 0 and not self.press:
            self.canvas.create_rectangle(0, 0, w, h, outline="", fill="#393939", stipple='gray50')
        else:
            self.canvas.create_rectangle(0, 0, w, point.y1, outline="", fill="#393939", stipple='gray50')
            self.canvas.create_rectangle(0, point.y1, point.x1, point.y2, outline="", fill="#393939", stipple='gray50')
            self.canvas.create_rectangle(0, point.y2, w, h, outline="", fill="#393939", stipple='gray50')
            self.canvas.create_rectangle(point.x2, point.y1, w, point.y2, outline="", fill="#393939", stipple='gray50')
            self.canvas.create_rectangle(point.x1, point.y1, point.x2, point.y2, outline="red")

    @staticmethod
    def __mod(point):
        """Fix point for all formats."""
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
