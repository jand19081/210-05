import constants

from game.casting.cast import Cast
from game.casting.food import Food
from game.casting.score import Score
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
    cast.add_actor("foods", Food())

    # Score 1
    score1 = Score(1)
    cast.add_actor("score1", score1)

    # Score 2
    score2 = Score(2)
    score2.set_position(Point(constants.MAX_X - 200, 0))
    cast.add_actor("score2", score2)


    # Add cycles to cast

    # Cycle1
    cycle1 = Cycle(1)
    cast.add_actor("cycle1", cycle1)

    # Cycle2
    cycle2 = Cycle(2)
    cast.add_actor("cycle2", cycle2)

   
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