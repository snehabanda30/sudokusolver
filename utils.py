####import cv2
####import numpy as np
####from tensorflow.keras.models import load_model


#### READ THE MODEL WEIGHTS
#### def intializePredectionModel():



#### 1 - Preprocessing Image
####def preProcess(img):



#### 3 - Reorder points for Warp Perspective
####def reorder(myPoints):



#### 3 - FINDING THE BIGGEST COUNTOUR ASSUING THAT IS THE SUDUKO PUZZLE
####def biggestContour(contours):


#### 4 - TO SPLIT THE IMAGE INTO 81 DIFFRENT IMAGES
####def splitBoxes(img):



#### 4 - GET PREDECTIONS ON ALL IMAGES
####def getPredection(boxes,model):



#### 6 -  TO DISPLAY THE SOLUTION ON THE IMAGE
####def displayNumbers(img,numbers,color = (0,255,0)):



#### 6 - DRAW GRID TO SEE THE WARP PRESPECTIVE EFFICENCY (OPTIONAL)
####def drawGrid(img):



#### 6 - TO STACK ALL THE IMAGES IN ONE WINDOW
####def stackImages(imgArray,scale):


