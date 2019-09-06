import cv2
import numpy as np


image_hsv = None        # global ;(
pixel = (20, 60, 80)    # some stupid default


# mouse callback function
def pick_color(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        pixel = image_hsv[y, x]

        # you might want to adjust the ranges(+-10, etc):
        hue = 20    # default 10
        sat = 20    # default 10
        val = 50    # default 40
        upper = np.array([pixel[0] + hue, pixel[1] + sat, pixel[2] + val])
        lower = np.array([pixel[0] - hue, pixel[1] - sat, pixel[2] - val])
        print(pixel, lower, upper)

        image_mask = cv2.inRange(image_hsv, lower, upper)
        cv2.imshow("mask", image_mask)


def main():
    import sys
    global image_hsv, pixel

    image_src = cv2.imread(sys.argv[1])
    image_src = cv2.resize(image_src, (0, 0), fx=0.25, fy=0.25)
    image_src = cv2.medianBlur(image_src, 5)

    if image_src is None:
        print("Image read is None!")
        return
    cv2.imshow("bgr", image_src)

    cv2.namedWindow('hsv')
    cv2.setMouseCallback('hsv', pick_color)

    # now click into the hsv img , and look at values:
    image_hsv = cv2.cvtColor(image_src, cv2.COLOR_BGR2HSV)
    cv2.imshow("hsv", image_hsv)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
