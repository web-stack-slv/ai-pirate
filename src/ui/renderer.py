"""
Rendering and drawing functions for the Sea Battle game.
"""

import pygame
import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.constants import (
    WHITE, BLACK, GRAY, LIGHT_GRAY, BLUE, LIGHT_BLUE,
    BOARD_SIZE, CELL_SIZE, BOARD_MARGIN, WINDOW_WIDTH, WINDOW_HEIGHT
)


class Renderer:
    """Handles all rendering and drawing operations."""
    
    def __init__(self, screen):
        """Initialize the renderer with a screen surface."""
        self.screen = screen
        self.font = pygame.font.Font(None, 36)
    
    def draw_text(self, text: str, position: tuple, color: tuple = WHITE):
        """Draw text on the screen."""
        text_surface = self.font.render(text, True, color)
        self.screen.blit(text_surface, position)
    
    def draw_board(self, board_offset: tuple):
        """Draw the game board grid."""
        board_x, board_y = board_offset
        
        # Draw board background
        board_rect = pygame.Rect(
            board_x - 5, 
            board_y - 5, 
            BOARD_SIZE * CELL_SIZE + 10, 
            BOARD_SIZE * CELL_SIZE + 10
        )
        pygame.draw.rect(self.screen, GRAY, board_rect)
        
        # Draw grid cells
        for x in range(BOARD_SIZE):
            for y in range(BOARD_SIZE):
                cell_rect = pygame.Rect(
                    board_x + x * CELL_SIZE,
                    board_y + y * CELL_SIZE,
                    CELL_SIZE,
                    CELL_SIZE
                )
                pygame.draw.rect(self.screen, LIGHT_GRAY, cell_rect)
                pygame.draw.rect(self.screen, BLACK, cell_rect, 1)
        
        # Draw coordinate labels
        for i in range(BOARD_SIZE):
            # Row labels (A-J)
            label = chr(65 + i)  # A, B, C, etc.
            self.draw_text(label, (board_x - 25, board_y + i * CELL_SIZE + 10))
            
            # Column labels (1-10)
            label = str(i + 1)
            self.draw_text(label, (board_x + i * CELL_SIZE + 15, board_y - 25))
    
    def draw_menu(self):
        """Draw the main menu."""
        title = "Sea Battle Game"
        title_pos = (WINDOW_WIDTH // 2 - 150, WINDOW_HEIGHT // 2 - 100)
        self.draw_text(title, title_pos, WHITE)
        
        subtitle = "Press SPACE to start"
        subtitle_pos = (WINDOW_WIDTH // 2 - 120, WINDOW_HEIGHT // 2 + 50)
        self.draw_text(subtitle, subtitle_pos, LIGHT_GRAY) 