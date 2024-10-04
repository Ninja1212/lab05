"""Test suite for game."""
import pygame
from cs110 import expect, summarize
import game
import player
import keys

#------------------------------------------------------------------------------#
# Setup: Run these before all tests.
#------------------------------------------------------------------------------#
test_game = game.Game(
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

test_player_1 = player.Player(x=100, y=100, size=10, speed=10, color="red")
test_player_2 = player.Player(x=100, y=100, size=10, speed=10, color="red")
test_player_3 = player.Player(x=100, y=100, size=10, speed=10, color="red")
test_player_4 = player.Player(x=100, y=100, size=10, speed=10, color="red")

test_player_UP = player.Player(x=100, y=  0, size=10, speed=10, color="red")
test_player_DN = player.Player(x=100, y=200, size=10, speed=10, color="red")
test_player_LT = player.Player(x=200, y=100, size=10, speed=10, color="red")
test_player_RT = player.Player(x=  0, y=100, size=10, speed=10, color="red")


#------------------------------------------------------------------------------#
# Test player.move
#------------------------------------------------------------------------------#
expect(test_player_1.move(10, ["UP"]),    test_player_UP)
expect(test_player_2.move(10, ["DOWN"]),  test_player_DN)
expect(test_player_3.move(10, ["RIGHT"]), test_player_LT)
expect(test_player_4.move(10, ["LEFT"]),  test_player_RT)


#------------------------------------------------------------------------------#
# Test player.directions
#------------------------------------------------------------------------------#
expect(keys.directions(test_game.keymap, ["w"]),      ["UP"])
expect(keys.directions(test_game.keymap, ["s"]),      ["DOWN"])
expect(keys.directions(test_game.keymap, ["a"]),      ["LEFT"])
expect(keys.directions(test_game.keymap, ["d"]),      ["RIGHT"])
expect(keys.directions(test_game.keymap, ["w", "a"]), ["UP", "LEFT"])
expect(keys.directions(test_game.keymap, ["w", "d"]), ["UP", "RIGHT"])
expect(keys.directions(test_game.keymap, ["s", "a"]), ["DOWN", "LEFT"])
expect(keys.directions(test_game.keymap, ["s", "d"]), ["DOWN", "RIGHT"])


#------------------------------------------------------------------------------#
# Test keys.pressed_keys
#------------------------------------------------------------------------------#
expect(keys.pressed_keys((False,) * 8   + (True,) * 2), ['backspace', 'tab'])
expect(keys.pressed_keys((False,) * 97  + (True,) * 3), ['a', 'b', 'c'])
expect(keys.pressed_keys((False,) * 100 + (True,) * 1), ['d'])


#------------------------------------------------------------------------------#
# Test game.tick
#------------------------------------------------------------------------------#
expect(test_game.tick(), test_game)


# TODO: add tests for moving one Food
food = Food(90, 90)
expect(food.move(10, 10), Food(100, 100))

# TODO: add tests for populating FoodList
# TODO: add tests for moving the player with the mouse
# TODO: add tests for hitting Food
# TODO: add tests for consuming Food in the Player
# TODO: add tests for removing a food from FoodList
# TODO: add tests for changing the size of Player based on food count

#------------------------------------------------------------------------------#
# Summarize the tests
#------------------------------------------------------------------------------#
summarize()