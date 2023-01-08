import pygame
from pygame import Vector2

import sys, os

import win32api
import win32con
import win32gui

from ctypes import windll, Structure, c_long, byref

from Constants import *

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# All this magic that you see happening here is to make the window
# transparent and to stay always on top
# and creating some pygame variables for our program

class RECT(Structure):
    _fields_ = [
        ('left',    c_long),
        ('top',     c_long),
        ('right',   c_long),
        ('bottom',  c_long),
    ]
    def width(self):  return self.right  - self.left
    def height(self): return self.bottom - self.top

def onTop(window):
    SetWindowPos = windll.user32.SetWindowPos
    GetWindowRect = windll.user32.GetWindowRect
    rc = RECT()
    GetWindowRect(window, byref(rc))
    SetWindowPos(window, -1, rc.left, rc.top, 0, 0, 0x0001)


from Cat import Cat
from CatMisc import CatType


pygame.init()
window_info = pygame.display.Info()
current_w, current_h = window_info.current_w, window_info.current_h

screen = pygame.display.set_mode((current_w, current_h), pygame.NOFRAME) # For borderless, use pygame.NOFRAME
pygame.display.set_caption(WINDOW_TITLE)
clock = pygame.time.Clock()

dark_red = pygame.color.Color(240, 240, 255)

# Create layered window
hwnd = pygame.display.get_wm_info()["window"]
win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,
                       win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
# Set window transparency color
win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*transparent_color), 0, win32con.LWA_COLORKEY)
# onTop(pygame.display.get_wm_info()['window'])
win32gui.SetWindowPos(pygame.display.get_wm_info()['window'], win32con.HWND_TOPMOST, 0,0,0,0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)

# End of black magic
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

# * Game stuff here

total_frames = 0
running = True

cat = None

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

        if event.type == pygame.KEYDOWN:
            pygame.event.Event
            if event.key == pygame.K_q:
                running = False
                break
        
        if pygame.key.get_focused():
            print("FOCUSSED", total_frames)

    if not cat:
        cat = Cat(screen, clock, Vector2(1800, 700), cfg_cat_type)

    screen.fill(transparent_color)  # Transparent background
    #? game functionality under here

    cat.render()

    #? - - - - - - - - - - - - - - - #
    # time and other stuff
    clock.tick(FPS)
    pygame.display.update()
    total_frames += 1

pygame.quit()
sys.exit(0)
