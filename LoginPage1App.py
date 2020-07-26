from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.core.window import Window

Window.size = 	(360, 640)
class MainApp(MDApp):

    def build(self):
        self.theme_cls.theme_style='Dark'
        return Builder.load_file('LoginPage1.kv')
        


MainApp().run()
