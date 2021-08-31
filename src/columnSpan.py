import cv2
import numpy as np


def getyValuesSpanningColumns(page, croppedImage, lineTop, lineBelow, lineLeft, lineRight):
	"""
	//TODO
	:param page:
	:param croppedImage:
	:param lineTop:
	:param lineBelow:
	:param lineLeft:
	:param lineRight:
	:return:
	"""
	try:
		tmp = np.copy(croppedImage)
		# print("shape =>", croppedImage.shape)
		# lines = detect_line.detect_all_vertical_lines(tmp)
		# imageEdit.highlight_line(lines, tmp, page )
		cv2.imwrite("tmp/" + str(page) + ".png", croppedImage)
	except Exception as e:
		print("error =>", e, page)
