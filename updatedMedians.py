from PIL import Image
import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
###    from documents on ilearn    ###
# Creates a function to find median with myList as a parameter
def medianOdd(myList): 
# Stores the length of the pixel list in the variable amtPixels
    listLength = len(myList)
# Sorts the list from lowest to highest
    sortedValues = sorted(myList)
# Adds 1 to the listLength, in order to start array at 1, splits 
# the array it in half, and subtracts to negate the zero index
    middleIndex = ((listLength + 1)/2) - 1
# Returns the object located at the middleIndex
    return sortedValues[middleIndex]
###             ###              ###

# Leaves a blank array to store the images in
imgs = []   
# A loop to iterate through the images
for p in range (1, 3):
# Opens the image where the index is at
    imgs.append(Image.open(str(p) + ".jpg"))

for i in range (len(imgs)):
    
    gray = cv2.cvtColor(imgs[i], cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.485, 5)
# print(faces)
    for (i, (x,y,w,h)) in enumerate(faces):
        
        cv2.rectangle(imgs[i], (x, y), (x+w, y+h), (255, 0, 0), 2)
        
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = imgs[i][y:y+h, x:x+w]
    
    cv2.imwrite(str(i) + ".jpg", imgs[i])
# Sets w to width and h to height of a 3D array
w, h = imgs[0].size
# Stores a new image into variable called editedImage
editedImage = Image.new("RGB", (w, h), 0)
# Loads the new image onto a variable called pixels
pixels = editedImage.load()
# Iterates through x-values
for x in range(w):
# Iterates through y-values
    for y in range(h):
# Blank arrays for storing pixels
        red = []
        green = []
        blue = []
# Iterates through images
        for i in (imgs):
# Sets a variable to obtain pixels within an image
            newRed, newGreen, newBlue = i.getpixel((x, y))
# Attaches pixel colors to the blank arrays
            red.append(newRed)
            green.append(newGreen)
            blue.append(newBlue)
# Calls the function for each color value, and stores them onto the new image
        pixels [x, y] = (medianOdd(red), medianOdd(green), medianOdd(blue))
# Saves the final image
editedImage.save("finalImage.jpg")