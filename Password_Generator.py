import random
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivymd.uix.textfield import MDTextField


class Password_Generator(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style = "Dark"
        self.screen = MDScreen()
        self.screen.add_widget(MDLabel(
            text="Password_Generator",
            font_style='H3',
            size_hint=(1, 0.5),
            pos_hint={'x': 0.2, 'y': 0.7}
        ))
        self.input2 = MDTextField(
            hint_text="Enter The Lenth",
            size_hint=(0.2, None),
            mode="round",
            pos_hint={"center_x": 0.3, "center_y": 0.7},
        )
        self.Press_button = MDRaisedButton(
            text="Genrate",
            pos_hint={"center_x": 0.5, "center_y": 0.7},
            on_press=self.gen_pass
        )
        self.output = MDLabel(
            text="",
            size_hint=(0.5, None),
            pos_hint={"center_x": 0.5, "center_y": 0.3},

        )
        self.screen.add_widget(self.input2)
        self.screen.add_widget(self.Press_button)
        self.screen.add_widget(self.output)
        return self.screen

    def gen_pass(self, i):
        pass1 = ""
        for i in range(int(self.input2.text)):
            pass1 += random.choice(
                "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+/*-.,<>?|")
        self.output.text = "The Genrated Password is   " + pass1
        self.Press_button.text = "ReGenrate"


if __name__ == '__main__':
    Password_Generator().run()
