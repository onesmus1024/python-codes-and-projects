from kivy.app import App
from kivy.uix.label import Label
import sys
import numpy as np
x = np.ones((2,2), dtype=int)
class MyApp(App):
    def build(self):
        return Label(text=str(x))
if __name__ == '__main__':
    MyApp().run()