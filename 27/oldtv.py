import cv2
import numpy as np
import imageio

tv_image = cv2.imread('./res/oldTV.png', cv2.IMREAD_COLOR)
tv_image_copy = tv_image.copy()
x, y, w, h = 40, 40, 418, 300
frames = []

while True:
    noise = np.random.random((h, w)) * 255
    noise = np.array(noise, dtype=np.uint8)
    noise = cv2.cvtColor(noise, cv2.COLOR_GRAY2BGR)
    tv_image_copy[y:y + h, x:x + w] = cv2.addWeighted(tv_image_copy[y:y + h, x:x + w], 0.5, noise, 0.5, 0)
    cv2.imshow("TV Noise", tv_image_copy)
    tv_image_rgb = cv2.cvtColor(tv_image_copy, cv2.COLOR_BGR2RGB)
    frames.append(tv_image_rgb)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
imageio.mimsave('./res/tv_noise.gif', frames, fps=10)