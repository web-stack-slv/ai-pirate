"""
Main entry point for the Sea Battle game.
"""

import pygame
import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from ui.window import GameWindow
from ui.renderer import Renderer
from ui.input_handler import InputHandler
from game.game_state import GameState
from utils.constants import WINDOW_WIDTH, WINDOW_HEIGHT, BOARD_MARGIN, CELL_SIZE, BOARD_SIZE


class SeaBattleGame:
    """Main game class that orchestrates all components."""
    
    def __init__(self):
        """Initialize the game."""
        self.window = GameWindow()
        self.renderer = Renderer(self.window.get_screen())
        self.input_handler = InputHandler()
        self.game_state = GameState()
        self.clock = self.window.get_clock()
        
        # Calculate board positions
        self.player_board_pos = (BOARD_MARGIN, WINDOW_HEIGHT // 2 - (BOARD_SIZE * CELL_SIZE) // 2)
        self.ai_board_pos = (WINDOW_WIDTH - BOARD_MARGIN - BOARD_SIZE * CELL_SIZE, 
                           WINDOW_HEIGHT // 2 - (BOARD_SIZE * CELL_SIZE) // 2)
    
    def run(self):
        """Main game loop."""
        self.window.start()
        
        while self.window.is_running():
            # Handle events
            events = self.input_handler.process_events()
            for event in events:
                if event.type == pygame.QUIT:
                    self.window.stop()
                    return
            
            # Handle input
            self.handle_input()
            
            # Update game state
            self.update()
            
            # Render
            self.render()
            
            # Cap the frame rate
            self.clock.tick(60)
    
    def handle_input(self):
        """Handle user input."""
        if self.game_state.is_menu():
            if self.input_handler.is_key_pressed(pygame.K_SPACE):
                self.game_state.start_game()
        
        elif self.game_state.is_placing_ships():
            # For now, just start playing when any key is pressed
            if self.input_handler.is_key_pressed(pygame.K_RETURN):
                self.game_state.start_playing()
        
        elif self.game_state.is_playing():
            # Handle mouse clicks for shooting
            if self.input_handler.is_mouse_clicked():
                mouse_pos = self.input_handler.get_mouse_position()
                # TODO: Implement shooting logic
                pass
    
    def update(self):
        """Update game logic."""
        # TODO: Add game logic updates
        pass
    
    def render(self):
        """Render the game."""
        # Clear the screen
        self.window.clear()
        
        if self.game_state.is_menu():
            self.renderer.draw_menu()
        
        elif self.game_state.is_placing_ships():
            self.render_placement_screen()
        
        elif self.game_state.is_playing():
            self.render_game_screen()
        
        # Update the display
        self.window.update()
    
    def render_placement_screen(self):
        """Render the ship placement screen."""
        # Draw title
        title = "Place Your Ships"
        title_pos = (WINDOW_WIDTH // 2 - 100, 50)
        self.renderer.draw_text(title, title_pos)
        
        # Draw player board
        self.renderer.draw_board(self.player_board_pos)
        
        # Draw instructions
        instructions = "Press ENTER to start game"
        inst_pos = (WINDOW_WIDTH // 2 - 120, WINDOW_HEIGHT - 50)
        self.renderer.draw_text(instructions, inst_pos)
    
    def render_game_screen(self):
        """Render the main game screen."""
        # Draw title
        title = "Sea Battle"
        title_pos = (WINDOW_WIDTH // 2 - 60, 20)
        self.renderer.draw_text(title, title_pos)
        
        # Draw player board
        self.renderer.draw_board(self.player_board_pos)
        
        # Draw AI board
        self.renderer.draw_board(self.ai_board_pos)
        
        # Draw labels
        player_label = "Your Board"
        player_label_pos = (self.player_board_pos[0], self.player_board_pos[1] - 30)
        self.renderer.draw_text(player_label, player_label_pos)
        
        ai_label = "Enemy Board"
        ai_label_pos = (self.ai_board_pos[0], self.ai_board_pos[1] - 30)
        self.renderer.draw_text(ai_label, ai_label_pos)


def main():
    """Main function to start the game."""
    try:
        game = SeaBattleGame()
        game.run()
    except Exception as e:
        print(f"Error running game: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main() 