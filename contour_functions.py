import cv2
import numpy as np


def contour_circularity(contour):
    area = cv2.contourArea(contour)
    perimeter = cv2.arcLength(contour, True)
    try:
        circularity = (4 * np.pi * area) / (perimeter ** 2)
    except ZeroDivisionError:
        circularity = 1.
    print('area:', area, '\tlength:', perimeter, '\t circularity:', circularity)
    return circularity


def contour_center(contour):
    # Compute mass center of contour
    moment = cv2.moments(contour)
    cx = int(moment["m10"] / moment["m00"])
    cy = int(moment["m01"] / moment["m00"])
    return cx, cy
