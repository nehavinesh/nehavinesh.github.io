# Define your load_img() function here.
#       Parameters: The name of the file to be opened (string)
#       Returns: The image object with the opened file.
import PIL
from PIL import Image

def load_img(filename):
    image = PIL.Image.open(filename)
    return image

# Define your show_img() function here.
#       Parameters: The image object to display.
#       Returns: nothing.
def show_img(image):
    image = image.rotate(180)
    image.show()


# Define your save_img() function here.
#       Parameters: The image object to save, the name to save the file as (string)
#       Returns: nothing.
def save_img(image,name):
    image.save(name)


# Define your obamicon() function here.
#       Parameters: The image object to apply the filter to.
#       Returns: A New Image object with the filter applied.
def obamicon(image):
    pix_map = image.load()
    width = image.size[0]
    height = image.size[1]
    for x in range(width):
        for y in range(height):
            intensity = 0
            pixel = pix_map[x,y]
            intensity = pixel[0] + pixel[1] + pixel[2]
            if intensity < 182:
                pix_map[x,y] = (0, 51, 76)
            elif intensity >= 182 and intensity < 364:
                pix_map[x,y] = (217, 26, 33)
            elif intensity >= 364 and intensity < 546:
                pix_map[x,y] = (112, 150, 158)
            else:
                pix_map[x,y] = (252, 227, 166)
    return image
