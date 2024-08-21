import cv2
import numpy as np
import imageio

frames = []
landscape = cv2.imread('./res/landscape.jpg')
num_snowflakes = 300
# Initial array for store snowflakes positions
snowflakes = np.zeros((num_snowflakes, 2), dtype=np.float32)
snowflakes[:, 0] = np.random.randint(0, landscape.shape[1], num_snowflakes)
snowflakes[:, 1] = np.random.randint(0, landscape.shape[0], num_snowflakes)
for _ in range(100):  # Number of frames
    frame = landscape.copy()
    # Movement
    snowflakes[:, 1] += np.random.randint(1, 5, num_snowflakes)
    # Reset y position
    snowflakes[snowflakes[:, 1] > landscape.shape[0], 1] = 0
    # Randomly choose the position of X to prevent the snowflakes from lining up
    snowflakes[snowflakes[:, 1] == 0, 0] = np.random.randint(0, landscape.shape[1], np.sum(snowflakes[:, 1] == 0))

    # Draw snowflakes
    for x, y in snowflakes:
        cv2.circle(frame, (int(x), int(y)), 1, (255, 255, 255), -1)

    # Convert frame to RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frames.append(frame_rgb)

# Save frames
imageio.mimsave('./res/snowfall.gif', frames, fps=10)