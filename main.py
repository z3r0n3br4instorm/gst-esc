def debug(x):
   #print("\033[1m"+"[DEBUG] "+str(x)+"\033[1m")
   i = 1

debug("S E R A P H I X - S Y S T E M S | GESTURESCAPE Demo")
debug("Initializing...")
from doctest import debug
from multiprocessing.forkserver import write_signed
import cv2
import mediapipe as mp
import threading
import time
import os
def debug(x):
  #  print("\033[1m"+"[DEBUG] "+str(x)+"\033[1m")
  i = 1

global cap
cap = cv2.VideoCapture(0)
def hand_recognition():
  exit_code = 0
  debug("Hand Recognition Initializing...")
  mp_drawing = mp.solutions.drawing_utils
  mp_drawing_styles = mp.solutions.drawing_styles
  mp_hands = mp.solutions.hands

  # For webcam input:
  global cap
  with mp_hands.Hands(
      model_complexity=0,
      min_detection_confidence=0.5,
      min_tracking_confidence=0.5) as hands:
    while cap.isOpened():
      #time.sleep(0.1)
      success, image = cap.read()
      if not success:
        print("Ignoring empty camera frame.")
        # If loading a video, use 'break' instead of 'continue'.
        continue

      # To improve performance, optionally mark the image as not writeable to
      # pass by reference.
      image.flags.writeable = False
      image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
      results = hands.process(image)

      # Draw the hand annotations on the image.
      image.flags.writeable = True
      image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
      
      if results.multi_hand_landmarks:
          for hand_landmarks in results.multi_hand_landmarks:
              wrist = hand_landmarks.landmark[mp_hands.HandLandmark.WRIST]
              thumb_1 = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_CMC]
              thumb_2 = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_MCP]
              thumb_3 = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP]
              thumb_4 = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
              index_1 = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP]
              index_2 = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP]
              index_3 = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_DIP]
              index_4 = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
              middle_1 = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP]
              middle_2 = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_PIP]
              middle_3 = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_DIP]
              middle_4 = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
              ring_1 = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_MCP]
              ring_2 = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_PIP]
              ring_3 = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_DIP]
              ring_4 = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP]
              pinky_1 = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_MCP]
              pinky_2 = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_PIP]
              pinky_3 = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_DIP]
              pinky_4 = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP]
              
              # Calculate distances or angles to define thumbs up gesture
              # Example criteria: Thumb tip above the index finger tip
              index_threshold = 0.2
              # print("Index 1",index_1," index 2",index_4)
              debug("X_VALUES \n ------------------- \nIndex Tip :"+ str(index_1.x) +"\nMiddle Tip :" + str(middle_1.x)+"\nRing Tip :"+str(ring_1.x)+"\nPinky Tip :"+str(pinky_1.x))
              debug("Y_VALUES \n ------------------- \nIndex Tip :"+ str(index_1.y) +"\nMiddle Tip :" + str(middle_1.y)+"\nRing Tip :"+str(ring_1.y)+"\nPinky Tip :"+str(pinky_1.y))
              # if (((index_1.x - index_4.x) > index_threshold) or ((index_1.y - index_4.y) > index_threshold)):
              #     cv2.putText(image, "Index Widen", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
              # elif (((index_1.x - index_4.x) < index_threshold) or ((index_1.y - index_4.y) < index_threshold)):
              #     cv2.putText(image, "Index Not Widen", (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
              # elif (((index_1.x - )))
              ########WRITE TO UI#############################################################################################


              write_text_x = "X Values\n"+"Thumb_Tip "+str(thumb_4.x)+"\nIndex_Tip "+str(index_4.x)+"\nMiddle_Tip "+str(middle_4.x)+"\nRing_Tip "+str(ring_4.x)+"\nPinky_Tip "+str(pinky_4.x)+"\nWrist "+str(wrist.x)+"\nThumb_Base "+str(thumb_1.x)+"\nIndex_Base "+str(index_1.x)+"\nMiddle_Base "+str(middle_1.x)+"\nRing_Base "+str(ring_1.x)+"\nPinky_Base "+str(pinky_1.x)
              write_text_y = "Y Values\n"+"Thumb_Tip "+str(thumb_4.y)+"\nIndex_Tip "+str(index_4.y)+"\nMiddle_Tip "+str(middle_4.y)+"\nRing_Tip "+str(ring_4.y)+"\nPinky_Tip "+str(pinky_4.y)+"\nWrist "+str(wrist.y)+"\nThumb_Base "+str(thumb_1.y)+"\nIndex_Base "+str(index_1.y)+"\nMiddle_Base "+str(middle_1.y)+"\nRing_Base "+str(ring_1.y)+"\nPinky_Base "+str(pinky_1.y)
              main_write_x = open("main_x.srpx", "w")
              main_write_y = open("main_y.srpx", "w")

              main_write_x.write(write_text_x)
              main_write_y.write(write_text_y)


              ################################################################################################################

              # if ((((index_1.x + wrist.x) < (index_4.x + wrist.x)) and ((middle_1.x + wrist.x) < (middle_4.x + wrist.x))) and exit_code == 0):
              #    print("\n\n WRIST OPENED \n\n")
              # elif (exit_code == 0):
              #    os.system("brave-browser")
              #    #exit_code = 1
              mp_drawing.draw_landmarks(
                  image,
                  hand_landmarks,
                  mp_hands.HAND_CONNECTIONS,
                  mp_drawing_styles.get_default_hand_landmarks_style(),
                  mp_drawing_styles.get_default_hand_connections_style())
      
      # Flip the image horizontally for a selfie-view display.
      cv2.imshow('Hand Gestures', cv2.flip(image, 1))
      if cv2.waitKey(5) & 0xFF == 27:
        break

  cap.release()

hand_gest = threading.Thread(target=hand_recognition)

def pose_recognition():
  # Load the pose landmark model
  debug("Pose recognition Initializing")
  mp_pose = mp.solutions.pose
  pose = mp_pose.Pose()

  # Start capturing video from the webcam
  global cap  # 0 represents the default camera

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
                        (0, 13), (13, 14), (14, 15), (15, 16)]  # Left leg

          # Draw the wireframe on the frame
          for connection in connections:
              start_point = (int(landmarks[connection[0]].x * frame.shape[1]),
                            int(landmarks[connection[0]].y * frame.shape[0]))
              end_point = (int(landmarks[connection[1]].x * frame.shape[1]),
                          int(landmarks[connection[1]].y * frame.shape[0]))
              cv2.line(frame, start_point, end_point, (0, 255, 0), 2)
          left_wrist = results.pose_landmarks.landmark[mp.solutions.pose.PoseLandmark.LEFT_WRIST]
          right_wrist = results.pose_landmarks.landmark[mp.solutions.pose.PoseLandmark.RIGHT_WRIST]

      print(left_wrist)
      print(right_wrist)
      # Display the frame with pose landmarks and wireframe
      cv2.imshow("Pose Detection", frame)

      if cv2.waitKey(1) & 0xFF == ord('q'):
          break

  cap.release()
  cv2.destroyAllWindows()

pose_detection = threading.Thread(target=pose_recognition)

if __name__ == "__main__":
   debug("Ready")
   #pose_detection.start()
   hand_gest.start()
