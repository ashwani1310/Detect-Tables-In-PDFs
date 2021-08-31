import cv2
import numpy as np
import glob

from pdf2table.imageProcessing import imageEdit,detectLine,createSkeletonImage

cv_img = []
for img in glob.glob("/home/ashwani/alexionformtemplates/templates/*.jpg"):
    n = cv2.imread(img)
    n = cv2.cvtColor(n,cv2.COLOR_BGR2GRAY)
    cv_img.append(n)

#print(len(cv_img))

for i in range(len(cv_img)):
	cv_img[i]=createSkeletonImage.create_skeleton(cv_img[i])
