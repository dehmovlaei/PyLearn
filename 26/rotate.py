import cv2

image = cv2.imread("./res/3.jpg")
angle = 180
center = (image.shape[1] // 2, image.shape[0] // 2)
rotation_matrix = cv2.getRotationMatrix2D(center, angle, scale=1.0)
rotated_image = cv2.warpAffine(image, rotation_matrix, (image.shape[1], image.shape[0]))
cv2.imshow("man", rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
