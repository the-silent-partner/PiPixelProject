## Importing the relevent directories
from PIL import Image
import os.path
from Pi100Million import Pi100Mil

## Setting the boundries
total_digits = len(Pi100Mil)-2
total_poss_area = total_digits/9

## Welcome message
print u"-- Welcome to the \u03c0 Pixel Project."
print u"-- Please pick a width and height for your \u03c0 image."
print "-- A total area of %d pixels is currently possible." % total_poss_area

## Setting the main funtions
width = int(raw_input("Width? "))
height = int(raw_input("Height? "))
pixels = width * height
indices = range(pixels)
file_name = 'PiPixels_%sx%s' % (width,height)

## Checking for errors
if width < 1:
    print "- Sorry, we can't have a image width below 1, try running the script again..."
    exit()
elif height < 1:
    print "- Sorry, we can't have a image height below 1, try running the script again..."
    exit()
elif pixels > total_poss_area:
    print "- Sorry, that total area is too big, try running the script again..."
    exit()
else:
    print "Creating..."

## Defining the pi range
def pi_digits(pi_Range):
    n = range(2,len(pi_Range), 3)
    return n

## Creating the new image
im = Image.new("RGB", (width,height), (0,0,0))

## Putting the pi pixels on the new image file
for i in indices:
    x = i % width
    y = i / width
    r = (i*9)+2
    g = (i*9)+5
    b = (i*9)+8
    red = int(int(Pi100Mil[r:r+3]) * 0.256256256256)
    green = int(int(Pi100Mil[g:g+3]) * 0.256256256256)
    blue = int(int(Pi100Mil[b:b+3]) * 0.256256256256)
    im.putpixel((x,y), (red,green,blue))
    ##print i, ':', (x,y), (r,g,b), (red,green,blue)

## write out
im.save(file_name + '.png', "PNG")
print "Congratulations!"
print u"Your new \u03c0 pixel image can be found here:" + os.path.join(os.getcwd(), file_name + '.png')
##im.show()
