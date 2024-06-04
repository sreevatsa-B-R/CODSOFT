from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivymd.uix.textfield import MDTextField


class Calculator(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style = "Dark"

        self.screen = MDScreen()
        self.Title = MDLabel(
            text="Calculator",
            font_style='H3',
            pos_hint={"x": 0.4, "center_y": 0.9},

        )
        self.input1 = MDTextField(
            hint_text="First Number",
            size_hint=(0.2, None),
            mode="round",
            pos_hint={"center_x": 0.3, "center_y": 0.7},
        )
        self.operater = MDTextField(
            hint_text="operater",
            size_hint=(0.1, None),
            mode="round",
            pos_hint={"center_x": 0.5, "center_y": 0.7},
        )
        self.input2 = MDTextField(
            hint_text="secound Number",
            size_hint=(0.2, None),
            mode="round",
            pos_hint={"center_x": 0.7, "center_y": 0.7},
        )
        self.Press_button = MDRaisedButton(
            text="calculate",
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            on_press=self.cal_process
        )
        self.output = MDLabel(
            text="",
            size_hint=(0.2, None),
            pos_hint={"center_x": 0.5, "center_y": 0.3},

        )
        self.screen.add_widget(self.Title)
        self.screen.add_widget(self.input1)
        self.screen.add_widget(self.operater)
        self.screen.add_widget(self.input2)
        self.screen.add_widget(self.Press_button)
        self.screen.add_widget(self.output)

        return self.screen

    def cal_process(self, i):
        if self.input1.text.isdigit() and self.input2.text.isdigit():
            if self.operater.text == "+":
                self.output.text = "The Output is " + str(int(self.input1.text) + int(self.input2.text))
            elif self.operater.text == "-":
                self.output.text = "The Output is " + str(int(self.input1.text) - int(self.input2.text))
            elif self.operater.text == "*":
                self.output.text = "The Output is " + str(int(self.input1.text) * int(self.input2.text))
            elif self.operater.text == "/":
                self.output.text = "The Output is " + str(int(self.input1.text) / int(self.input2.text))
            else:
                self.output.text = "invalid operater"
        else:
            self.output.text = "enter a valid Number"


if __name__ == "__main__":
    Calculator().run()
