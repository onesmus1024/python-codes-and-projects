from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.actionbar import ActionBar
from kivy.uix.scrollview import ScrollView

class LoginScreen(GridLayout):
    def __init__ (self, **kwargs):
        super(LoginScreen, self).__init__ ( **kwargs)
        self.cols = 1
        self.add_widget(Label(text='Username'))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)
        self.add_widget(Label(text='password'))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)
        self.button = Button(text='click me')
        self.add_widget(self.button)
class MyApp(App):
    def build(self):
        return LoginScreen()
if __name__ == '__main__':
    MyApp().run()