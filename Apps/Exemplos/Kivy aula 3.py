from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class Test(App):
    def build(self):
        box = BoxLayout(orientation='vertical')
        button = Button(text='Button 1', font_size = 30, on_release = self.incrementar)
        self.label = Label(text='1', font_size = 30)
        box.add_widget(button)
        box.add_widget(self.label)

        return box

    def incrementar(self, button):
        if button.text == 'Soltei':
            button.text = 'Voltei'
            self.label.text = str(int(self.label.text) + 1)
        else:
            self.label.text = str(int(self.label.text) + 1)
            button.text = 'Soltei'
        return


Test().run()
