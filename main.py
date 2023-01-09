import pygame
from pygame import Vector2

import sys, os

import win32api
import win32con
import win32gui

from Constants import *
from Logger import ErrorHandler
from Cat import Cat
from CatMisc import CatType


def main():
    pygame.init()
    window_info = pygame.display.Info()
    current_w, current_h = window_info.current_w, window_info.current_h

    if not SANDBOX_MODE:
        screen = pygame.display.set_mode((current_w, current_h), pygame.NOFRAME) # For borderless, use pygame.NOFRAME
    else:
        screen = pygame.display.set_mode((current_w, current_h)) # For borderless, use pygame.NOFRAME
    pygame.display.set_caption(WINDOW_TITLE)
    pygame.display.set_icon(pygame.image.load(ICON_FILE).convert_alpha())
    
    clock = pygame.time.Clock()

    dark_red = pygame.color.Color(240, 240, 255)

    # Getting the window handle
    hwnd = pygame.display.get_wm_info()["window"]
    # set the window to be transparent
    win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,
                           win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
    # Set window transparency color
    win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*transparent_color), 0, win32con.LWA_COLORKEY)
    # onTop(pygame.display.get_wm_info()['window'])

    start_x = start_y = 50 if SANDBOX_MODE else 0
    win32gui.SetWindowPos(pygame.display.get_wm_info()['window'], win32con.HWND_TOPMOST, start_x, start_y, 0, 0, win32con.SWP_NOSIZE)

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
            cat = Cat(screen, clock, Vector2(1200, 500), cfg_cat_type)

        screen.fill(transparent_color)  # Transparent background
        #? game functionality under here

        cat.render()

        #? - - - - - - - - - - - - - - - #
        # time and other stuff
        clock.tick(FPS)
        pygame.display.update()
        total_frames += 1
    # end window loop
    pygame.quit()
    sys.exit(0)


if __name__ == "__main__":
    # TODO: when building for release, uncomment these 2 lines, and remove the main() at the end
    # safe_main = ErrorHandler(main)
    # safe_main()
    main()
