import cv2


image = cv2.imread("./res/wolf.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("row", image)
rows, cols = image.shape

threshold = 100
for r in range(rows):
    for c in range(cols):
        if image[r, c] > threshold:
            image[r, c] = 255
        else:
            image[r, c] = 0

cv2.imshow("result", image)
cv2.waitKey()