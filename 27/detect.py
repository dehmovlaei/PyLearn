import cv2

def get_color_name(value):
    if value < 75:
        return "Black"
    elif 100 > value > 75:
        return "Gray"
    else:
        return "White"

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('./res/detect.avi', fourcc, 20.0, (640, 480))
_, frame = cap.read()
square_size = 85
height, width = frame.shape[:2]
x_center = width // 2
y_center = height // 2
x1 = x_center - square_size // 2
y1 = y_center - square_size // 2
x2 = x_center + square_size // 2
y2 = y_center + square_size // 2

while True:
    _, frame = cap.read()
    blurred_frame = cv2.GaussianBlur(frame, (77, 77), 0)
    blurred_frame[y1:y2, x1:x2] = frame[y1:y2, x1:x2]
    gray = cv2.cvtColor(blurred_frame, cv2.COLOR_BGR2GRAY)
    center_x, center_y = blurred_frame.shape[1] // 2, blurred_frame.shape[0] // 2
    cv2.rectangle(blurred_frame, (x1, y1), (x2, y2), (0, 0, 0), 2)
    center_value = gray[center_y, center_x]
    color_name = get_color_name(center_value)
    cv2.putText(blurred_frame, color_name, (10, 30), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.circle(blurred_frame, (center_x, center_y), 5, (255, 255, 255), -1)
    out.write(blurred_frame)
    cv2.imshow('Color Detector', blurred_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
