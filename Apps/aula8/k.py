from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

class Managment(ScreenManager):
    pass

class Menu(Screen):
    pass

class Tasks(Screen):
    def __init__(self,tasks = [],**kwargs):
        super().__init__(**kwargs)
        for task in tasks:
            self.ids.box.add_widget(Task(text = task))
    
    def on_pre_enter(self):
        Window.bind(on_keyboard = self.voltar)

    def voltar(self, window, key,*args):
        if key ==27:
            App.get_running_app().root.current = 'menu'
            return True

    def on_pre_leave(self):
        Window.unbind(on_keyboard = self.voltar)

    def addWidget(self):
        texto = self.ids.texto.text
        self.ids.box.add_widget(Task(text = texto))
        self.ids.texto.text = ''

class Task(BoxLayout):
    def __init__(self,text = '', **kwargs):
        super().__init__(**kwargs)
        self.ids.label.text = text

class Test(App):
    def build(self):
        return Managment()


Test().run()
