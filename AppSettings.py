class AppSettings:
    """
    This class serves as a common place for all the settings of the game.
    Any class can access the settings of the game by importing this class

    It has an init method that initialize the font for the game
    """
    name = "Mancala Game"
    width = 1280
    height = 720
    colors = {
        'white': (255, 255, 255),
        'black': (0, 0, 0),
        'light_gray': (200, 200, 200),
        'green': (0, 255, 0),
        'orange_h4': (230, 115, 0),
        'orange_h2': (179, 89, 0),
        'no_color': (0, 0, 0, 0),
        'orange_h6': (161, 61, 27)
    }
    board_width = 800
    board_height = 500

    font = None

    @staticmethod
    def init(font):
        """
        This method initializes the font of the game.
        It is called only once by the App.init() method.
        """
        AppSettings.font = font
