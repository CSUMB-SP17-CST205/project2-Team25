import dlib
import numpy as np
from skimage import io
import random as r #imported to make the file name randomized


class GetPoints: #class container so that code can be reused easily, and is modular
    def __init__(self, image):
        self.predictor_path = "shape_predictor_68_face_landmarks.dat"
        
        self.detector = dlib.get_frontal_face_detector()
        self.predictor = dlib.shape_predictor(self.predictor_path)
        
        self.img = io.imread(image)
        
        self.dets = self.detector(self.img)

    def get_coors(self):
        save_coordinates = open(str(r.randint(0,100)) + 'coordinates.txt', 'a') #randint changes the name of the text file
        
        for k, d in enumerate(self.dets):
            shape = self.predictor(self.img, d)
        
        vec = np.empty([68, 2], dtype = int)
        
        for b in range(68): #gets the coordinates of the picture passed in
            vec[b][0] = shape.part(b).x
            vec[b][1] = shape.part(b).y
            save_coordinates.write(str(vec[b][0]) + " "+ str(vec[b][1]) + "\n") #adds them to the randomized text file

        extra_points = ['514 360', '294 676', '0 680', '599 588', '0 0', '0 400', '0 799', '300 799',
             '599 799', '599 400', '599 0' , '300 0']
        
        for i in range(len(extra_points)): #this accesses the array of extra points and writes them into the text file
            save_coordinates.write(extra_points[i] + "\n")
        
        save_coordinates.close() #this closes the picture

name = "ted_cruz" #this will have to be gotten from the user instead of hardcoding
image = name + ".jpg"

x = GetPoints(image) #pass the file name into the class to be converted into a text file
x.get_coors() #this calls the object so that files can be used appropriately

