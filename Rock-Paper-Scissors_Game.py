import random
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton, MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import MDLabel
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.screen import MDScreen


class Rock_Paper_Scissors(MDApp):

    def menu_callback(self, user_choice):
        mylist = ["rock", "paper", "scissor"]
        c_choice = random.choice(mylist)
        self.menu.dismiss()
        self.check(user_choice, c_choice)

    def build(self):
        self.u_count = 0
        self.c_count = 0
        self.tie_count = 0
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style = "Dark"
        self.screen = MDScreen()
        self.screen.add_widget(MDLabel(
            text="Rock Paper Scissors",
            font_style='H3',
            size_hint=(1, 0.5),
            pos_hint={'center_x': 0.7, 'center_y': 0.9}
        ))

        menu_items = [
            {
                "text": "rock",
                "viewclass": "OneLineListItem",
                "height": 40,
                "on_release": lambda x="rock": self.menu_callback(x)
            },
            {
                "text": "paper",
                "viewclass": "OneLineListItem",
                "height": 40,
                "on_release": lambda x="paper": self.menu_callback(x)
            },
            {
                "text": "scissor",
                "viewclass": "OneLineListItem",
                "height": 40,
                "on_release": lambda x="scissor": self.menu_callback(x)
            },
        ]

        self.user_label = MDLabel(
            text="User's Score",
            size_hint=(0.5, None),
            pos_hint={'x': 0.1, 'y': 0.75}
        )
        self.com_label = MDLabel(
            text="Computer's Score",
            size_hint=(0.5, None),
            pos_hint={'x': 0.4, 'y': 0.75}
        )
        self.tie_label = MDLabel(
            text="Tie",
            size_hint=(0.5, None),
            pos_hint={'x': 0.8, 'y': 0.75}
        )

        self.tie_score = MDLabel(
            text="0",
            size_hint=(0.5, None),
            pos_hint={'x': 0.8, 'y': 0.65}
        )
        self.u_score = MDLabel(
            text="0",
            size_hint=(0.5, None),
            pos_hint={'x': 0.1, 'y': 0.65}
        )
        self.c_score = MDLabel(
            text="0",
            size_hint=(0.5, None),
            pos_hint={'x': 0.4, 'y': 0.65}
        )
        self.result = MDLabel(
            text="",
            size_hint=(0.5, None),
            pos_hint={'center_x': 0.5, 'center_y': 0.4}
        )

        self.select = MDRaisedButton(
            text="Select",
            pos_hint={"center_x": 0.5, "center_y": 0.5},
        )

        self.menu = MDDropdownMenu(
            caller=self.select,
            items=menu_items,
            width_mult=2,
        )

        self.select.bind(on_release=lambda x: self.menu.open())

        self.screen.add_widget(self.user_label)
        self.screen.add_widget(self.com_label)
        self.screen.add_widget(self.u_score)
        self.screen.add_widget(self.c_score)
        self.screen.add_widget(self.tie_score)
        self.screen.add_widget(self.tie_label)
        self.screen.add_widget(self.result)
        self.screen.add_widget(self.select)

        return self.screen

    def show_dialog(self,result_text):
        self.dialog = MDDialog(
            text=f"{result_text}\n\nPlay again?",
            buttons=[
                MDFlatButton(text="Yes", on_release=self.close_dialog),
                MDFlatButton(text="No", on_release=self.stop_app)
            ],
        )
        self.dialog.open()

    def close_dialog(self, *args):
        self.dialog.dismiss()

    def stop_app(self, *args):
        self.dialog.dismiss()
        MDApp.get_running_app().stop()

    def check(self, user_choice, c_choice):
        if c_choice == user_choice:
            result_text = f"Both chose {user_choice}. It's a tie!"
            self.tie_count += 1
            self.tie_score.text = str(self.tie_count)
        elif (user_choice == "rock" and c_choice == "scissor") or \
             (user_choice == "paper" and c_choice == "rock") or \
             (user_choice == "scissor" and c_choice == "paper"):
            result_text = f"You chose {user_choice}, Computer chose {c_choice}. You Won!"
            self.u_count += 1
            self.u_score.text = str(self.u_count)
        else:
            result_text = f"You chose {user_choice}, Computer chose {c_choice}. You Lost!"
            self.c_count += 1
            self.c_score.text = str(self.c_count)

        self.result.text = result_text
        self.show_dialog(result_text)


if __name__ == '__main__':
    Rock_Paper_Scissors().run()
