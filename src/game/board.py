"""
Game board management for the Sea Battle game.
"""

from typing import List, Tuple, Optional
import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.constants import BOARD_SIZE


class Board:
    """Represents a 10x10 game board."""
    
    def __init__(self):
        """Initialize an empty board."""
        self.grid = [[None for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
        self.shots = [[False for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
        self.hits = [[False for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    
    def place_ship(self, ship, positions: List[Tuple[int, int]]) -> bool:
        """Place a ship on the board."""
        # Check if all positions are valid and empty
        for x, y in positions:
            if not self.is_valid_position(x, y) or self.grid[x][y] is not None:
                return False
        
        # Place the ship
        for x, y in positions:
            self.grid[x][y] = ship
        
        return True
    
    def is_valid_position(self, x: int, y: int) -> bool:
        """Check if a position is within the board bounds."""
        return 0 <= x < BOARD_SIZE and 0 <= y < BOARD_SIZE
    
    def get_cell(self, x: int, y: int):
        """Get the content of a cell."""
        if self.is_valid_position(x, y):
            return self.grid[x][y]
        return None
    
    def make_shot(self, x: int, y: int) -> bool:
        """Make a shot at the specified position."""
        if not self.is_valid_position(x, y) or self.shots[x][y]:
            return False
        
        self.shots[x][y] = True
        
        if self.grid[x][y] is not None:
            self.hits[x][y] = True
            return True
        
        return False
    
    def is_shot(self, x: int, y: int) -> bool:
        """Check if a position has been shot at."""
        return self.shots[x][y]
    
    def is_hit(self, x: int, y: int) -> bool:
        """Check if a position has been hit."""
        return self.hits[x][y]
    
    def is_miss(self, x: int, y: int) -> bool:
        """Check if a position was a miss."""
        return self.shots[x][y] and not self.hits[x][y]
    
    def clear(self):
        """Clear the board."""
        self.grid = [[None for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
        self.shots = [[False for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
        self.hits = [[False for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)] 