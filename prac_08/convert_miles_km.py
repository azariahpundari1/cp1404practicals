"""
CP1404 Programming II - Convert Miles to Kilometers
A program that converts miles to kilometers
By Azariah Pundari
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty

KM_CONVERSION = 1.60934


class ConvertMileKm(App):
    """Convert mile to kilometer app start"""
    input_message = StringProperty()
    output_message = StringProperty()

    def build(self):
        """ Build miles to kilometers widget window"""
        Window.size = (350, 200)
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file('convert_miles_km.kv')
        self.input_message = "34"
        self.output_message = "5.717"
        return self.root

    def handle_calculate(self):
        """Calculate result using value set by user"""
        value = self.get_valid_number()
        result = float(value) * KM_CONVERSION
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, increment):
        """Increase or decrease input value by 1"""
        value = self.get_valid_number() + increment
        self.root.ids.user_input.text = str(value)

    def get_valid_number(self):
        """Get a valid number from user"""
        try:
            value = self.root.ids.user_input.text
            return int(value)
        except ValueError:
            pass


ConvertMileKm().run()
