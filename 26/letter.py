import cv2
import numpy as np

# Create a white image with a specified width and height
width, height = 640, 640
white_image = np.ones((height, width, 3), dtype=np.uint8) * 255
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 15
font_color = (0, 0, 0)  # Black color
thickness = 10
x, y = 200, 450
cv2.putText(white_image, 'A', (x, y), font, font_scale, font_color, thickness)
cv2.imshow("My Letter", white_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Create a white image with a specified width and height
width, height = 640, 640
white_image = np.ones((height, width, 3), dtype=np.uint8) * 255
white_image[250:270, 250:390] = 0
white_image[150:170, 310:330] = 0
y1, y2 = 150, 170
x1,x2, x3, x4 = 310, 330, 310, 330
for i in range (0, 10):
    y1 += 10
    y2 += 20
    x1 -= 10
    x2 -= 10
    x3 += 10
    x4 += 10
    white_image[y1:y2, x1:x2] = 0
    white_image[y1:y2, x3:x4] = 0
cv2.imshow("My Letter", white_image)
cv2.waitKey(0)
cv2.destroyAllWindows()