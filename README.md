# Sea Battle Game

A classic Sea Battle (Battleship) game built with Python and Pygame.

## Features (Planned)
- Classic 10x10 grid gameplay
- Single player vs AI
- Multiplayer support
- Ship placement and targeting
- Visual feedback and animations
- Sound effects

## Project Structure
```
ai-pirate/
├── src/
│   ├── __init__.py
│   ├── main.py              # Main game entry point
│   ├── game/
│   │   ├── __init__.py
│   │   ├── game_state.py    # Game state management
│   │   ├── board.py         # Game board logic
│   │   └── ships.py         # Ship classes and logic
│   ├── ui/
│   │   ├── __init__.py
│   │   ├── window.py        # Window management
│   │   ├── renderer.py      # Drawing and rendering
│   │   └── input_handler.py # Input processing
│   └── utils/
│       ├── __init__.py
│       ├── constants.py     # Game constants
│       └── helpers.py       # Utility functions
├── assets/
│   ├── images/              # Game images and sprites
│   ├── sounds/              # Sound effects
│   └── fonts/               # Custom fonts
├── tests/
│   └── __init__.py
├── requirements.txt
└── README.md
```

## Setup Instructions

1. **Create virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the game:**
   ```bash
   python src/main.py
   ```

## Development

This project follows clean architecture principles:
- **Separation of Concerns**: Game logic, UI, and utilities are separated
- **Dependency Inversion**: High-level modules don't depend on low-level modules
- **Single Responsibility**: Each class has one reason to change
- **Open/Closed**: Open for extension, closed for modification

## Current Status
- ✅ Project structure setup
- ✅ Basic pygame window
- 🔄 Game board implementation
- 🔄 Ship placement logic
- 🔄 Game mechanics
- 🔄 UI improvements