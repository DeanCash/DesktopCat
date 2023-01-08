import time
import win32gui
time.sleep(2)
hwnd = win32gui.FindWindow(None, "Downloads")

# Get the current size and position of the window


# Set the new position of the window, keeping the same size
xmove, ymove = 0.2, 0.1
for i in range(1000):
    x1, y1, x2, y2 = win32gui.GetWindowRect(hwnd)
    width = x2 - x1
    height = y2 - y1
    win32gui.MoveWindow(hwnd, x1 - 2, y1 - 1, width, height, True)
    time.sleep(0.02)
x1, y1, x2, y2 = win32gui.GetWindowRect(hwnd)
print(x1, y1)
