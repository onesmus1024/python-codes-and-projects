from kivy.app import App
from kivy.lang import Builder
root = Builder.load_string('''
FloatLayout:
    canvas.before:
        Color:
            rgba: 0.5, 0.5, 0, 1
        Rectangle: # self here refers to the widget i.e FloatLayout
            pos: self.pos
            size: self.size
    Button:
        text: 'Hello World!!'
        size_hint: .3, .1
        pos_hint: {'center_x':.5, 'center_y': .8}
    Button:
        text:'onesmus'
        size_hint: .3, .1
        pos_hint: {'center_x':.5, 'center_y': .4}
''')
class MainApp(App):
    def build(self):
        return root
if __name__ == '__main__':
    MainApp().run()