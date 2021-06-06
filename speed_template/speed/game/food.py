import random
from game import constants
from game.actor import Actor
from game.point import Point

# TODO: Define the Food class here
class Food(Actor):
    def __init__(self):
        super().__init__()
        #position = Point(random.randrange(0, constants.MAX_X), 0)
        #self.set_position(position)
        #self._points = random.randint(1,5)
        #self.set_text("h")
        #self._segments = [] probably what we will need to store each of the words... maybe
        #Maybe we just need all of the words in a list and then return that list to compare each of the words with the user's guess
        all_quotes = open("speed_template\speed\game\words.txt", "r")
        self._list_quotes = all_quotes.readlines()

        self._segments = []

        self._points = 0
        self._lists = []
        self._dic_words = {}
        self._direction = Point(0, 1)
        self._prepare()


    def get_all(self):
        """Gets all the snake's segments.
        
        Args:
            self (Snake): An instance of snake.

        Returns:
            list: The snake's segments.
        """
        return self._segments
        

    def get_points(self):

        return self._points
        
    def move_word(self):
        #val = self._lists[1]

        count = len(self._segments) - 1
        for n in range(count, -1, -1):
            segment = self._segments[n]
            if n > 0:
                leader = self._segments[n - 1]
                velocity = leader.get_velocity()
                segment.set_velocity(velocity)
            else:
                segment.set_velocity(self._direction)
            segment.move_next()
        """
        self.set_velocity(self._direction)
        self.move_next()
        """

    def reset(self):

        self._lists[1] = random.choice(self._list_quotes)
        self._lists[1] = self._lists[1][:-1]
        self.set_text(self._lists[1])

        self._points = len(self._lists[1])
        position = Point(random.randrange(1, constants.MAX_X), 1)
        self.set_position(position)


######################################################################


    def _add_segment(self, text, position, velocity):
        """Adds a new segment to the snake using the given text, position and velocity.

        Args:
            self (Snake): An instance of snake.
            text (string): The segment's text.
            position (Point): The segment's position.
            velocity (Point): The segment's velocity.
        """
        segment = Actor()
        segment.set_text(text)
        segment.set_position(position)
        segment.set_velocity(velocity)
        self._segments.append(segment)


######################################################################


    def _prepare(self):
        """all_quotes = open("speed_template\speed\game\words.txt", "r")
        list_quotes = all_quotes.readlines()"""

        for n in range(0, 5):
            text = random.choice(self._list_quotes)
            position2 = Point(random.randrange(0, constants.MAX_X), 1)
            velocity = self._direction
            self._add_segment(text, position2, velocity)


        """for x in range (0, 5):
            #Chooses a random quote from the list and then breaks the quote up into a list that is stored into val
            self.lists.append(random.choice(list_quotes))
            self.lists[x] = self.lists[x][:-1]"""

        """
        for x in range (0, 5):
            #Chooses a random quote from the list and then breaks the quote up into a list that is stored into val
            word = random.choice(self._list_quotes)
            word = word[:-1]
            points = len(word)
            position = Point(random.randrange(0, constants.MAX_X), 1)
            self._dic_words[word] = [points, position]
            self._lists.append(word)
            """

        """
        for x in range (0, 5):
            self.set_text(self._lists[x])
            self.set_position(self._dic_words[self._lists[x]][1])
            self._points = self._dic_words[self._lists[x]][0]
        """
        """
        for n in range(0, 5):
            text = self._lists[n]
            position2 = self._dic_words[self._lists[n]]
            velocity = self._direction
            self._add_segment(text, position2, velocity)
            """

        """
        self._lists[x].set_text(self._lists[x])
        self._lists[x].set_position(self._dic_words[self._lists[x]][1])
        self._lists[x].set_points(self._dic_words[self._lists[x]][0])
        """

        #self.set_velocity(self._direction)


        

