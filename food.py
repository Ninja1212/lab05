"""Manages Food state."""
from typing import List
from dataclasses import dataclass
from player import Player
from typing_extensions import Self

@dataclass
class Food:
    """TODO: complete the Food class with appropriate variables and methods."""
    x: float
    y: float
    size: float

    # TODO: create a method to move a single Food
    
    
    def move(self, x: float, y: float) -> Self:
        """
        Purpose: moves a Food's position by x and y
        Example:
            food.x -> food.x + x
            food.y -> food.x + y
        """
        self.x = self.x + x
        self.y = self.y + y
        return self
    
    
    
    def hit(self, player: Player) -> bool:
        """
        TODO: Design a function that takes this Food a Player and determines
        whether they are touching.
        
        Use the HtDF formula and put your tests in tests.py.
        """
        return False # stub

@dataclass
class FoodList:
    """TODO: complete the FoodList class with appropriate variables and methods."""
    food: List[Food]

    # TODO: create a method to populate the food. 
    # Consider using https://docs.python.org/3/library/random.html

    # TODO: create a method to move all of the FoodList.
    
    # TODO: create a method to remove a Food




 
 