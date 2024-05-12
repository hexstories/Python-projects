import cv2
import pyautogui
import numpy as np

# Screen resolution
screen_width, screen_height = pyautogui.size()

# Output video file
output_file = 'screen_recording.mp4'

# Video codec
codec = cv2.VideoWriter_fourcc(*'mp4v')

# Frames per second (FPS)
fps = 20.0

# Create VideoWriter object
out = cv2.VideoWriter(output_file, codec, fps, (screen_width, screen_height))

try:
    while True:
        # Capture screenshot
        screenshot = pyautogui.screenshot()

        # Convert screenshot to OpenCV format
        frame = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

        # Write frame to output video
        out.write(frame)

except KeyboardInterrupt:
    # Release VideoWriter object
    out.release()

    print("Screen recording stopped.")
