from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget


#root widget for our app

class win1(Widget):
    pass

#app class
class MyApp(App):
    #override build method of App class to render the root widget
    def build(self):
        return win1()

if __name__ =="__main__":
    MyApp().run()