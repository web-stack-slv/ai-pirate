"""
Window management for the Sea Battle game.
"""

import pygame
import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.constants import WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE


class GameWindow:
    """Manages the main game window and display."""
    
    def __init__(self):
        """Initialize the game window."""
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption(WINDOW_TITLE)
        self.clock = pygame.time.Clock()
        self.running = False
    
    def start(self):
        """Start the game window."""
        self.running = True
    
    def stop(self):
        """Stop the game window."""
        self.running = False
        pygame.quit()
    
    def clear(self):
        """Clear the screen."""
        self.screen.fill((0, 0, 0))  # Black background
    
    def update(self):
        """Update the display."""
        pygame.display.flip()
    
    def get_screen(self):
        """Get the pygame screen surface."""
        return self.screen
    
    def get_clock(self):
        """Get the pygame clock."""
        return self.clock
    
    def is_running(self):
        """Check if the window is running."""
        return self.running 