import cv2
import numpy as np

# Create a white image with a specified width and height
width, height = 255, 255
white_image = np.ones((height, width, 3), dtype=np.uint8) * 255
x1, x2 = 55, 90
for i in range(0, 100):
    white_image[i, x1:x2] = 0
    if x1 > 0:
        x1 -= 1
        x2 -= 1
    elif x2 > 0:
        x2 -= 1

cv2.imshow("Death symbol", white_image)
cv2.waitKey(0)
cv2.destroyAllWindows()