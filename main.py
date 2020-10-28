import pyautogui
import time


#  Select all(X:276, Y: 221) Delete(X:424, Y:221)

try: 
  while True:
    pyautogui.click(x=276, y=221)
    pyautogui.click(x=424, y=221)
    time.sleep(2)
    

    # FOR COORDINATES
    # x,y = pyautogui.position()
    # position_str = "X: " + str(x).rjust(4) + " Y: " + str(y).rjust(4)
    # print(position_str, flush=True)
    # # print("\b" * len(position_str), end="", flush=True)
    # time.sleep(1)

except KeyboardInterrupt:
  print("\n")