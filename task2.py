from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
import math

Window.size = (400, 200)

class Task2(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=25, spacing=10)

        self.input_label = Label(text="Enter a positive int:")
        self.input_field = TextInput(hint_text="Enter a num", multiline=False)

        self.calculate_button = Button(text="Calculate", on_press=self.calculate)

        self.result_label = Label(text="Result: ")

        self.layout.add_widget(self.input_label)
        self.layout.add_widget(self.input_field)
        self.layout.add_widget(self.calculate_button)
        self.layout.add_widget(self.result_label)

        return self.layout

    def calculate(self, *args):
        try:
            number = int(self.input_field.text)
            if number <= 0:
                self.result_label.text = "Please enter a positive int"
                return

            factors = self.splitIntoMultipliers(number)
            factors_str = ' x '.join(map(str, factors))
            self.result_label.text = f"Result: {number}: {factors_str}"

        except ValueError:
            self.input_field.text = ""
            self.result_label.text = "Invalid input, int needed"


    def splitIntoMultipliers(self, n):
        i = 2
        multi = []
        while i * i <= n:
            while (n % i) == 0:
                multi.append(i)
                n /= i
                n = int(n)
            i += 1
        if n > 1:
            multi.append(n)
        return multi

if __name__ == '__main__':
    Task2().run()
