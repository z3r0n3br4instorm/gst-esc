import cv2
import mediapipe as mp

# Initialize the holistic model
holistic = mp.solutions.holistic.Holistic(model_path="/home/zerone/DSUploads/pose_landmarker_heavy.task")

# Capture the video feed
cap = cv2.VideoCapture(0)

while True:
    # Capture the current frame
    ret, frame = cap.read()

    # Run the holistic model on the frame
    results = holistic.process(frame)

    # Draw the pose landmarks on the frame
    if results.pose_landmarks:
        for landmark in results.pose_landmarks:
            cv2.circle(frame, landmark.point, 5, (0, 255, 0), thickness=2)

    # Display the frame
    cv2.imshow("Pose Detection", frame)

    # Press ESC to quit
    if cv2.waitKey(1) == 27:
        break

# Release the capture
cap.release()
cv2.destroyAllWindows()
