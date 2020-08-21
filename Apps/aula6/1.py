from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView

class Tasks(ScrollView):
    def __init__(self,tasks,**kwargs):
        super().__init__(**kwargs)
        for task in tasks:
            self.ids.box.add_widget(Label(text = task, font_size = 30,size_hint_y = None,height = 200))
   

class Test(App):
    def build(self):
        return Tasks(['Fazer Compras', 'buscar filho','a'])


Test().run()
