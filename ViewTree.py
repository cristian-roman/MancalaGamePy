from pages.ViewModel import ViewModel


class ViewTree:
    views = []

    @staticmethod
    def init(ui_view: ViewModel):
        ViewTree.views = [ui_view]

    @staticmethod
    def push_view(view: ViewModel):
        ViewTree.views.append(view)

    @staticmethod
    def pop_view():
        ViewTree.views.pop()

    @staticmethod
    def get_current_view():
        return ViewTree.views[-1]
