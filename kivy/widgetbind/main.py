from kivy.app import App

from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget

#root widget class
class win1(Widget):

    def execute(self,*args):
        TextInput=self.ids['bindTextInput']
        for i in range(10):
            TextInput.text+="\nones"
    pass

class bindApp(App):
    def build(self):
        return win1()



if __name__ =="__main__":
    bindApp().run()
