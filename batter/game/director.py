from time import sleep
from . import constants
from .score_manager import ScoreManager


class Director:
    """A code template for a person who directs the game. The responsibility of
    this class of objects is to control the sequence of play.

    Stereotype:
        Controller"""

    def __init__(self, cast, script, output_service):
        """The class constructor.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
            script (dict): The game actions {key: tag, value: list}.
        """
        self._output_service = output_service
        self._cast = cast
        self._script = script

    def start_game(self):
        """Starts the game loop to control the sequence of play."""
        while True:
            self._cue_action("input")
            if self._cue_action("update"):
                sleep(3)
                break
            self._cue_action("output")
            sleep(constants.FRAME_LENGTH)

    def _cue_action(self, tag):
        """Executes the actions with the given tag.

        Args:
            tag (string): The given tag.
        """
        for action in self._script[tag]:
            if action.execute(self._cast):
                self._output_service.print_game_over(ScoreManager.score)
                return True
