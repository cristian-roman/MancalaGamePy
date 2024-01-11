class GameComponent:

    """
    An interface for the components of the game.

    It is an abstract class, so it cannot be instantiated.

    It has only one method, the _draw() method, that must be implemented
    """
    def _draw(self):
        raise NotImplementedError
