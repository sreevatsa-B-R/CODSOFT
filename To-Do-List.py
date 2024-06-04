from kivy.uix.scrollview import ScrollView
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.list import MDList, TwoLineListItem
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel


class TodoListApp(MDApp):

    def build(self):
        self.tasks = []
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style = "Dark"

        self.screen = MDScreen()
        self.screen.add_widget(MDLabel(
            text="To-Do List",
            font_style='H3',
            size_hint=(1, 0.5),
            pos_hint={'x': 0.35, 'y': 0.7}
        ))
        self.task_input = MDTextField(
            icon_left="plus",
            hint_text="Add a Task",
            size_hint=(0.5, None),
            mode="round",
            pos_hint={"center_x": 0.5, "center_y": 0.1},
            on_text_validate=self.add_task
        )
        self.scroll = ScrollView(pos_hint={"center_x": 0.75, "center_y": 0.4})
        self.task_list = MDList(
            size_hint=(0.5, None),
            md_bg_color="grey"
        )
        self.scroll.add_widget(self.task_list)
        self.screen.add_widget(self.scroll)
        self.screen.add_widget(self.task_input)
        return self.screen

    def add_task(self, *args):
        task_text = self.task_input.text.strip()
        if task_text:
            self.tasks.append(task_text)
            self.task_input.text = ""
            self.update_task_list()

    def update_task_list(self):
        self.task_list.clear_widgets()
        for task in self.tasks:
            item = TwoLineListItem(
                text=task,
                secondary_text="Click to remove",
                on_release=self.delete_task
            )
            self.task_list.add_widget(item)

    def delete_task(self, instance):
        task_text = instance.text
        self.tasks.remove(task_text)
        self.update_task_list()


if __name__ == "__main__":
    TodoListApp().run()
