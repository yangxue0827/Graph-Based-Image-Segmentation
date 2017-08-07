import cv2

name = 'yangxue'
img = cv2.imread("./{}.jpg".format(name))
cv2.imwrite("./{}.ppm".format(name), img)