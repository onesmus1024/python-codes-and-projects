from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from  kivy.uix.widget import Widget
from kivy.animation import Animation
from kivy.lang import Builder
#loading our kivy file
#root widget
class win1(Widget):
    def animate_it(self,widget,*args):
        #difine animation
        #first animation
        animate = Animation(
            background_color=(0,0,1,1))
        #second animation
        
        #third aniamtion
        animate +=Animation(
            size_hint=(0.5,0.5))
        animate +=Animation(
            size_hint=(1,1))
        animate += Animation(
            background_color=(0,0,0,1))
        
        animate.start(widget)

        #call back
        animate.bind(on_complete=self.my_call_back)
    def my_call_back(self,*args):
        pass
        #self.ids[animate_Btn1].text="finished animating"

class animation(App):
    def build(self):
        return win1()

if __name__ == "__main__":
    animation().run()