import pygame
from pygame.locals import *
import os

class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Shape:
    SQUARE = 'square'
    CIRCLE = 'circle'
    POLYGON = 'polygon'

class ESPAGL:
    def __init__(self):
        pygame.init()
        self.screen = None
        self.clock = pygame.time.Clock()  # Clock to control frame rate
        self.inputs = {}  # Dictionary to map input names to pygame key constants

    def start_game(self, window_name, size):
        # Initialize Pygame screen
        self.screen = pygame.display.set_mode((size.x, size.y))
        pygame.display.set_caption(window_name)

        self.clock.tick(60)

        # Determine the directory of the current script
        script_dir = os.path.dirname(os.path.abspath(__file__))

        # Load the icon file relative to the script directory
        icon_path = os.path.join(script_dir, '..', 'graphics', 'icon.ico')
        icon_path = os.path.abspath(icon_path)  # Get absolute path to the icon file
        icon = pygame.image.load(icon_path)

        # Set the window icon
        pygame.display.set_icon(icon)


    def update_screen(self):
        pygame.display.update()

    def draw_shape(self, shape_type, position, color, *args):
        if shape_type == Shape.SQUARE:
            pygame.draw.rect(self.screen, color, (position.x, position.y, 100, 100))  # Draw a square (100x100)
        elif shape_type == Shape.CIRCLE:
            pygame.draw.circle(self.screen, color, (position.x, position.y), 50)  # Draw a circle (radius 50)

    def render_sprite(self, sprite_file_location, sprite_pos_x=0, sprite_pos_y=0, sprite_scale_x=2, sprite_scale_y=2):
        img = pygame.image.load(sprite_file_location)
        img = pygame.transform.scale(img, (sprite_scale_x, sprite_scale_y))
        self.screen.blit(img, (sprite_pos_x, sprite_pos_y))

    def write_text(self, text, position, color=(255, 255, 255)):
        font = pygame.font.Font(None, 36)  # Load a default font with size 36
        text_surface = font.render(text, True, color)  # Render the text onto a surface
        text_rect = text_surface.get_rect(center=(position.x, position.y))  # Get the rectangle containing the text
        self.screen.blit(text_surface, text_rect)  # Draw the text surface onto the screen

    def close_game(self):
        pygame.quit()

    def add_input(self, name, keys):
        # Map the input name to a list of pygame key constants
        self.inputs[name] = [getattr(pygame, key) for key in keys]

    def get_input(self):
        keys = pygame.key.get_pressed()
        for name, key_list in self.inputs.items():
            if any(keys[key] for key in key_list):
                return name
        return None