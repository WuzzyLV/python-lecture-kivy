from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
import math

class Task1(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.a_input = TextInput(hint_text='Enter side A', multiline=False)
        self.b_input = TextInput(hint_text='Enter side B', multiline=False)
        self.c_input = TextInput(hint_text='Enter side C', multiline=False)
        self.result_label = Label(text='Result:')
        result_layout = BoxLayout(orientation='horizontal')
        result_button = Button(text='Calculate')
        result_button.bind(on_press=self.calculate)
        
        layout.add_widget(Label(text='A:'))
        layout.add_widget(self.a_input)
        layout.add_widget(Label(text='B:'))
        layout.add_widget(self.b_input)
        layout.add_widget(Label(text='C:'))
        layout.add_widget(self.c_input)
        layout.add_widget(result_layout)
        result_layout.add_widget(result_button)
        result_layout.add_widget(self.result_label)

        return layout
    
    def calculate(self, instance):
        try:
            print(instance)
            a = float(self.a_input.text)
            b = float(self.b_input.text)
            c = float(self.c_input.text)
            p = (a + b + c) / 2
            S = math.sqrt(p * (p - a) * (p - b) * (p - c))
            self.result_label.text = f"Area: {S:.2f}"
        except ValueError:
            self.result_label.text = "Please enter valid numbers"

if __name__ == '__main__':
    Task1().run()
