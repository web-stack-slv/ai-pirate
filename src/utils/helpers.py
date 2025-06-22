"""
Utility functions for the Sea Battle game.
"""

from typing import Tuple, List
import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.constants import BOARD_SIZE


def is_valid_coordinate(x: int, y: int) -> bool:
    """Check if coordinates are within the game board bounds."""
    return 0 <= x < BOARD_SIZE and 0 <= y < BOARD_SIZE


def get_cell_coordinates(mouse_pos: Tuple[int, int], board_offset: Tuple[int, int]) -> Tuple[int, int]:
    """Convert mouse position to board cell coordinates."""
    from .constants import CELL_SIZE
    
    x, y = mouse_pos
    board_x, board_y = board_offset
    
    cell_x = (x - board_x) // CELL_SIZE
    cell_y = (y - board_y) // CELL_SIZE
    
    return cell_x, cell_y


def get_cell_rect(cell_x: int, cell_y: int, board_offset: Tuple[int, int]) -> Tuple[int, int, int, int]:
    """Get the rectangle coordinates for a cell."""
    from .constants import CELL_SIZE
    
    board_x, board_y = board_offset
    x = board_x + cell_x * CELL_SIZE
    y = board_y + cell_y * CELL_SIZE
    
    return (x, y, CELL_SIZE, CELL_SIZE)


def generate_ship_positions(ship_size: int, orientation: str, start_x: int, start_y: int) -> List[Tuple[int, int]]:
    """Generate all positions a ship would occupy."""
    positions = []
    
    if orientation == "horizontal":
        for i in range(ship_size):
            positions.append((start_x + i, start_y))
    else:  # vertical
        for i in range(ship_size):
            positions.append((start_x, start_y + i))
    
    return positions 