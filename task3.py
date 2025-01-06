from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
import random
from bubble_sort import bubble_sort


Window.size = (700, 700)

class Task2(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=25, spacing=10)

        self.error_label = Label(text="")

        self.n_label = Label(text="Enter N:")
        self.n_input = TextInput(hint_text="Enter a num", multiline=False)
        self.m_label = Label(text="Enter M:")
        self.m_input = TextInput(hint_text="Enter a num", multiline=False)

        self.calculate_button = Button(text="Calculate", on_press=self.calculate)

        self.a_label = Label(text="A: ...", size_hint_y=None, height=300)
        self.x_label = Label(text="X: ...")
        self.y_label = Label(text="Y: ...")

        self.layout.add_widget(self.error_label)
        self.layout.add_widget(self.n_label)
        self.layout.add_widget(self.n_input)
        self.layout.add_widget(self.m_label)
        self.layout.add_widget(self.m_input)
        self.layout.add_widget(self.calculate_button)
        self.layout.add_widget(self.a_label)
        self.layout.add_widget(self.x_label)
        self.layout.add_widget(self.y_label)

        return self.layout

    def calculate(self, *args):
        try:
            n = int(self.n_input.text)
            m = int(self.m_input.text)
            print(n, m)
            if n <= 0 or m <= 0:
                self.error_label.text = "Please enter a positive int"
                return

            A = []
            for i in range(m):
                A.append([])
                for j in range(n):
                    A[i].append(random.randint(-255, 255))

            X = []
            Y = []
            for i in range(m):
                for j in range(n):
                    if A[i][j] > 0:
                        X.append(A[i][j])
                    elif A[i][j] == 0:
                        continue
                    else:
                        Y.append(A[i][j])

            A_str = '\n'.join([str(row) for row in A])

            self.a_label.text = f"A:\n{A_str}"
            self.x_label.text = f"X: {bubble_sort(X)}"
            self.y_label.text = f"Y: {bubble_sort(Y)}"
            self.error_label.text = ""
        except ValueError:
            self.n_input.text = ""
            self.m_input.text = ""
            self.error_label.text = "Invalid inputs, int needed"

if __name__ == '__main__':
    Task2().run()
