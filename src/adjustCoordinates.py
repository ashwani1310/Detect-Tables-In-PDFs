import cv2


def adjustCoordinates(points, pageWidth, pageHeight):
    """

    :param points: coordinates (pdf point)
    :param pageWidth: width of pdf page
    :param pageHeight: height of pdf page
    :return: changed coordinates
    """
    left, top, right, bottom = points[0], points[1], points[2], points[3]

    if (pageHeight > pageWidth):
        # adjusting y coordinate
        # adjust y coordinate by 10
        adjust_factor = 10
        y1 = adjustPoint(top, adjust_factor)
        y2 = adjustPoint(bottom, adjust_factor)
    elif (pageWidth > pageHeight):
        # adjust x coordinate by 3 and y coordinate by 4
        adjust_factor = 5
        x1 = adjustPoint(left, adjust_factor)
        x2 = adjustPoint(right, adjust_factor)
        adjust_factor = 4
        y1 = adjustPoint(top, adjust_factor)
        y2 = adjustPoint(bottom, adjust_factor)
    left = adjustPdfPointToPixel(left)
    top = adjustPdfPointToPixel(top)
    right = adjustPdfPointToPixel(right)
    bottom = adjustPdfPointToPixel(bottom)
    p1 = [left, top]
    p2 = [right, top]
    p3 = [left, bottom]
    p4 = [right, bottom]
    return p1, p2, p3, p4


def adjustImage(pageWidth, pageHeight, img_new):
    """

    :param pageWidth: (int) pdf page height
    :param pageHeight: (int) pdf page width
    :param img_new: (np.array) img numpy array
    :return:
    """
    # middle pdf coordinates
    pdfWidth = pageWidth * 0.66
    pdfHeight = pageHeight * 0.66

    # conversion to image pixels
    imgWidth = int(pdfWidth * 1.38)
    imgHeight = int(pdfHeight * 1.38)
    print("imgWidth =>", imgWidth, "imgHeight =>", imgHeight)

    img_re = cv2.resize(img_new, (imgWidth, imgHeight))

    return img_re


def adjustPdfPointToPixel(x):
    """
        this convert pdf point to pixels
    :param x: int
    :return: int
    """
    x = x * 0.66
    x = x * 1.38
    return int(x)


def adjustPixelsToPdfPoint(x):
    """
        thi0s converts pixel to pdf point
    :param x: int
    :return: int
    """
    x = x * 0.72
    x = x * 1.501
    return int(x)


def adjustPoint(pt, adjust_factor):
    return pt + adjust_factor

def adjustPointSub(pt, adjust_factor):
	return pt + adjust_factor


def reverseAdjustCoordinates(points, pageWidth, pageHeight):
    """
    Input : left, top, right, bottom most coordinates of a rectangular block
    convert coordinates from pixel to PDF point and return into a format
    Output : returns  topLeft, topRight, bottomLeft, bottomRight coordinates
    :param points: np.Array
    :param pageWidth: int
    :param pageHeight: int
    :return: np.Array, np.Array, np.Array, np.Array
    """
    left, top, right, bottom = points[0], points[1], points[2], points[3]

    left = adjustPixelsToPdfPoint(left)
    top = adjustPixelsToPdfPoint(top)
    right = adjustPixelsToPdfPoint(right)
    bottom = adjustPixelsToPdfPoint(bottom)
    if (pageHeight > pageWidth):
        # adjusting y coordinate
        # adjust y coordinate by 10
        adjust_factor = 10
        top = adjustPointSub(top, adjust_factor)
        bottom = adjustPointSub(bottom, adjust_factor)
    elif (pageWidth > pageHeight):
        # adjust x coordinate by 3 and y coordinate by 4
        adjust_factor = 5
        x1 = adjustPointSub(left, adjust_factor)
        x2 = adjustPointSub(right, adjust_factor)
        adjust_factor = 4
        y1 = adjustPointSub(top, adjust_factor)
        y2 = adjustPointSub(bottom, adjust_factor)

    p1 = [left, top]
    p2 = [right, top]
    p3 = [left, bottom]
    p4 = [right, bottom]
    return p1, p2, p3, p4
