"""
Input handling for the Sea Battle game.
"""

import pygame
from typing import List, Tuple


class InputHandler:
    """Handles all user input and events."""
    
    def __init__(self):
        """Initialize the input handler."""
        self.keys_pressed = set()
        self.mouse_pos = (0, 0)
        self.mouse_clicked = False
    
    def process_events(self) -> List[pygame.event.Event]:
        """Process all pygame events and return them."""
        events = []
        
        for event in pygame.event.get():
            events.append(event)
            
            if event.type == pygame.QUIT:
                return events
            
            elif event.type == pygame.KEYDOWN:
                self.keys_pressed.add(event.key)
            
            elif event.type == pygame.KEYUP:
                self.keys_pressed.discard(event.key)
            
            elif event.type == pygame.MOUSEMOTION:
                self.mouse_pos = event.pos
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left click
                    self.mouse_clicked = True
        
        return events
    
    def is_key_pressed(self, key: int) -> bool:
        """Check if a specific key is currently pressed."""
        return key in self.keys_pressed
    
    def get_mouse_position(self) -> Tuple[int, int]:
        """Get the current mouse position."""
        return self.mouse_pos
    
    def is_mouse_clicked(self) -> bool:
        """Check if mouse was clicked and reset the flag."""
        if self.mouse_clicked:
            self.mouse_clicked = False
            return True
        return False
    
    def clear_keys(self):
        """Clear all pressed keys."""
        self.keys_pressed.clear() 