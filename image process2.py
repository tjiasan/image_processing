import numpy as np
import cv2
from os import listdir
from matplotlib import pyplot as plt
import os


image_files= os.listdir("/home/jason/Desktop/adhesion 31")
#list of all image files
text_file= open("average values.txt","w")
for i in range (1, len(image_files)):
    # get the file names
    FileName= image_files[i]
    
    if FileName[-4:] == ".tif":
        #load the image matrix
        img= cv2.imread(FileName,0)
        # apply the algorithm
        

        sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=3) 
        #plot to check
##        plt.subplot(2,2,2),plt.imshow(laplacian,cmap= 'gray')
##        plt.title("Laplacian"), plt.imshow(laplacian,cmap='gray')
##        plt.show()

        #inverting the image

        sobelx=(255-sobelx)

        #eliminate background noise


        #saving the image
        new_name= "/home/jason/Desktop/adhesion 31 process/"+ str(FileName[:-4])+ "_sobel.jpg"
        cv2.imwrite (new_name, sobelx)

        img1=cv2.imread(new_name,0)

        ret,thresh1 = cv2.threshold(img1,230,255,cv2.THRESH_BINARY)

        #calculate average value
        kernel= np.ones((5,5),np.uint8)
        dilation= cv2.erode(thresh1, kernel,iterations=1)
        avgimagevalue= np.mean(dilation)
        
        #write average value to file
        
        towrite= FileName+ ";"+ str(avgimagevalue)+ " \n"
        text_file.write(towrite)
        text_file.flush()
        
        cv2.imwrite (new_name, dilation)
        
        
        
       



















