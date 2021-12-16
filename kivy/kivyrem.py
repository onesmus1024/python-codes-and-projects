from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):#subclassing App class
    def build(self):#build is a method from App class whick is used to load the root widgets
        return Label(text="onesmus")


if __name__ == '__main__':
    MyApp().run()