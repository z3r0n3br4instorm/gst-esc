import os
def install_start():
  print("Seraphics Systems : Dependencies Installer...")
  os.system("pip install mediapipe")
  os.system("pip install pyqt5")
  os.system("pip install cv2")
  os.system("pip install doctest")

if __name__ == "__main__":
  install_start()
