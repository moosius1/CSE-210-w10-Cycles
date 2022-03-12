import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the snake collides
    with the food, or the snake collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        #sets game as over and also creates empty string for stating which player is dead. 
        self._is_game_over = False
        self._dead_player = None

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_own_collision(cast)
            self._handle_cycle_collisions(cast)
            self._handle_game_over(cast)

    
  

    def _handle_own_collision(self,cast):
        cycle1 = cast.get_first_actor("cycle1")
        cycle1_head = cycle1.get_segments()[0]
        cycle1_segments = cycle1.get_segments()[1:]

        cycle2 = cast.get_first_actor("cycle2")
        cycle2_head = cycle2.get_segments()[0]
        cycle2_segments = cycle2.get_segments()[1:]

        #check to see if head of both cycles is equal to it's same segment

        for segment in cycle1_segments:
            if cycle1_head.get_position().equals(segment.get_position()):
                self._is_game_over = True
                self._dead_player = "cycle1"
        
        for segment in cycle2_segments:
            if cycle2_head.get_position().equals(segment.get_position()):
                self._is_game_over = True
                self._dead_player = "cycle2"

    def _handle_cycle_collisions(self,cast):
        cycle1 = cast.get_first_actor("cycle1")
        cycle1_head = cycle1.get_segments()[0]
        cycle1_segments = cycle1.get_segments()[1:]

        cycle2 = cast.get_first_actor("cycle2")
        cycle2_head = cycle2.get_segments()[0]
        cycle2_segments = cycle2.get_segments()[1:]

       #check if cycles hit one another, or if the head of cycle hits segment of other cycle

        for segment in cycle1_segments:
            if cycle2_head.get_position().equals(segment.get_position()):
                self._is_game_over = True
                self._dead_player = "cycle2"

        
        for segment in cycle2_segments:
            if cycle1_head.get_position().equals(segment.get_position()):
                self._is_game_over = True
                self._dead_player = "cycle1"

    def _handle_game_over(self, cast):
        """Shows the 'game over' message if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:

            #places text message in middle of screen

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 3)
            position = Point(x, y)

            #defines message as an actor and also evaluates which player died to output winner along with text. 

            message = Actor()
            if self._dead_player == "cycle1":
                color_winner = "Blue"
            elif self._dead_player == "cycle2":
                color_winner = "Orange"
            message.set_text(f"Game Over! {color_winner} Wins!")
            message.set_position(position)
            cast.add_actor("messages", message)
