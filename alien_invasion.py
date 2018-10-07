import sys

import pygame
from settings import Settings

def run_game():
  # Initialize game and create a screen object.
  pygame.init()
  ai_settingss = Settings()
  screen = pygame.display.set_mode((ai_settingss.screen_width, ai_settingss.screen_height))
  pygame.display.set_caption("Alien Invasion")
  # Set the background color.
  bg_color = ai_settingss.bg_color
  

  # Start the main loop for the game.
  while True:
    # Watch for keyboard and mouse events.
    # (event-loop)
    for event in pygame.event.get(): 
      if event.type == pygame.QUIT:
        sys.exit()
    
    # Redraw the screen during each pass through the loop.
    screen.fill(bg_color)

    # Make the most recently drawn screen visible.
    pygame.display.flip()

run_game()