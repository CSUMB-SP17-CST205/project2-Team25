#Santiago Bruno Gonzalez
#Project 1: Write a median filter program using Python and Pillow to create a new image from the 9 images without the pesky tourist
#Link to Git Hub Repository: https://github.com/CSUMB-SP17-CST205/sbruno-team6
from PIL import Image

# This opens up each image individualy and also converst it to the RGB values.
image1 = Image.open("hillary_clinton.jpg").convert("RGB")
image2 = Image.open("ted_cruz.jpg").convert("RGB")
# image3 = Image.open("3.png").convert("RGB")
# image4 = Image.open("4.png").convert("RGB")
# image5 = Image.open("5.png").convert("RGB")
# image6 = Image.open("6.png").convert("RGB")
# image7 = Image.open("7.png").convert("RGB")
# image8 = Image.open("8.png").convert("RGB")
# image9 = Image.open("9.png").convert("RGB")

#This gives us the height and width of an image. In this case it gets it from image 1
width, height = image1.size

#This is the emty list in which the new, median value, RGB values will be stored
RGBs = []

#This nested loop goes through each pixel coordinate on all 9 images
for y in range(height):
    for x in range(width):
        #These are the empty lists in which the Red, Green, & Blue values will be stored
        red = []
        green = []
        blue = []
#This gets the RGB values from Image [ 1 ] and appends them to the lists mentined above.-------------------------------------------------------
        r1, g1 ,b1 = image1.getpixel((x,y))
        red.append(r1)
        green.append(g1)
        blue.append(b1)
#This gets the RGB values from Image [ 2 ] and appends them to the lists mentined above.-------------------------------------------------------
        r2, g2 ,b2 = image2.getpixel((x,y))
        red.append(r2)
        green.append(g2)
        blue.append(b2)
#This gets the RGB values from Image [ 3 ] and appends them to the lists mentined above.-------------------------------------------------------
        # r3, g3 ,b3 = image3.getpixel((x,y))
        # red.append(r3)
        # green.append(g3)
        # blue.append(b3)
#This gets the RGB values from Image [ 4 ] and appends them to the lists mentined above.-------------------------------------------------------
#         r4, g4 ,b4 = image4.getpixel((x,y))
#         red.append(r4)
#         green.append(g4)
#         blue.append(b4)
# #This gets the RGB values from Image [ 5 ] and appends them to the lists mentined above.-------------------------------------------------------
#         r5, g5 ,b5 = image5.getpixel((x,y))
#         red.append(r5)
#         green.append(g5)
#         blue.append(b5)
# #This gets the RGB values from Image [ 6 ] and appends them to the lists mentined above.-------------------------------------------------------
#         r6, g6 ,b6 = image6.getpixel((x,y))
#         red.append(r6)
#         green.append(g6)
#         blue.append(b6)
# #This gets the RGB values from Image [ 7 ] and appends them to the lists mentined above.-------------------------------------------------------
#         r7, g7 ,b7 = image7.getpixel((x,y))
#         red.append(r7)
#         green.append(g7)
#         blue.append(b7)
# #This gets the RGB values from Image [ 8 ] and appends them to the lists mentined above.-------------------------------------------------------
#         r8, g8 ,b8 = image8.getpixel((x,y))
#         red.append(r8)
#         green.append(g8)
#         blue.append(b8)
# #This gets the RGB values from Image [ 9 ] and appends them to the lists mentined above.-------------------------------------------------------
#         r9, g9 ,b9 = image9.getpixel((x,y))
#         red.append(r9)
#         green.append(g9)
#         blue.append(b9)
#--------------------------------------------------------
#This sorts the RGB values stored in the lists named: red, green, blue, and stores them in the variables: r, g, b.
        r = sorted(red)
        g = sorted(green)
        b = sorted(blue)
        
        #This takes the median value of each sorted list and adds it to our empty list called: RGBs
        RGBs.append((r[len(r)/2], g[len(g)/2], b[len(b)/2]))

#This creates a new image with RGB values and with the width and height
endResult = Image.new("RGB", (width,height))
#This puts all the RGB values into the new image
endResult.putdata(RGBs)
#This saves the newly created image
endResult.save("end.png")
#slkfsdabvgfuifsda