import time
import pyautogui

def get_mouse_position():
   
    time.sleep(5)
    
    
    x, y = pyautogui.position()
    
    # Print the coordinates
    print(f"Mouse position: ({x}, {y})")


get_mouse_position()    
    
 