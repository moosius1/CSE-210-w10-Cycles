import constants

from game.casting.cast import Cast
from game.casting.cycle import Cycle
from game.scripting.script import Script
from game.scripting.control_actors_action import ControlActorsAction
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.scripting.draw_actors_action import DrawActorsAction
from game.directing.director import Director
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.shared.color import Color
from game.shared.point import Point


def main():
    
    # create the cast
    cast = Cast()
    cast.add_actor("cycle1", Cycle())
    cast.add_actor("cycle2", Cycle())


    #Example casting
    #  cast = Cast()
    # cast.add_actor("foods", Food())
    # cast.add_actor("snakes", Snake())
    # cast.add_actor("cycles", Cycle(constants.RED))
    # cast.add_actor("cycles", Cycle(constants.GREEN))
    # cast.add_actor("scores", Score())

    #adding in cast specifications with specific names to better identify them throughout the game
    #also added in start position as well as colors. 
    cycle1 = cast.get_first_actor("cycle1")
    cycle1.prepare_body(Point(0, 300), Point(constants.CELL_SIZE, 0), constants.BLUE)
    
    cycle2 = cast.get_first_actor("cycle2")
    cycle2.prepare_body(Point(900, 300), Point(constants.CELL_SIZE, 0), constants.ORANGE)

    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", ControlActorsAction(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("output", DrawActorsAction(video_service))
    
    director = Director(video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()