"""
Game constants and configuration.
"""

# Window settings
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800
WINDOW_TITLE = "Sea Battle Game"

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
LIGHT_GRAY = (200, 200, 200)
BLUE = (0, 0, 255)
LIGHT_BLUE = (173, 216, 230)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Game board settings
BOARD_SIZE = 10
CELL_SIZE = 40
BOARD_MARGIN = 50

# Game states
STATE_MENU = "menu"
STATE_PLACING_SHIPS = "placing_ships"
STATE_PLAYING = "playing"
STATE_GAME_OVER = "game_over"

# Ship types and sizes
SHIPS = {
    "carrier": 5,
    "battleship": 4,
    "cruiser": 3,
    "submarine": 3,
    "destroyer": 2
} 