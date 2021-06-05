import random
from game import constants
from game.actor import Actor
from game.point import Point

# TODO: Define the Food class here
class Food(Actor):
    def __init__(self):
        super().__init__()
        position = Point(random.randrange(0, constants.MAX_X), random.randrange(1, constants.MAX_Y))
        self.set_position(position)
        self._points = random.randint(1,5)
        self.set_text("h")
        #self._segments = [] probably what we will need to store each of the words... maybe
        #Maybe we just need all of the words in a list and then return that list to compare each of the words with the user's guess
        

    def get_points(self):

        return self._points
        

    def reset(self):
        
        self._points = random.randint(1,5)
        position = Point(random.randrange(1, constants.MAX_X), random.randrange(1, constants.MAX_Y))
        self.set_position(position)