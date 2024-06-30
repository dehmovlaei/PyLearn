import cv2

woman_image = cv2.imread("./res/1.jpg")
man_image = cv2.imread("./res/2.jpg")
inverted_woman = cv2.bitwise_not(woman_image)
inverted_man = cv2.bitwise_not(man_image)
cv2.imshow("woman", inverted_woman)
cv2.imshow("man", inverted_man)
cv2.waitKey(0)
cv2.destroyAllWindows()
