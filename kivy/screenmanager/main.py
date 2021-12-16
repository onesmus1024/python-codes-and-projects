from kivy.app import App

from kivy.uix.spinner import Spinner
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import FadeTransition
from kivy.uix.screenmanager import ScreenManager, Screen

#screen one
class FirstScreen(Screen):
    def on_enter(self):
        print("entered first screen")
    pass

#screen two
class SecondScreen(Screen):
    pass

#Screen manager
class ScreenManager1(ScreenManager):
    pass


class MultipleScreenApp(App):
    def build(self):
        return ScreenManager1()


if __name__ =="__main__":
    MultipleScreenApp().run()