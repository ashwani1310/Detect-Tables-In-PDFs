import cv2
import numpy as np

from pdf2table.imageProcessing import adjustCoordinates
from pdf2table.imageProcessing import columnSpan
from pdf2table.imageProcessing import detectLine


def detectBlockLine(page, pageWidth, pageHeight, left, top, right, bottom):
    """
         //TODO
    :param page: int
    :param pageWidth: int
    :param pageHeight:  int
    :param left: int
    :param top: int
    :param right: int
    :param bottom: int
    :return: to be concluded
    """
    # to normalize bottom point
    bottom = bottom - 3
    # read image
    img_name = page
    if page / 100 == 0:
        page = "images/study-0" + str(page) + ".ppm"
    else:
        page = "images/study-" + str(page) + ".ppm"
    print(page)
    img = cv2.imread(page)
    # print("shape =>", img.shape)
    adjustedImage = adjustCoordinates.adjustImage(pageWidth, pageHeight, img)
    p1, p2, p3, p4 = adjustCoordinates.adjustCoordinates([left, top, right, bottom], pageWidth, pageHeight)
    print "coordinates", p1, p2, p3, p4
    copyImage = np.copy(img)

    # detect lines
    lines = detectLine.detect_all_horizontal_lines(adjustedImage)
    # horizontal line
    horizontalLines = []
    horizontalLines.append([p1[0], p1[1], p2[0], p2[1]])
    horizontalLines.append([p3[0], p3[1], p4[0], p4[1]])

    # vertical line
    verticalLines = []
    verticalLines.append([p1[0], p1[1], p3[0], p3[1]])
    verticalLines.append([p2[0], p2[1], p4[0], p4[1]])
    # imageEdit.highlight_line([horizontalLines[0], horizontalLines[1], verticalLines[0], verticalLines[1]], adjustedImage)

    # top
    lineTop, index = detectLine.detect_horizontal_line(lines, horizontalLines[0], position="above")
    # below

    lineBelow1, index = detectLine.detect_horizontal_line(lines, horizontalLines[1], position="below")
    lineBelow2, index = detectLine.detect_horizontal_line(lines, horizontalLines[1], position="above")

    if np.abs(lineBelow1[1] - horizontalLines[1][1]) < np.abs(lineBelow2[1] - horizontalLines[1][1]):
        lineBelow = lineBelow1
    else:
        lineBelow = lineBelow2
    # left
    # lineLeft, index = detect_line.detect_vertical_line(lines, verticalLines[0] ,position="left")
    # right
    # lineRight, index = detect_line.detect_vertical_line(lines, verticalLines[1] ,position="right")
    # get left line
    lineLeft = [lineTop[0], lineTop[1], lineBelow[0], lineBelow[1]]
    lineRight = [lineTop[2], lineTop[3], lineBelow[2], lineBelow[3]]
    # crop image
    croppedImage = adjustedImage[lineTop[1]:lineBelow[3], lineTop[0]:lineBelow[2]]
    cv2.imwrite("cropped.png", croppedImage)

    tmp = np.copy(adjustedImage)
    # imageEdit.highlight_line([lineTop, lineBelow, lineLeft, lineRight], tmp, name = str(img_name))
    # imageEdit.highlight_line([horizontalLines[0], horizontalLines[1], verticalLines[0], verticalLines[1]], tmp, name = str(img_name))

    # verticalLines = detect_line.detect_all_vertical_lines(adjustedImage)
    # detect corner
    # corners = cornerDetection.cornerDetection("cropped.png")
    # lines = detect_line.detect_all_horizontal_lines(croppedImage)
    # l2 = detect_line.detect_all_vertical_lines(croppedImage)
    # tmp2 = np.copy(adjustedImage)
    # imageEdit.highlight_line(verticalLines, tmp2)
    columnSpan.getyValuesSpanningColumns(img_name, croppedImage, lineTop, lineBelow, lineTop, lineRight)
    return adjustedImage
