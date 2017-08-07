import cv2
name = 'out'

img = cv2.imread("./{}.ppm".format(name))
cv2.imshow("image", img)
cv2.waitKey(0)

