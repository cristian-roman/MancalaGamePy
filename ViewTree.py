from pages.ViewModel import ViewModel


class ViewTree:
    """
    This class keeps control of the pages of the game:
    - UI
    - Game
    - EndScreen

    It is a static class, so it is not meant to be instantiated.
    Only the init() method is meant to be called by the App class.

    It acts like a stack where the top is the current page.

    """
    views = []

    @staticmethod
    def init(ui_view: ViewModel):
        """
        Adds the first view to the ViewTree.
        :param ui_view:
        :return: None
        """
        ViewTree.views = [ui_view]

    @staticmethod
    def push_view(view: ViewModel):
        """
        Switches the current view to the given view,
        by adding it to top of the ViewTree.
        :param view:
        :return: None
        """
        ViewTree.views.append(view)

    @staticmethod
    def pop_view():
        """
        Goes back to the previous view,
        by removing the current view from the ViewTree.
        :return: None
        """
        ViewTree.views.pop()

    @staticmethod
    def get_current_view():
        """
        Returns the current view.
        :return: ViewModel
        """
        return ViewTree.views[-1]
