import numpy as np

from pdf2table.imageProcessing import imageEdit
from pdf2table.imageProcessing import  detectLine
import cv2


def create_skeleton(img):
    """

    :param img: np.array
    :return: np.array
    """
    #filtered_horizontal_lines, all_horizontal_lines, all_vertical_lines = util.get_image_property(img)
    # a = input()
    # tmp = np.copy(img)
    # imageEdit.highlight_line_2(lines=all_horizontal_lines, img=tmp, name="test")

    img = cv2.bilateralFilter(img,9,75,75)
    img_with_line = np.zeros_like(img)
    img_with_line.fill(255)
    contours_horizontal = detectLine.detect_contours_horizontal(img)
    contours_vertical = detectLine.detect_contours_vertical(img)
    cv2.drawContours(img_with_line, contours_horizontal, -1, (0, 0, 0), 2)
    cv2.drawContours(img_with_line, contours_vertical, -1, (0, 0, 0), 2)
    return img_with_line
