import cv2
import numpy as np
import pygame


def play_sound(sound):
    pygame.mixer.init()
    pygame.mixer.music.load(sound)
    pygame.mixer.music.play()


def is_fire(contour, frame_width, frame_height):
    # Compute the bounding box of the contour
    x, y, w, h = cv2.boundingRect(contour)

    # Compute the aspect ratio of the bounding box
    aspect_ratio = w / float(h)

    # Compute the area of the contour
    contour_area = cv2.contourArea(contour)

    # Define threshold values for aspect ratio and area to classify as fire
    aspect_ratio_threshold = 0.8
    area_threshold = 500

    # Check if the contour meets the criteria for fire
    if aspect_ratio > aspect_ratio_threshold and contour_area > area_threshold:
        # Check if the contour is near the top portion of the frame
        if y < frame_height // 3:
            return True
    return False


if name == "main":
    sound_file = "C:\Users\user\Desktop\mixkit-classic-alarm-995.wav"
    play_sound(sound_file)

    # Load the webcam
    cap = cv2.VideoCapture(0)

    # Define the lower and upper bounds for the red color in HSV
    lower_red = np.array([0, 120, 70])
    upper_red = np.array([10, 255, 255])

    # Initialize alert flag and cooldown parameters
    alert_flag = False
    cooldown_frames = 100
    current_cooldown = cooldown_frames

    while True:
        # Read frame from webcam
        ret, frame = cap.read()
        if not ret:
            break

        # Convert frame to HSV color space
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Create a mask to isolate red color
        mask = cv2.inRange(hsv, lower_red, upper_red)

        # Apply morphological operations to reduce noise
        kernel = np.ones((5, 5), np.uint8)
        mask = cv2.dilate(mask, kernel, iterations=1)
        mask = cv2.erode(mask, kernel, iterations=1)

        # Find contours in the mask
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Iterate through contours
        for contour in contours:
            # Check if contour represents fire
            if is_fire(contour, frame.shape[1], frame.shape[0]):
                # Fire detected, play alert sound and set flag
                if not alert_flag:
                    play_sound(sound_file)
                    print("Fire Detected!")
                    alert_flag = True
                    current_cooldown = cooldown_frames

                # Draw contours on the original frame
                cv2.drawContours(frame, [contour], -1, (0, 255, 0), 2)

        # Display the frame
        cv2.imshow("Fire Detection", frame)

        # Decrease cooldown timer
        if alert_flag:
            current_cooldown -= 1
            if current_cooldown == 0:
                alert_flag = False

        # Check for 'q' key press to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and close all windows
    cap.release()
    cv2.destroyAllWindows()