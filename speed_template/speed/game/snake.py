from game import constants
from game.actor import Actor
from game.point import Point

class Snake(Actor):
    """A limbless reptile. The responsibility of Snake is keep track of its segments. It contains methods for moving and growing among others.

    Stereotype:
        Structurer, Information Holder

    Attributes:
        _body (List): The snake's body (a list of Actor instances)
    """
    def __init__(self):
        """The class constructor. Invokes the superclass constructor, initializes points to zero, sets the position and updates the text.
        
        Args:
            self (Snake): an instance of Snake.
        """
        super().__init__()
        self._letters = ""
        position = Point(1, constants.MAX_Y -1)
        self.set_position(position)
        self.set_text(f"Score: {self._letters}")
    
    def get_points(self, points):
        """Adds the given points to the running total and updates the text.
        
        Args:
            self (Snake): An instance of Snake.
            points (integer): The points to add.
        """
        self._letters += points
        self.set_text(f"Buffer: {self._letters}")

    def get_word(self): # may need to delete this
        """returns the current wriiten word from the user.

        Args:
            self (Snake): An instance of Snake."""
        
        return self._letters

    def reset(self):
        """resets the word that the user has typed so it is now empty

        Args:
            self (Snake): An instance of Snake."""
        
        self._letters = ""
