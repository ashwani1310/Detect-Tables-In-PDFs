import sys

import numpy as np


def is_horizontal_line(line):
    """
        it returns whether line is horizontal or vertical
    returns True if line is horizontal and False if line is vertical
    :param line: line coorinates list
    :return: bool
    """
    if line[0] - line[2] == 0:
        return False
    elif line[1] - line[3] == 0:
        return True


def is_x_lie_in_between(line1, line2):
    """
        it returns whether line lies under the area convered by line1 line
    :param line1: list
    :param line2: list
    :return: bool
    """
    if int(line1[0]) <= int(line2[0]) and int(line1[2]) >= int(line2[2]):
        return True
    else:
        return False


def is_y_lie_in_between(line1, line2):
    """
        it returns whether line1 covers line2 in y axis
    :param line1: list
    :param line2: list
    :return: bool
    """
    if int(line1[1]) <= int(line2[1]) and int(line1[3]) >= int(line2[3]):
        return True
    else:
        return False


def is_y_lie_in_left(line1, line2):
    """
        returns True if lies in left and return Flase if it lies in right
    :param line1: list
    :param line2: list
    :return: bool
    """
    if (line1[1] - line2[1]) < 0:
        return True
    elif (line1[1] - line2[1]) > 0:
        return False
    else:
        return None


def distance_line_horizontal(line1, line2, position="above"):
    """
        calculate Distance between line1 and line2 in horizontal way
    return distance
    :param line1: list
    :param line2: list
    :param position:
    :return:
    """
    inf = 0x3f3f3f
    try:
        # print("position =>", position)
        if position == "above":
            if is_horizontal_line(line1) and is_x_lie_in_between(line1, line2) and line1[1] < line2[1]:
                d = np.abs(int(line1[1]) - int(line2[1]))
                return d

            elif not is_horizontal_line(line1):
                return inf
            else:
                return inf
        elif position == "below":
            if is_horizontal_line(line1) and is_x_lie_in_between(line1, line2) and line1[1] >= line2[1]:
                d = np.abs(int(line1[1]) - int(line2[1]))

                return d
            elif not is_horizontal_line(line1):
                return inf
            else:
                return inf
    except Exception as e:
        print("error =>", e)


def distance_line_vertical(line1, line2, position="left"):
    """
    calculates Distance between line1 and line 2 in vertical way means on y axis
    returns distance on y axis
    """
    inf = 0x3f3f3f
    try:
        print("position =>", position)
        if position == "left":
            if not is_horizontal_line(line1) and is_y_lie_in_left(line1, line2) and is_y_lie_in_between(line1, line2):
                d = np.abs(np.int64(line1[0]) - np.int64(line2[0]))
                print("line =>", line1)
                return d
            elif is_horizontal_line(line1):
                return inf
            else:
            	return inf
        elif position == "right":
            if not is_horizontal_line(line1) and not is_y_lie_in_left(line1, line2) and is_y_lie_in_between(line1, line2):
                d = np.abs(np.int64(line1[0]) - np.int64(line2[0]))
                return d
            elif is_horizontal_line(line1):
            	return inf
            else:
            	return inf
    except Exception as e:
        print("error =>", e)


def line_length(l):
    """
    it calculates eucluidean distance between two points
    """
    x1, y1, x2, y2 = l
    t1 = (np.power((x2 - x1), 2))
    t2 = (np.power((y2 - y1), 2))
    distance = np.sqrt(t1 + t2)
    return distance


def rearrange_coordinates(l):
    """
    it rearranges the coordinates
    :param l:
    :return:
    """
    t1 = [l[0], l[1]]
    t2 = [l[2], l[3]]
    if np.sum(t1) > np.sum(t2):
        return [l[2], l[3], l[0], l[1]]
    else:
        return l


def intersect_line(line1, line2):
    """
    //TODO don't use
    returns True if line2 touches line1  else False
    :param line1:
    :param line2:
    :return: bool
    """
    # if line 2  is horizontal
    if (line1[0] >= line2[0] and line1[0] <= line2[2]):
        return True
    else:
        return True


def unblock_shaped(arr, h, w):
    """
    Return an array of shape (h, w) where
    h * w = arr.size

    If arr is of shape (n, nrows, ncols), n sublocks of shape (nrows, ncols),
    then the returned array preserves the "physical" layout of the sublocks.
    """
    n, nrows, ncols = arr.shape
    return (arr.reshape(h // nrows, -1, nrows, ncols)
            .swapaxes(1, 2)
            .reshape(h, w))


def rect_to_line(rect1):
    x1, y1, x2, y2 = rect1
    top = [x1, y1, x2, y1]
    right = [x2, y1, x2, y2]
    bottom = [x1, y2, x2, y2]
    left = [x1, y1, x1, y2]
    return top, right, bottom, left


def area_under_the_curve(rect1, rect2):
    """
    Return the ratio of area covered by rect2 of rect1. area(rect1) >= area(rect2)
    :param rect1: list/tuple Co-ordinates of rect1
    :param rect2: list/tuple Co-ordinates of rect2
    :return:float  ratio of area covered.
    """
    left = max(rect1[0], rect2[0])
    right = min(rect1[2], rect2[2])
    bottom = min(rect1[3], rect2[3])
    top = max(rect1[1], rect2[1])
    height = line_length([left, top, left, bottom])
    width = line_length([left, top, right, top])
    rect2_height = line_length([rect2[0], rect2[1], rect2[0], rect2[3]])
    rect2_width = line_length([rect2[0], rect2[1], rect2[2], rect2[1]])
    if left < right and top < bottom:
        return (height * width) / (rect2_height * rect2_width)
    return -1
