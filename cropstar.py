import import os

from PIL import Image

# subfunction to crop image and save it as a new file.
def crop_image(img, crop_area, new_filename):
    cropped_image = img.crop(crop_area)
    cropped_image.save(new_filename)

# (x1, y1, x2, y2) coordinates of to crop, you can use pint to figure out the pixel coordinates
crop_areas = [(180, 242, 330, 566), (340, 150, 900, 570)]

image_name = 'download.jpg' #here you need to add your image name
img = Image.open(image_name)

# Loops so that it goes though all the areas.
for i, crop_area in enumerate(crop_areas):
    filename = os.path.splitext(image_name)[0]
    ext = os.path.splitext(image_name)[1]
    new_filename = filename + '_cropped' + str(i) + ext

    crop_image(img, crop_area, new_filename)
