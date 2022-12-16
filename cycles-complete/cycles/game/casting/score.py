from game.casting.actor import Actor


class Score(Actor):
    """
    A record of points made or lost. 
    
    The responsibility of Score is to keep track of the points the player has earned by eating food.
    It contains methods for adding and getting points. Client should use get_text() to get a string 
    representation of the points earned.

    Attributes:
        _points (int): The points earned in the game.
    """
    def __init__(self, player_value):
        super().__init__()
        self._player_value = player_value
        self._points = 0
        self.add_points(0)

    def add_points(self, points):
        """Adds the given points to the score's total points.
        
        Args:
            points (int): The points to add.
        """
        if self._player_value == 1:
            self._points += points
            self.set_text(f"Player 1 Score: {self._points}")
        elif self._player_value == 2:
            self._points += points
            self.set_text(f"Player 2 Score: {self._points}")
        else:
            self._points += points
            self.set_text(f"Score: {self._points}")

        def get_player_value(self):
            return self._player_value