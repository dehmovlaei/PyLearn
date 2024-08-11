import cv2

image = cv2.imread("./res/bat.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("row", image)
rows, cols = image.shape
threshold = 100
_, image = cv2.threshold(image, 100, 255, cv2.THRESH_BINARY_INV)
cv2.putText(image, "BATMAN",
            (350, 444), cv2.FONT_HERSHEY_SIMPLEX, 1.5, 256, 3)
cv2.imshow("result", image)
cv2.imwrite("./res/bat_bw.jpg", image)
cv2.waitKey()