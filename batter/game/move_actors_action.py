from . import constants
from .action import Action
from .point import Point


class MoveActorsAction(Action):
    """A code template for moving actors. The responsibility of this class of
    objects is move any actor that has a velocity more than zero.

    Stereotype:
        Controller
    Attributes:
        _input_service (InputService): An instance of InputService.
    """

    def execute(self, cast):
        """Executes the action using the given actors.
        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        for group in cast.values():
            for actor in group:
                if not actor.get_velocity().is_zero():
                    self._move_actor(actor)

    def _move_actor(self, actor):
        """Moves the given actor to its next position according to its
        velocity. Will wrap the position from one side of the screen to the
        other when it reaches the edge in either direction.

        Args:
            actor (Actor): The actor to move.
        """

        if actor._text == "@":
            actor._position._x += actor._velocity._x
            if actor._position._x < 0 or actor._position._x > constants.MAX_X:
                actor._velocity._x *= -1
                actor._position._x += actor._velocity._x
            actor._position._y += actor._velocity._y
            if actor._position._y < 0 or actor._position._y > constants.MAX_Y:
                actor._velocity._y *= -1
                actor._position._y += actor._velocity._y

        if actor._text == "===========":
            actor._position._x += actor._velocity._x
            if actor._position._x < -3 or actor._position._x > constants.MAX_X - len(actor._text) + 1:
                actor._position._x -= actor._velocity._x
