import pygame
import os

pygame.init()

fonts_dir = "assets/fonts"
cat_font = "CatFont.otf"

to_text = "Meow!"

catfont = pygame.font.Font(os.path.join(fonts_dir, cat_font), 84)

# Set the window size
window_size = (640, 480)

# Create the window
screen = pygame.display.set_mode(window_size)

# Set the window title
pygame.display.set_caption("My Pygame Program")



# Run the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with white
    screen.fill((255, 255, 255))

    # Render some text
    text = catfont.render(to_text, 1, (0, 0, 0))
    screen.blit(text, (10, 10))

    # Update the display
    pygame.display.flip()

# Shut down Pygame
pygame.quit()
