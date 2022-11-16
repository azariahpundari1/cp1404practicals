"""
CP1404 Programming II - Dynamic Labels
A program about dynamic labels
By Azariah Pundari
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabel(App):

    def __init__(self, **kwargs):
        """Initialize dynamic label app"""
        super().__init__(**kwargs)
        self.names = ["Azariah", "Bob", "Jeremy"]

    def build(self):
        """ Build dynamic label window"""
        # Window.size = (350, 200)
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_label.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create label from list of names"""
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.main.add_widget(temp_label)


DynamicLabel().run()
