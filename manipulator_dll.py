from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance

def image_info(image_name):
    with Image.open(image_name) as variable:
        return (
            str(variable.size) + "\n" +
            str(variable.format) + "\n" +
            str(variable.mode)
        )

def MBW(line_edit):
    image_name = line_edit.text()
    with Image.open(image_name) as variable:
        blackandwhite = variable.convert('L')
        blackandwhite.show()

def blur(line_edit):
    image_name = line_edit.text()
    with Image.open(image_name) as variable:
        BLUR_image = variable.filter(ImageFilter.BLUR)
        BLUR_image.show()

def contour(line_edit):
    image_name = line_edit.text()
    with Image.open(image_name) as variable:
        CONTOUR_image = variable.filter(ImageFilter.CONTOUR)
        CONTOUR_image.show()

def emboss(line_edit):
    image_name = line_edit.text()
    with Image.open(image_name) as variable:
        EMBOSS_image = variable.filter(ImageFilter.EMBOSS)
        EMBOSS_image.show()

def flip(line_edit):
    image_name = line_edit.text()
    with Image.open(image_name) as variable:
        FLIP_image = variable.transpose(Image.FLIP_LEFT_RIGHT)
        FLIP_image.show()

def rotate(line_edit):
    image_name = line_edit.text()
    with Image.open(image_name) as variable:
        ROTATE_image = variable.transpose(Image.ROTATE_180) # Разворот
        ROTATE_image.show()