import pygame
from espagl import ESPAGL, Vector2

# Initialize ESPAGL
espagl = ESPAGL()

# Start the game window
espagl.start_game("Hairmess Engine Test Prototype", Vector2(800, 400))

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # Exit the loop if the user wants to close the window

    # Update game state
    # (Add any game logic or updates here)

    # Draw "Hello World!" text at the center of the screen
    espagl.write_text("Hello World!", Vector2(300, 180), (0, 255, 0))

    # Update the screen
    espagl.update_screen()

# Close the game
espagl.close_game()
