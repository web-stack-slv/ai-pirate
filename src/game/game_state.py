"""
Game state management for the Sea Battle game.
"""

import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.constants import STATE_MENU, STATE_PLACING_SHIPS, STATE_PLAYING, STATE_GAME_OVER


class GameState:
    """Manages the current state of the game."""
    
    def __init__(self):
        """Initialize the game state."""
        self.current_state = STATE_MENU
        self.player_board = None
        self.ai_board = None
        self.current_player = "player"  # "player" or "ai"
        self.game_phase = "setup"  # "setup", "playing", "finished"
    
    def set_state(self, new_state: str):
        """Change the current game state."""
        self.current_state = new_state
    
    def get_state(self) -> str:
        """Get the current game state."""
        return self.current_state
    
    def is_menu(self) -> bool:
        """Check if currently in menu state."""
        return self.current_state == STATE_MENU
    
    def is_placing_ships(self) -> bool:
        """Check if currently placing ships."""
        return self.current_state == STATE_PLACING_SHIPS
    
    def is_playing(self) -> bool:
        """Check if currently playing."""
        return self.current_state == STATE_PLAYING
    
    def is_game_over(self) -> bool:
        """Check if game is over."""
        return self.current_state == STATE_GAME_OVER
    
    def start_game(self):
        """Start the game."""
        self.current_state = STATE_PLACING_SHIPS
        self.game_phase = "setup"
    
    def start_playing(self):
        """Start the playing phase."""
        self.current_state = STATE_PLAYING
        self.game_phase = "playing"
    
    def end_game(self):
        """End the game."""
        self.current_state = STATE_GAME_OVER
        self.game_phase = "finished" 