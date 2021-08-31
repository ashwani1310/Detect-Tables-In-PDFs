import cv2.cv as cv


def cornerDetection(name):
    # params
    # blockSize = 2
    # ksize = 3
    # k = 0.4

    # #detecting corner
    # out = cv2.cornerHarris(im, blockSize, ksize, k, cv2.BORDER_DEFAULT)
    # convert it into iplimage
    # img = cv2.cvtColor(realimg,cv2.COLOR_BGR2GRAY)
    # im = cv.CreateImageHeader((img.shape[1], img.shape[0]), cv.IPL_DEPTH_8U, 3)
    # cv.SetData(im, img.tostring(), img.dtype.itemsize * 3 * img.shape[1])

    im = cv.LoadImage(name, cv.CV_LOAD_IMAGE_GRAYSCALE)

    dst_32f = cv.CreateImage(cv.GetSize(im), cv.IPL_DEPTH_32F, 1)

    neighbourhood = 3
    aperture = 3
    k = 0.01
    maxStrength = 0.0
    threshold = 0.01
    nonMaxSize = 3
    print(type(im))
    cv.CornerHarris(im, dst_32f, neighbourhood, aperture, k)

    minv, maxv, minl, maxl = cv.MinMaxLoc(dst_32f)

    dilated = cv.CloneImage(dst_32f)
    cv.Dilate(dst_32f,
              dilated)  # By this way we are sure that pixel with local max value will not be changed, and all the others will

    localMax = cv.CreateMat(dst_32f.height, dst_32f.width, cv.CV_8U)
    cv.Cmp(dst_32f, dilated, localMax,
           cv.CV_CMP_EQ)  # compare allow to keep only non modified pixel which are local maximum values which are corners.

    threshold = 0.01 * maxv
    cv.Threshold(dst_32f, dst_32f, threshold, 255, cv.CV_THRESH_BINARY)

    cornerMap = cv.CreateMat(dst_32f.height, dst_32f.width, cv.CV_8U)
    cv.Convert(dst_32f, cornerMap)  # Convert to make the and
    cv.And(cornerMap, localMax, cornerMap)  # Delete all modified pixels

    radius = 3
    thickness = 2

    l = []
    for x in range(cornerMap.height):  # Create the list of point take all pixel that are not 0 (so not black)
        for y in range(cornerMap.width):
            if cornerMap[x, y]:
                l.append((y, x))

    for center in l:
        cv.Circle(im, center, radius, (0, 0, 255), thickness)

    cv.SaveImage("corner.png", im)

    return l
