import cv2

my_image = cv2.imread("./res/nowruz.png")
my_image_gray = cv2.cvtColor(my_image, cv2.COLOR_BGR2GRAY)
cv2.imwrite("./res/newruz_gray.png", my_image_gray)
my_image_gray[0:10, 0:300] = 0
my_image_gray[0:168, 0:10] = 0
my_image_gray[158:168, 0:300] = 0
my_image_gray[0:168, 290:300] = 0

tea = my_image_gray[105:155, 15:70]
my_image_gray[118:168, 130:185] = tea

cv2.imshow("Croped", tea)
cv2.imshow("MyPic", my_image_gray)
print(my_image_gray.shape)
print(my_image_gray[10, 20])
cv2.waitKey()
