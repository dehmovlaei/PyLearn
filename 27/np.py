import cv2
import numpy as np

# my_image = np.ones((250, 350), dtype=np.uint8) * 255
while True:
    my_image = np.random.random((600, 800)) * 255
    my_image = np.array(my_image, dtype=np.uint8)
    cv2.imshow("result", my_image)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break