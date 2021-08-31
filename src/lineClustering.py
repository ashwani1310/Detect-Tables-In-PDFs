import numpy as np
from pdf2table.imageProcessing import coordinateGeometry
import sympy
def checkCluster(cluster, line):
    """
    it creates clusters of lines which forms any geometric figure
    so that table can be detected
    :param cluster:
    :param line:
    :return:
    """
    # print("lines = >", line)
    for id in cluster.keys():
        tmpLine  = coordinateGeometry.rearrange_coordinates(line)
        lines = cluster[id]
        # print("tmp =>", tmpLine[0] - tmpLine[2])
        isHorizontal = coordinateGeometry.is_horizontal_line(tmpLine)
        if isHorizontal:
            # print("yes horizontal ", tmpLine, id)
            if (tmpLine not in lines):
                for l in lines:
                    # print("ss => ", l)
                    # print(tmpLine, cluster[id])
                    isHorizontal = coordinateGeometry.is_horizontal_line(l)
                    if not isHorizontal:
                        # print("not horizontal", l)
                        t1 = coordinateGeometry.rearrange_coordinates(l)
                        l1 = sympy.Line([t1[0], t1[1]], [t1[2], t1[3]])
                        l2 = sympy.Line([tmpLine[0], tmpLine[1]], [tmpLine[2], tmpLine[3]])
                        intersectionPt = sympy.intersection(l1, l2)
                        print(intersectionPt, l1, l2)
                        if len(intersectionPt) != 0:
                            return True, id
    return False, None



# def checkCluster(cluster, line):
#     """
#
#     :param cluster:
#     :param line:
#     :return:
#     """
#     for id in cluster.keys():
#         return False, None


def lineClustering(lines):
    """

    :param lines:
    :return:
    """
    # coordinateGeometry.unblockshaped(lines, 2, 3)
    tmp = []
    for l in range(len(lines)):
        tmp.append(lines[l][0])
    # print(tmp)
    # tmp = [[10, 10, 10, 20], [5, 15, 30, 15]]
    #pick any line at random
    # x = 1
    x = np.random.randint(len(tmp))
    t = {}
    t[0] = []
    t[0].append(tmp[x])
    clusterCount = 0
    for i in tmp:
        flag, clusterID = checkCluster(t, i)
        if flag:
            t[clusterID].append(i)
        elif not flag:
            clusterCount += 1
            t[clusterCount] = []
            t[clusterCount].append(i)

    return t
