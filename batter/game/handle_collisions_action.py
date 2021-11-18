from . import constants
from .action import Action
from .score_manager import ScoreManager


class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.

    Stereotype:
        Controller
    """

    def execute(self, cast):
        """Executes the action using the given actors.
        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """

        paddle = cast["paddle"][0]
        ball = cast["ball"][0]
        for brick in cast["brick"]:
            if brick.get_position().equals(ball.get_position()):
                cast["brick"].remove(brick)
                ball._velocity._y *= -1
                ScoreManager.score += 1
                break
        if paddle._position._x < ball._position._x < paddle._position._x + len(paddle._text) and \
                paddle._position._y - 1 == ball._position._y:
            ball._velocity._y *= -1
        if ball._position._y >= constants.MAX_Y:
            return True
