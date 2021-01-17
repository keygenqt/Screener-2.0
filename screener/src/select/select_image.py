from pathlib import Path

import pyautogui
from PIL import Image, ImageTk, ImageDraw, ImageGrab


class SelectImage:
    def __init__(self, ctx):
        self.conf_save = ctx.obj.get('save')
        self.conf_extension = ctx.obj.get('extension')
        self.path = self.__get_path_img()
        self.screenshot = pyautogui.screenshot()
        self.data = self.__get_image()
        self.is_save = False

    def __get_path_img(self):
        """Generate path for save screenshot."""
        index = sum(1 for x in Path(self.conf_save).glob('**/*') if x.is_file()) + 1
        return '{}/{}.{}'.format(self.conf_save, index, self.conf_extension)

    def __get_image(self):
        """Get image from bytes."""
        return Image.frombytes(self.screenshot.mode, (self.screenshot.width, self.screenshot.height), self.screenshot.tobytes(), 'raw')

    def save(self, point=None):
        """Save screenshot."""
        if point is None:
            self.screenshot.save(self.path)
        else:
            ImageGrab.grab().crop((point.x1 + 1, point.y1 + 1, point.x2, point.y2)).save(self.path)
        self.is_save = True
        return self.path

    def get_image_tk(self):
        """Image to ImageTk."""
        return ImageTk.PhotoImage(self.data)

    @staticmethod
    def get_zoom_for_preview(image):
        """Zoom crop image for preview select."""
        return image.resize((200, 200), Image.ANTIALIAS)

    @staticmethod
    def get_crop_for_preview(event, image):
        """Crop image for preview select by event mouse move."""
        return image.crop((event.x - 50, event.y - 50, event.x + 100 - 50, event.y + 100 - 50))

    @staticmethod
    def get_crop_tkimage_from_img(tk_root, image):
        """Gen ImageTk without clear."""
        tk_root.one = ImageTk.PhotoImage(image)
        return tk_root.one

    @staticmethod
    def get_round_img(image):
        """Round off the image."""
        bigsize = (image.size[0] * 3, image.size[1] * 3)
        mask = Image.new('L', bigsize, 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0) + bigsize, fill=255)
        mask = mask.resize(image.size, Image.ANTIALIAS)
        image.putalpha(mask)
        return image
