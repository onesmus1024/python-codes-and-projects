from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout

root = Builder.load_file("python/kivy/app2/ones.kv")


class onesApp(App):
    #build method from App class to load the root widget
    def build(self):
        return root


if __name__ == "__main__":
    onesApp().run()