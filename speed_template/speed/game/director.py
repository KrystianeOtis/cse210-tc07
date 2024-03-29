from time import sleep
from game import constants
from game.food import Food
from game.score import Score
from game.snake import Snake

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        food (Food): The snake's target.
        input_service (InputService): The input mechanism.
        keep_playing (boolean): Whether or not the game can continue.
        output_service (OutputService): The output mechanism.
        score (Score): The current score.
        snake (Snake): The player or snake.
    """

    def __init__(self, input_service, output_service):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self._food = Food()
        self._input_service = input_service
        self._keep_playing = True
        self._output_service = output_service
        self._score = Score()
        self._snake = Snake() #grant_note won't need this... maybe
        
    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        while self._keep_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()
            sleep(constants.FRAME_LENGTH)

    def _get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means getting the desired direction and moving the snake.

        Args:
            self (Director): An instance of Director.
        """
        letter = self._input_service.get_letter()
        self._snake.get_points(letter)
        self._food.move_word()

        """#grant_note we will make a value where if enter is pressed then it will do what is needed
        if("enter"):
            pass"""

    def _do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means checking for a collision and updating the score.

        Args:
            self (Director): An instance of Director.
        """
        #self._handle_body_collision()
        #self._food.add_one()
        self._handle_food_collision()
        
        
    def _do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means checking if there are stones left and declaring 
        the winner.

        Args:
            self (Director): An instance of Director.
        """
        self._output_service.clear_screen()
        self._output_service.draw_actors(self._food.get_all()) #need to fix
        self._output_service.draw_actor(self._snake) #grant_note display the guessed word
        self._output_service.draw_actor(self._score)
        self._output_service.flush_buffer()

    def _handle_body_collision(self):
        """Handles collisions between the snake's head and body. Stops the game 
        if there is one.

        Args:
            self (Director): An instance of Director.
        """ 


        head = self._snake.get_head()
        body = self._snake.get_body()
        for segment in body:
            if head.get_position().equals(segment.get_position()):
                self._keep_playing = False
                break

    def _handle_food_collision(self):
        """Handles collisions between the snake's head and the food. Grows the 
        snake, updates the score and moves the food if there is one.

        Args:
            self (Director): An instance of Director.
        """
        #grant_note this section we might use to see if what the user typed matches with any of the words

        #grant_note we also need to make sure that it only activates if the user clicks enter, aka, when the last character in the guessed word string equals "*"

        compare = "0"
        written = self._snake.get_word()
        if(written != ""):
            compare = written
            compare = compare.rstrip(compare[-1])
            compare += "*"

        food = self._food.get_text()+"*"
        if(written == food):
            points = self._food.get_points()
            self._score.add_points(points)
            self._snake.reset()
            self._food.reset()
        elif(written == compare):
            self._snake.reset()

        
        """
        head = self._snake.get_head()
        if head.get_position().equals(self._food.get_position()):
            points = self._food.get_points()
            for n in range(points):
                self._snake.grow_tail()
            self._score.add_points(points)
            self._food.reset() 
            """