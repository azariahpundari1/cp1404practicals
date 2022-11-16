"""
CP1404 Programming II - Convert Miles to Kilometers
A program that converts miles to kilometers
By Azariah Pundari
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class ConvertMileKm(App):
    """Convert mile to kilometer app start"""

    def build(self):
        """ Build miles to kilometers widget window"""
        Window.size = (350, 200)
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self, value):
        try:
            result = float(value) * 1.60934
            self.root.ids.output_label.text = f"{str(result)} km"
        except ValueError:
            pass

    def handle_up_increment(self):
        # TODO do code for this
        pass

    def handle_down_increment(self):
        # TODO do code for this
        pass


ConvertMileKm().run()
