"""Example game showing a circle moving on screen."""
import pygame

from cs110 import expect, summarize
from game import Game
from player import Player
from keys import pressed_keys, directions

    
# TODO: draw your List of Food
def draw(game: Game, player: Player):
    """
    Draws the player and game on the screen.
    
    Note that because this function has only side-effects, it would take a
    simulation to test. We can do that, but for this class, it's a bit much.
    Therefore, we don't have any tests for this.
    """
    game.screen.fill(game.background)
    pygame.draw.circle(
        game.screen,
        player.color,
        pygame.Vector2(player.x, player.y),
        player.size
    )
    pygame.display.flip()
    

def main():
    """
    Run the main game loop.
    
    Note: again, because this is a function that only has side effects, there's
    not really a clean way to test this. Main loops usually follow a command
    pattern like this where they coordinate functions from different files.
    """
    
    # Define the Game state
    game = Game(
        screen     = pygame.display.set_mode((1280, 720)),
        clock      = pygame.time.Clock(),
        background = "purple",
        fps        = 60,
        running    = True,
        deltaT     = 0,
        keymap     = {
                        "w": "UP",
                        "s": "DOWN",
                        "a": "LEFT",
                        "d": "RIGHT"
        },
    )

    # Define the player
    player = Player(
              x     = game.screen.get_width() / 2,
              y     = game.screen.get_height() / 2,
              size  = 40,
              speed = 300,
              color = "red"
              # TODO: add food count
    )
    
    # Initialze pygame
    pygame.init()
    
    # Run forever in a loop until quit
    while game.running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.running = False
                pygame.quit()

        # Move the game clock forward
        game.tick()

        # Get pressed keys and directions
        pressed = pressed_keys(pygame.key.get_pressed())
        dirs = directions(game.keymap, pressed)
        
        # Move the player
        player.move(game.deltaT, dirs)

        # TODO: determine whether your food has been consumed
        # TODO: change the player size based on food count
        # TODO: draw the food

        # Draw the game
        # TODO: extend to draw Food 
        draw(game, player)

# Run the main function
if __name__ == "__main__":
    main()
