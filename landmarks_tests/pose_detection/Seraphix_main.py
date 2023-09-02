import os
import sys
import mediapipe as mp
import cv2

def debug(x):
    print("[DEBUGGER] ",x)

def pose_detection():
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

def hand_gesture_detection():
    def detect_gesture(frame, pose):
        if pose is None:
            return "No gesture"
        left_wrist = pose.pose_landmarks.landmark[mp.solutions.pose.PoseLandmark.LEFT_WRIST]
        right_wrist = pose.pose_landmarks.landmark[mp.solutions.pose.PoseLandmark.RIGHT_WRIST]
        left_wrist_y = left_wrist.y * frame.shape[0]
        right_wrist_y = right_wrist.y * frame.shape[0]

        # Define a threshold for detecting the raised hand
        threshold = 0.9

        # Check if the wrists are above the threshold (raised hand)
        if left_wrist_y < threshold * frame.shape[0] or right_wrist_y < threshold * frame.shape[0]:
            return "Raised hand"
        
        return "No gesture"

    def main():
        cap = cv2.VideoCapture(0)

        mp_pose = mp.solutions.pose
        pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            # Convert the frame to RGB (Mediapipe requires RGB images)
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Process the frame using Mediapipe Pose model
            results = pose.process(frame_rgb)

            # Detect the gesture
            gesture = detect_gesture(frame, results)

            # Display the gesture on the frame
            cv2.putText(frame, gesture, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

            # Show the frame
            cv2.imshow('Gesture Recognition', frame)

            if cv2.waitKey(10) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    printf(" S E R A P H I X - S Y S T E M S ")
    debug("INITIALIZING GESTURE-ESCAPE...")