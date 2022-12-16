import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the cycle collides
    with the food, or the cycle collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_food_collision(cast)
            self._handle_segment_collision(cast)
            self._handle_game_over(cast)

    def _handle_food_collision(self, cast):
        """Updates the score nd moves the food if the cycle collides with the food.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        score1 = cast.get_first_actor("score1")
        score2 = cast.get_first_actor("score2")
        food = cast.get_first_actor("foods")
        cycles = cast.get_first_actor("cycle1"), cast.get_first_actor("cycle2")
        
        for cycle in cycles:
            head = cycle.get_head()
            player = cycle.get_player()

            if head.get_position().equals(food.get_position()):
                points = food.get_points()
                cycle.grow_tail(points)
                
                if player == 1:
                    score1.add_points(points)
                elif player == 2:
                    score2.add_points(points)
                
                food.reset()
    
    def _handle_segment_collision(self, cast):
        """Sets the game over flag if the cycle collides with one of its segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        cycles = cast.get_first_actor("cycle1"), cast.get_first_actor("cycle2")
        cycle1 = cycles[0]
        cycle2 = cycles[1]
        segments = cycle1.get_segments()[1:] + cycle2.get_segments()[1:]
        head1 = cycle1.get_segments()[0]
        head2 = cycle2.get_segments()[0]
            
        for segment in segments:
            if head1.get_position().equals(segment.get_position()):
                    self._is_game_over = True

            if head2.get_position().equals(segment.get_position()):
                    self._is_game_over = True
        

    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the cycle and food white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            cycles = cast.get_first_actor("cycle1"), cast.get_first_actor("cycle2")
            food = cast.get_first_actor("foods")

            for cycle in cycles:
                segments = cycle.get_segments()
            

                x = int(constants.MAX_X / 2)
                y = int(constants.MAX_Y / 2)
                position = Point(x, y)

                message = Actor()
                message.set_text("Game Over!")
                message.set_position(position)
                cast.add_actor("messages", message)

                for segment in segments:
                    segment.set_color(constants.WHITE)
                food.set_color(constants.WHITE)