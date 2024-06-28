import cv2
import numpy as np

# Create a black image with a specified width and height
width, height = 640, 640
chess_board = np.zeros((height, width, 3), dtype=np.uint8)
row, col = 0, 0
for i in range(0, 8):
    for j in range(0, 8):
        if (i + j) == 0 or ((i + j) % 2) == 0:
            chess_board[row:row + 80, col:col + 80] = 255
        col += 80
    col = 0
    row += 80
# Display the black image
cv2.imshow("chess_board Image", chess_board)
cv2.waitKey(0)
cv2.destroyAllWindows()