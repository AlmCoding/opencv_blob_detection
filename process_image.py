import cv2
import numpy as np
from circle_detector import detect_circles


def process_image(img):
    r, b, rc, bc = detect_circles(img.copy())
    img = cv2.drawContours(img, (rc, bc), -1, (0, 0, 0), 3)

    rc_radius = np.sqrt(4 * cv2.contourArea(rc) / np.pi)
    # dx = abs(r[0] - b[0])
    # dy = abs(r[1] - b[1])

    cv2.arrowedLine(img, b, r, (0, 0, 0), int(rc_radius/4))

    # pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
    # pts = pts.reshape((-1, 1, 2))
    # cv2.polylines(img, [pts], True, (0, 255, 255))

    return img
