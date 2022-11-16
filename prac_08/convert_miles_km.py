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
        """ build the Kivy app from the kv file """
        Window.size = (350, 200)
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root


ConvertMileKm().run()
