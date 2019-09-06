import cv2
import numpy as np
from contour_functions import contour_circularity
from contour_functions import contour_center


# Color ranges
red_range1 = ((159, 100, 100), (179, 255, 255))
red_range2 = ((0, 100, 100), (20, 255, 255))
blue_range = ((100, 100, 100), (140, 255, 255))

# Contour properties
max_contour_size = 1e6
min_contour_size = 1e1
min_contour_circ = 0.7


def detect_circles(img):
    # Blur image
    img = cv2.medianBlur(img, 5)

    # Mask colors
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Red
    red_mask1 = cv2.inRange(img_hsv, red_range1[0], red_range1[1])
    red_mask2 = cv2.inRange(img_hsv, red_range2[0], red_range2[1])
    red_mask = cv2.bitwise_or(red_mask1, red_mask2)

    # Blue
    blue_mask = cv2.inRange(img_hsv, blue_range[0], blue_range[1])

    red_contours = extract_contours(red_mask)
    blue_contours = extract_contours(blue_mask)

    # TODO Smart contour matching
    # ...

    # Get contour centers
    red_contour = red_contours[0]
    blue_contour = blue_contours[0]

    red_center = contour_center(red_contour)
    blue_center = contour_center(blue_contour)

    return red_center, blue_center, red_contour, blue_contour


def extract_contours(mask):
    # Extract contours
    contours, _ = cv2.findContours(mask.astype(np.uint8), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Reject to small and to big contours
    contours = [c for c in contours if min_contour_size < cv2.contourArea(c) < max_contour_size]

    # Reject contours with low circularity
    contours = [c for c in contours if contour_circularity(c) > min_contour_circ]

    # Sort contours according area
    contours = sorted(contours, key=lambda e: cv2.contourArea(e), reverse=True)

    return contours
