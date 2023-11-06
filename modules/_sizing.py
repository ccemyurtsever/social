import pyautogui
import time

width, height = pyautogui.size()

try:
  print(f"Main Screen Resolution: {width}x{height}")
  xdef , ydef = width / 1.65  , height / 1.65
  xdefmov , ydefmove = width / 5  , height / 7
    
except ZeroDivisionError:
  print("No resolution found.")
  breakpoint()
except ValueError:
  print("Could not create a screen with this resolution.")
  breakpoint()
except:
  print("An unknown problem has occurred.")
  breakpoint()