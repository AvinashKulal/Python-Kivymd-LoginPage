from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.factory import Factory
from kivy.core.window import Window
Window.size = 	(360, 640)


Builder.load_string("""
#:include LoginPage2.kv
#:import utils kivy.utils
""")


class MainApp(MDApp):
    def __init__(self,**kwargs):
        self.title = 'MY FIRST LOGIN PAGE'
        self.sc = ScreenManager()
        self.theme_cls.primary_style='Dark'
        super().__init__(**kwargs)
    def build(self):
        self.sc.add_widget(Factory.LoginScreen())
        return self.sc

MainApp().run()
