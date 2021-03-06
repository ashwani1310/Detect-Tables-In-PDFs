import cv2
import numpy as np

from pdf2table.imageProcessing import coordinateGeometry


def detect_line(img):
    """

    :param img: numpy array of image
    :return: return np.array
    """

    # define kernel for morphological processes
    kernel = np.ones((4, 4), np.uint8)
    # erode operation
    erosion = cv2.erode(img, kernel, iterations=1)
    # dilation operation
    dilation = cv2.dilate(erosion, kernel, iterations=1)
    # convert BGR to gray scale

    gray = cv2.cvtColor(dilation, cv2.COLOR_BGR2GRAY)
    # detect edges with canny edge detection algorithm
    edges = cv2.Canny(img, 50, 150, apertureSize=3)
    cv2.imwrite('edges.png', edges)
    min_line_length = 100
    max_line_gap = 10
    # detect lines by hough transform
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 100, min_line_length, max_line_gap)

    return lines[0]


def detect_all_horizontal_lines(img, convert_to_gray = True):
    """
       it detectes all horizontal lines present in image
    :param img: np.array
    :return: list
    """
    if convert_to_gray:
    	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #bw = cv2.adaptiveThreshold(~gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 15, -2) 
    #shape = gray.shape
	#for i in xrange(shape[0]):
	#	for j in xrange(shape[1]):
	#		if gray[i][j]>194:
	#			gray[i][j]=0 
	#		else:
	#			gray[i][j]=255
		
    
    bw = cv2.adaptiveThreshold(~gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 15, -2)
    horizontal = np.copy(gray)

    horizontal_size = horizontal.shape[1] / 30
    horizontal_structure = cv2.getStructuringElement(cv2.MORPH_RECT, (int(horizontal_size), 1))
    # horizontal_structure_dilate = cv2.getStructuringElement(cv2.MORPH_RECT, (int(horizontal_size_dilate), 1))

    # apply morphological ops
    horizontal = cv2.erode(horizontal, horizontal_structure)
    horizontal = cv2.dilate(horizontal, horizontal_structure)

    # print(horizontal.shape)

    edges = cv2.Canny(horizontal, 50, 150, apertureSize=3)
    min_line_length = 100
    max_line_gap = 10
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 100, min_line_length, max_line_gap)
    # as lines is in shape (1,2,1)
    tmp = []
    if lines is not None:
        for i in lines:
            tmp.append(i[0])
    return tmp


def detect_all_vertical_lines(img, min_line_length=10, shape=45):
    """
        it returns all vertical lines detected in image
    :param img: np.array
    :param min_line_length: minimum line distance
    :param shape: shape size
    :return:
    """
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #shape = gray.shape
	#for i in xrange(shape[0]):
	#	for j in xrange(shape[1]):
	#		if gray[i][j]>194:
	#			gray[i][j]=0 
	#		else:
	#			gray[i][j]=255
		

    bw = cv2.adaptiveThreshold(~gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 15, -2)
    vertical = np.copy(gray)
    shape = shape
    vertical_size = vertical.shape[0] / shape
    # vertical_size_dilate = vertical.shape[0] / 60
    vertical_structure = cv2.getStructuringElement(cv2.MORPH_RECT, (1, int(vertical_size)))
    # vertical_structure_dilate = cv2.getStructuringElement(cv2.MORPH_RECT, (1, int(vertical_size_dilate)))
    vertical = cv2.erode(vertical, vertical_structure)
    vertical = cv2.dilate(vertical, vertical_structure)
    not_vertical = cv2.bitwise_not(vertical)

    edges = cv2.Canny(not_vertical, 50, 150, apertureSize=3)

    # cv2.imwrite('edges1.png', edges)
    # minLineLength = 4
    # maxLineGap = 10
    # lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength,maxLineGap)
    # lines = cv2.HoughLinesP(edges, rho=1, theta=np.pi / 270, threshold=19, minLineLength=1, maxLineGap=2)
    lines = cv2.HoughLinesP(edges, rho=1, theta=np.pi / 270, threshold=10, minLineLength=min_line_length, maxLineGap=20)
    # as lines is in shape (1,2,1)
    tmp = []
    if lines is not None:
        for i in lines:
            tmp.append(i[0])
    return tmp


def detect_horizontal_line(lines, line, position="above"):
    """

    :param lines: list
    :param line: line coordinates
    :param position: Above or Below
    :return: lines Coordinates, index number
    """
    x = np.apply_along_axis(coordinateGeometry.distance_line_horizontal, 1, lines, line, position)
    index = np.argmin(x)
    return lines[index], index


def detect_vertical_line(lines, line, position="left"):
    """

    :param lines: list
    :param line: line coordinates
    :param position: left or right
    :return: lines coordinates, index number
    """
    x = np.apply_along_axis(coordinateGeometry.distance_line_vertical, 1, lines, line, position)
    index = np.argmin(x)
    return lines[index], index


def remove_horizontal_lines(img, lines):
    pass


def detect_contours_vertical(img, shape=45):
    """
    this detects all the vertical components(shape or objects) in  given image
    :param img: np.array
    :return: list i.e contours
    """

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
   # shape = gray.shape
	#for i in xrange(shape[0]):
	#	for j in xrange(shape[1]):
	#		if gray[i][j]>194:
	#			gray[i][j]=0 
	#		else:
	#			gray[i][j]=255
		

    bw = cv2.adaptiveThreshold(~gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 15, -2)
    vertical = np.copy(gray)
    shape = shape
    vertical_size = vertical.shape[0] / shape
    # vertical_size_dilate = vertical.shape[0] / 60
    vertical_structure = cv2.getStructuringElement(cv2.MORPH_RECT, (1, int(vertical_size)))
    # vertical_structure_dilate = cv2.getStructuringElement(cv2.MORPH_RECT, (1, int(vertical_size_dilate)))
    vertical = cv2.erode(vertical, vertical_structure)
    vertical = cv2.dilate(vertical, vertical_structure)
    not_vertical = cv2.bitwise_not(vertical)

    edges = cv2.Canny(not_vertical, 50, 150, apertureSize=3)
    ret, thresh = cv2.threshold(edges, 127, 255, 0)
    im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    return contours


def detect_contours_horizontal(img):
    """
    it
    :param img:
    :return:
    """
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
   # shape = gray.shape
	#for i in xrange(shape[0]):
	#	for j in xrange(shape[1]):
	#		if gray[i][j]>194:
	#			gray[i][j]=0 
	#		else:
	#			gray[i][j]=255
		

    bw = cv2.adaptiveThreshold(~gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 15, -2)
    horizontal = np.copy(gray)

    horizontal_size = horizontal.shape[1] / 30
    horizontal_structure = cv2.getStructuringElement(cv2.MORPH_RECT, (int(horizontal_size), 1))
    # horizontal_structure_dilate = cv2.getStructuringElement(cv2.MORPH_RECT, (int(horizontal_size_dilate), 1))

    # apply morphological ops
    horizontal = cv2.erode(horizontal, horizontal_structure)
    horizontal = cv2.dilate(horizontal, horizontal_structure)

    # print(horizontal.shape)

    edges = cv2.Canny(horizontal, 50, 150, apertureSize=3)
    ret, thresh = cv2.threshold(edges, 127, 255, 0)
    im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    return contours
