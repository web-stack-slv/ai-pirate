"""
Ship classes for the Sea Battle game.
"""

from typing import List, Tuple
import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.constants import SHIPS


class Ship:
    """Base ship class."""
    
    def __init__(self, ship_type: str, size: int):
        """Initialize a ship."""
        self.ship_type = ship_type
        self.size = size
        self.positions = []
        self.hits = set()
        self.orientation = "horizontal"  # "horizontal" or "vertical"
    
    def place(self, positions: List[Tuple[int, int]], orientation: str):
        """Place the ship on the board."""
        self.positions = positions
        self.orientation = orientation
    
    def hit(self, position: Tuple[int, int]) -> bool:
        """Record a hit on the ship."""
        if position in self.positions:
            self.hits.add(position)
            return True
        return False
    
    def is_sunk(self) -> bool:
        """Check if the ship is sunk."""
        return len(self.hits) == len(self.positions)
    
    def get_hit_count(self) -> int:
        """Get the number of hits on the ship."""
        return len(self.hits)


class Carrier(Ship):
    """Carrier ship (size 5)."""
    
    def __init__(self):
        super().__init__("carrier", 5)


class Battleship(Ship):
    """Battleship (size 4)."""
    
    def __init__(self):
        super().__init__("battleship", 4)


class Cruiser(Ship):
    """Cruiser ship (size 3)."""
    
    def __init__(self):
        super().__init__("cruiser", 3)


class Submarine(Ship):
    """Submarine (size 3)."""
    
    def __init__(self):
        super().__init__("submarine", 3)


class Destroyer(Ship):
    """Destroyer ship (size 2)."""
    
    def __init__(self):
        super().__init__("destroyer", 2)


def create_ship(ship_type: str) -> Ship:
    """Factory function to create ships by type."""
    ship_classes = {
        "carrier": Carrier,
        "battleship": Battleship,
        "cruiser": Cruiser,
        "submarine": Submarine,
        "destroyer": Destroyer
    }
    
    if ship_type in ship_classes:
        return ship_classes[ship_type]()
    
    raise ValueError(f"Unknown ship type: {ship_type}") 