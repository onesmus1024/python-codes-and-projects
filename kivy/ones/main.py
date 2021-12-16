from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.animation import Animation
from kivy.core.audio import SoundLoader
from kivy.uix.camera import Camera
from kivy.core.camera import CameraBase
#my root widget
class win1(Widget):
    def animate_it(self,widget,*args):
        sound = SoundLoader.load("/home/onesmus/Downloads/chris_brown_young_thug_go_crazy_official_video_mp3_39258.mp3")
        if sound:
            sound.play()

        camera = CameraBase()
        camera.init_camera()
        camera.start()
        camera.texture
        camera.stop()
        b= BoxLayout()
        animate = Animation(x=1,duration=0.5,transition="in_circ")+Animation(x=100,duration=0.5)
        animate.start(widget)
    pass

#my main appp
class summertech1024App(App):
    def build(self):
        return win1()

if __name__ =="__main__":
    summertech1024App().run()

