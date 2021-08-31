import cv2
import numpy as np

from pdf2table.imageProcessing import adjustCoordinates
from pdf2table.imageProcessing import detectLine
from pdf2table.imageProcessing import imageEdit


def textRepetitionModule(page, textBlockCoordinates, pageWidth, pageHeight):
    """
        this return the y cooridnates upto whicht that column has to be repeateds
    :param page: int
    :param textBlockCoordinates: x1, x3 coordinates , list
    :param pageWidth: PDF page wioth
    :param pageHeight: PDF page height
    :return: int, int
    """
    img_name = page
    if page / 100 == 0:
        page = "images/study-0" + str(page) + ".ppm"
    else:
        page = "images/study-" + str(page) + ".ppm"
    print(page)
    img = cv2.imread(page)
    # print("shape =>", img.shape)
    adjustedImage = adjustCoordinates.adjustImage(pageWidth, pageHeight, img)
    """
    x------- = l1
    #      #
    #      #
    #------y = l2
    x and y coordinates location
    """
    x = []
    y = []
    x.append(textBlockCoordinates[0])
    x.append(textBlockCoordinates[1])
    y.append(textBlockCoordinates[2])
    y.append(textBlockCoordinates[3])

    x[0] = adjustCoordinates.adjustPdfPointToPixel(x[0])
    x[1] = adjustCoordinates.adjustPdfPointToPixel(x[1])

    y[0] = adjustCoordinates.adjustPdfPointToPixel(y[0])
    y[1] = adjustCoordinates.adjustPdfPointToPixel(y[1])

    l1 = [x[0], x[1], y[0], x[1]]
    l2 = [x[0], y[1], y[0], y[1]]

    # detect line above l1
    # detect all lines lines
    lines = detectLine.detect_all_horizontal_lines(adjustedImage)

    # top
    lineTop, index = detectLine.detect_horizontal_line(lines, l1, position="above")
    # below
    lineBelow, index = detectLine.detect_horizontal_line(lines, l2, position="below")
    tmp = np.copy(adjustedImage)

    imageEdit.highlight_line([lineBelow, lineTop], tmp, name="textLine")

    yTop = adjustCoordinates.adjustPixelsToPdfPoint(lineTop[1])
    yBottom = adjustCoordinates.adjustPixelsToPdfPoint(lineBelow[1])
    # adjustCoordinates.adjustPixelsToPdfPoint

    return yTop, yBottom
