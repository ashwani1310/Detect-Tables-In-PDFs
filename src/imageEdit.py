import cv2


def highlight_line(lines, img, name):
    """
    this function works with python3 and cv3 + version
    :param lines:
    :param img:
    :param name:
    :return:
    """
    # print("shape =>", img.shape)
    for i in lines:
        x1, y1, x2, y2 = i[0]
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 2)

    cv2.imwrite("tmp/" + name + ".png", img)


# cv2.imwrite('houghlines_1.png',img)
def highlight_line_2(lines, img, name):
    """
    this function works with python2/python 3 
    :param lines:
    :param img:
    :param name:
    :param print: bool
    :return:
    """

    # print("shape =>", img.shape)
    for x1, y1, x2, y2 in lines:
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 2)
    cv2.imwrite("tmp/" + name + ".png", img)


def black_line(lines, img):
    for x1, y1, x2, y2 in lines:
        cv2.line(img, (x1, y1), (x2, y2), (0, 0, 0), 3)


def whiteLine(lines, img):
    """
    it replaces black line with white line
    :param lines:
    :param img:
    :return:
    """
    for x1, y1, x2, y2 in lines:
        cv2.line(img, (x1, y1), (x2, y2), (255, 255, 255), 3)
    cv2.imwrite('houghlines_white.png', img)


def whiteOutBlock(textCoordinates, page):
    """
    #TODO need to  rethink
    :param textCoordinates:
    :param page:
    :return:
    """
    # TODO
    print(len(textCoordinates))
    # restructure image

    print(textCoordinates[1])
    for i in textCoordinates[0]:
        rectCoordinates = i.getRect()
        # cv2.rectangle()
        pass

# def white_out_text(textBlockList, img):
#     """
#     it remove all the text present in the image
#     :param textBlock: object of textBlock class
#     :param img:np.array
#     :return:np.array i.e. img
#     """
#     coordinateList = []
#     for i in textBlockList:
#         r = i.getRect()
#         coordinateList.append(util.return_converted_rect(r))
#     for i in coordinateList:
#         pt1, pt2 = [i[0], i[1]], [i[2], i[3]]
#         # print(pt1, pt2)
#         cv2.rectangle(img, tuple(pt1), tuple(pt2), (255, 255, 255), 10)
#     print("writing file")
#     cv2.imwrite("tmp/white.png", img)
#     return img
