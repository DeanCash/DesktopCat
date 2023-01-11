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
        screen = pygame.display.set_mode((current_w, current_h - 50), pygame.NOFRAME) # For borderless, use pygame.NOFRAME
    else:
        screen = pygame.display.set_mode((current_w, current_h - 50)) # For borderless, use pygame.NOFRAME
    pygame.display.set_caption(WINDOW_TITLE)
    pygame.display.set_icon(pygame.image.load(ICON_FILE).convert_alpha())

    default_font = pygame.font.Font(DEFAULT_FONT_FILE, DEFAULT_FONT_SIZE)
    clock = pygame.time.Clock()

    dark_red = pygame.color.Color(240, 240, 255)

    # Getting the window handle
    hwnd = pygame.display.get_wm_info()['window']
    # allows the window to be drawn using alpha blending
    win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,
                           win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
    # Set window transparency color
    win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*transparent_color), 0, win32con.LWA_COLORKEY)

    start_x = start_y = 50 if SANDBOX_MODE else 0
    win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, start_x, start_y, 0, 0, win32con.SWP_NOSIZE)

    # * Game stuff here

    total_frames = 0
    running = True
    ran_once = False

    cat = None
    fps_text = default_font.render(f"FPS xx", False, DEFAULT_COLOR, None)
    fps_text_width = fps_text.get_width()

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
                # when window has focus
                pass

        if not cat:
            cat = Cat(screen, clock, Vector2(int(current_w * 0.75), int(current_h * 0.60)), cfg_cat_type)

        screen.fill(transparent_color)  # Transparent background
        #? game functionality under here

        cat.render()

        #? - - - - - - - - - - - - - - - #
        # fps counter, for if SANDBOX_MODE is enabled
        if SANDBOX_MODE:
            # refresh the fps counter 4 times a frame instead of 60
            if (total_frames % 15 == 0) or (not ran_once):
                get_time = clock.get_time()
                fps_text = default_font.render(f"FPS {int(1000 / (get_time if get_time != 0 else 1))}", False, DEFAULT_COLOR, None)
                ran_once = True
            # using the walrus operator to save an extra function call to get_height
            screen.blit(fps_text, (screen.get_width() - (fps_text_width + (fps_text_height := fps_text.get_height())), fps_text_height))

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
