import cv2
import numpy as np

# Create a white image with a specified width and height
width, height = 255, 255
white_image = np.ones((height, width, 3), dtype=np.uint8) * 255
brightness = 255
for i in range(0, 255):
    white_image[i, 0:255] = brightness
    brightness -= 1

cv2.imshow("My gradient", white_image)
cv2.waitKey(0)
cv2.destroyAllWindows()