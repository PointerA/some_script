from ctypes import windll
import win32api
import win32con
import time

width = windll.user32.GetSystemMetrics(0)
height = windll.user32.GetSystemMetrics(1)
print(width, height)
t = 0
while 1:
    windll.user32.SetCursorPos(640,150)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 640,150)
    time.sleep(0.05)    
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 640,150)
    time.sleep(10)
    t = t+1
    if t%100 == 99:
        windll.user32.SetCursorPos(170,150)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 170,150)
        time.sleep(0.05)    
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 170,150)
