import cv2
import numpy as np 
import pytesseract

from pdf2table.imageProcessing import adjustCoordinates
from pdf2table.imageProcessing import detectLine
from pdf2table.imageProcessing import imageEdit
from pdf2table.imageProcessing import coordinateGeometry
from pdf2table.imageProcessing import ocr

def removeAmbiguity(page, textBlockCoordinates, pageWidth, pageHeight):
	"""
	this function detects line between text and it tries to find out text and 
	line position so that it can be mapped properly to column

	"""
	img_name = page
	if page / 100 == 0:
		page = "images/study-0"+ str(page) +".ppm"
	else:
		page = "images/study-"+ str(page) +".ppm"
	print(page)
	img  = cv2.imread(page)
	adjustedImage = adjustCoordinates.adjustImage(pageWidth, pageHeight, img)
	"""
	x1,y1------- = l1
    #      		#
    #      		#
    #------x2,y2= l2
	x and y coordinates location
	"""

	x1 = (textBlockCoordinates[0])
	y1 = (textBlockCoordinates[1])
	x2 = (textBlockCoordinates[2])
	y2 = (textBlockCoordinates[3])


	x1 = adjustCoordinates.adjustPdfPointToPixel(x1)
	y1 = adjustCoordinates.adjustPdfPointToPixel(y1)

	x2 = adjustCoordinates.adjustPdfPointToPixel(x2)
	y2 = adjustCoordinates.adjustPdfPointToPixel(y2)
	#crop image 

	croppedImage = adjustedImage[y1:y2, x1:x2]
	cv2.imwrite("tmp/cropped.png", croppedImage)
	minLineLength = 20
	lines = detectLine.detect_all_vertical_lines(croppedImage, min_line_length= minLineLength, shape = 1)
	distance =  []
	for x1,y1,x2,y2 in lines:
		distance.append(coordinateGeometry.line_length(x1, y1, x2, y2))
	dimension = croppedImage.shape
	print("shape = >",croppedImage.shape)
	maxValue = np.max(distance)
	print("max =>", distance)
	bifurcateLines = []
	for i in range(0, len(distance)):
		if distance[i] == maxValue:
			bifurcateLines.append(lines[i])


	sortedBifurcateLines = sorted(bifurcateLines, key = lambda x : x[0])


	tmp = np.copy(croppedImage)
	imageEdit.highlight_line(lines = lines, img = tmp, name=  "crp")

	realBeginXCoordinate = x1 

	beginLine = [0,0,0,dimension[0]]
	endLine = [dimension[1],0, dimension[1], dimension[0]]


	prevLine = beginLine

	textBoundries = []
	for i in range(0, len(sortedBifurcateLines)):
		line = coordinateGeometry.rearrange_coordinates(sortedBifurcateLines[i])
		if i == len(sortedBifurcateLines) - 1:
			tmpImg = croppedImage[prevLine[1]:endLine[3], prevLine[0]:endLine[2]]

			print(tmpImg.shape)
			text = ocr.getTextFromImage(tmpImg)
			print("data =>",text, sortedBifurcateLines[i])
			if text is not '':
				t = {}
				t["text"] = text
				t["xValueStart"] = realBeginXCoordinate + prevLine[0]
				t["xValueEnd"] = realBeginXCoordinate + endLine[0]
				textBoundries.append(t)

		else:
			tmpImg = croppedImage[prevLine[1]:line[3], prevLine[0]:line[2]]
			print(tmpImg.shape)
			text = ocr.getTextFromImage(tmpImg)
			print("data =>",text, sortedBifurcateLines[i])
			if text is not '':
				t = {}
				t["text"] = text
				t["xValueStart"] = realBeginXCoordinate + prevLine[0]
				t["xValueEnd"] = realBeginXCoordinate + line[0]
				textBoundries.append(t)

 		prevLine = line


 	#remove repeting values
 	seen = set()
	new_l = []
	for d in textBoundries:
	    t = tuple(d.items())
	    if t not in seen:
	        seen.add(t)
	        new_l.append(d)

 	print new_l

















 