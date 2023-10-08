from ctypes import windll
import win32api
import win32con
import time

width = windll.user32.GetSystemMetrics(0)
height = windll.user32.GetSystemMetrics(1)
print(width, height)
while 1:
    #windll.user32.SetCursorPos(640,150)
    '''
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 640,150)
    time.sleep(0.05)    
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 640,150)
    '''
    win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL,  int(width/2),int(height/2), 100, 0)
    time.sleep(1)
    