import kivy
kivy.require('1.0.5')
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.properties import StringProperty

root= Builder.load_string('''
<MyFirstWidget>:
    Button:
        on_press: root.text(txt_inpt.text)
        TextInput:
            id: txt_inpt
<MySecondWidget>:
    Button:
        on_press: root.text(txt_inpt.text)
    TextInput:
        id: txt_inpt
''')






class MyFirstWidget(BoxLayout):
    def text(self, val):
        print('text input text is: {txt}'.format(txt=val))



class MySecondWidget(BoxLayout):
    writing = StringProperty('')
    def text(self, val):
        self.writing = val


class docApp(App):

    def build(self):
        return root



if __name__ == "__main__":
    docApp().run()