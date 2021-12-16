from kivy.app import App

from kivy.uix.label import Label
from kivy.uix.scatter import Scatter
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.actionbar import ActionBar

class scatterApp(App):
    def build(self):
        a = ActionBar()
        g = BoxLayout(orientation='vertical')
        s = Scatter()
        l = Label(text="ones",font_size=150)
        t = TextInput(text="ones")
        g.add_widget(a)
        g.add_widget(s)
        g.add_widget(t)
        s.add_widget(l)
        t.bind(text=l.setter('text'))
        return g


if __name__ == "__main__":
    scatterApp().run()