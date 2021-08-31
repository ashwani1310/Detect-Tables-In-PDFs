import cv2
import numpy as np


def detect_rect(img):
    """
    it detects the rectangles in the images
    if finds the rectangles which encloses minimum area
    :param img: np.array
    :return: list
    """
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]
    image, cnts, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    rect_coordinates = []
    for cnt in cnts:
        rect = cv2.minAreaRect(cnt)
        box = cv2.boxPoints(rect)
        # box = np.int(box)
        rect_coordinates.append(box)
        # box  # <- statement seems to have no effect
        # cv2.drawContours(again, [box], 0, (0, 255, 0), 2)
    return rect_coordinates
