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
        self._points = 0
        self.lists = []
        self.dic_words = {}
        self._prepare()

    def get_word(self, which_word):
        
        return self.list[which_word]
        

    def get_points(self):

        return self._points
        

    def reset(self):
        
        self._points = random.randint(1,5)
        position = Point(random.randrange(1, constants.MAX_X), random.randrange(1, constants.MAX_Y))
        self.set_position(position)

    def _prepare(self):
        all_quotes = open("speed_template\speed\game\words.txt", "r")
        list_quotes = all_quotes.readlines()

        """for x in range (0, 5):
            #Chooses a random quote from the list and then breaks the quote up into a list that is stored into val
            self.lists.append(random.choice(list_quotes))
            self.lists[x] = self.lists[x][:-1]"""
        for x in range (0, 5):
            #Chooses a random quote from the list and then breaks the quote up into a list that is stored into val
            word = random.choice(list_quotes)
            word = word[:-1]
            points = len(word)
            position = Point(random.randrange(0, constants.MAX_X), 1)
            self.dic_words[word] = [points, position]
            self.lists.append(word)

        self.set_text(self.lists[1])
        self.set_position(self.dic_words[self.lists[1]][1])
        self._points = self.dic_words[self.lists[1]][0]


        

