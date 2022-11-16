from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    def build(self):
        """Build a box layout model of greeting a user"""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """Greet the user after user enter name"""
        print('greet')  # test
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"

    def handle_clear(self):
        """Reset output label to default - Enter name"""
        self.root.ids.output_label.text = "Enter name"


BoxLayoutDemo().run()
