from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import ScreenManager, Screen

class Managment(ScreenManager):
    pass

class Tasks(BoxLayout):
    def __init__(self,tasks,**kwargs):
        super().__init__(**kwargs)
        for task in tasks:
            self.ids.box.add_widget(Task(text = task))
    
    def addWidget(self):
        texto = self.ids.texto.text
        self.ids.box.add_widget(Task(text = texto))
        self.ids.texto.text = ''
class Task(BoxLayout):
    def __init__(self,text = '', **kwargs):
        super().__init__(**kwargs)
        self.ids.label.text = text
        return

class Test(App):
    def build(self):
        return Tasks(['Fazer Compras', 'buscar filho','a'])


Test().run()
