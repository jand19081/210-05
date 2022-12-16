import constants
from game.casting.actor import Actor
from game.shared.point import Point


class Cycle(Actor):
    """
    A motorcycle with a lighttrail.
    
    The responsibility of Cycle is to move itself.

    Attributes:
        _points (int): The number of points the food is worth.
    """
    def __init__(self, player_value):
        super().__init__()
        self._player = player_value
        self._segments = []
        self._prepare_body()
        

    def get_segments(self):
        return self._segments

    def move_next(self):
        # move all segments
        for segment in self._segments:
            segment.move_next()
        # update velocities
        for i in range(len(self._segments) - 1, 0, -1):
            trailing = self._segments[i]
            previous = self._segments[i - 1]
            velocity = previous.get_velocity()
            trailing.set_velocity(velocity)

    def get_head(self):
        return self._segments[0]

    def grow_tail(self, number_of_segments):
        for i in range(number_of_segments):
            tail = self._segments[-1]
            velocity = tail.get_velocity()
            offset = velocity.reverse()
            position = tail.get_position().add(offset)
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text("#")
            segment.set_color(self._get_tail_color())
            self._segments.append(segment)

    def turn_head(self, velocity):
        self._segments[0].set_velocity(velocity)

    def _get_tail_color(self):
        """Gets color of segments for a player."""
        if self._player == 1:
            return constants.BLUE
        elif self._player == 2:
            return constants.ORANGE
        else:
            return constants.WHITE
    
    def _prepare_body(self):
        
        if self._player == 1:
            x = int(constants.MAX_X)
            y = int(constants.MAX_Y / 4)
        elif self._player == 2:
            x = 0
            y = int(constants.MAX_Y * (3/4))

        for i in range(constants.CYCLE_LENGTH):
            position = Point(x - i * constants.CELL_SIZE, y)
            velocity = Point(1 * constants.CELL_SIZE, 0)
            text = "8" if i == 0 else "#"
            if i == 0:
                color = constants.YELLOW
            else:
                color = self._get_tail_color()
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text(text)
            segment.set_color(color)
            self._segments.append(segment)

    

    def set_player(self, player_value):
        """Sets the player value."""
        self._player = int(player_value)

    def get_player(self):
        return self._player