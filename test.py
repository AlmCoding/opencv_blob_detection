import cv2
from process_image import process_image

img = cv2.imread('t6.jpg')
img = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)

img2 = process_image(img.copy())

cv2.imshow("image 2", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()


"""

red 108, 200, 170 
blue 170, 160, 185

[111 180 116] [ 91 160  76] [131 200 156]
[108 202 168] [ 88 182 128] [128 222 208]

blue
hue 200 - 250 
sat 70 - 100
val 50 - 100

red
hue -25 - 25 
sat 70 - 100
val 50 - 100



[171 169 133] [151 149  93] [191 189 173]
[170 160 183] [150 140 143] [190 180 223]

"""
