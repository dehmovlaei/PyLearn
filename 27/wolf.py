import cv2


image = cv2.imread("./res/wolf.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
print(image.shape)