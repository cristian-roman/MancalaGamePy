from models.ViewModel import ViewModel


class ViewTree:

    def __init__(self, ui_view: ViewModel):
        self.views = [ui_view]

    def push_view(self, view):
        self.views.append(view)

    def pop_view(self):
        self.views.pop()

    def get_current_view(self):
        return self.views[-1]
