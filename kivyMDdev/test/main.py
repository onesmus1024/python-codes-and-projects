from kivymd.app import MDApp
from kivy.lang import Builder


#root widget
class mainApp(MDApp):
    def build(self):
        #self.theme_cls.theme_style="Dark"
        return Builder.load_file("main.kv")
    def menu_click(self):
        print("menu icon clicked")
mainApp().run()