import cv2
import numpy as np

my_image = np.ones((600, 800), dtype=np.uint8) * 255
my_image = np.array(my_image, dtype=np.uint8)
cv2.rectangle(my_image, (111, 44), (350, 410), 0, 7)
cv2.circle(my_image, (230, 225), 100, 120, 10)
cv2.line(my_image, (0, 100), (100, 0), 0, 45)
cv2.putText(my_image, "Python is the best programing language",
            (20, 500), cv2.FONT_HERSHEY_SIMPLEX, 1, 0)
cv2.imshow("result", my_image)
cv2.waitKey()
