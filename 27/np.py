import cv2
import numpy as np

# my_image = np.ones((250, 350), dtype=np.uint8) * 255
my_image = np.random.random((250, 350)) * 255
my_image = np.array(my_image, dtype=np.uint8)
cv2.imshow("result", my_image)
cv2.waitKey()