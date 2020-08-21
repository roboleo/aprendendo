from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class Incrementador(BoxLayout):
    
    pass
   

class Test(App):
    def build(self):
        return Incrementador()


Test().run()
