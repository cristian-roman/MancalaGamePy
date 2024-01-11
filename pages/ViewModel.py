class ViewModel:
    """
    This class is the parent class of all the pages of the game.

    It is an abstract class, so it is not meant to be instantiated.

    It contains the loop() method, which is the main loop of the page.

    It also contains the _load_view() method, which is responsible for
    loading the view of the page.

    It also contains the _listen_for_events() method, which is responsible
    for listening for events.
    """
    def _loop(self):
        raise NotImplementedError

    def _load_view(self):
        raise NotImplementedError

    def _listen_for_events(self):
        raise NotImplementedError
