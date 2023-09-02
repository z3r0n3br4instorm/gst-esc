import mediapipe as mp
import cv2

# Load the pose landmark model
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

# Start capturing video from the webcam
cap = cv2.VideoCapture(0)  # 0 represents the default camera

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detect pose landmarks
    results = pose.process(image_rgb)

    if results.pose_landmarks:
        # Define indices of landmarks representing body parts
        landmarks = results.pose_landmarks.landmark

        # Define connections for the wireframe
        connections = [(0, 1), (1, 2), (2, 3), (3, 4),  # Right arm
                       (0, 5), (5, 6), (6, 7), (7, 8),  # Left arm
                       (0, 9), (9, 10), (10, 11), (11, 12),  # Right leg
                       (0, 13), (13, 14), (14, 15), (15, 16),  # Left leg
                       (0, 17)]  # Wrist

        # Draw the wireframe on the frame
        for connection in connections:
            start_point = (int(landmarks[connection[0]].x * frame.shape[1]),
                           int(landmarks[connection[0]].y * frame.shape[0]))
            end_point = (int(landmarks[connection[1]].x * frame.shape[1]),
                         int(landmarks[connection[1]].y * frame.shape[0]))
            cv2.line(frame, start_point, end_point, (0, 255, 0), 2)

    # Display the frame with pose landmarks and wireframe
    cv2.imshow("Pose Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
