from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton, MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import MDLabel
from kivymd.uix.list import MDList, OneLineListItem
from kivymd.uix.screen import MDScreen
from kivymd.uix.textfield import MDTextField
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.toolbar import MDTopAppBar
from kivy.uix.scrollview import ScrollView


class ContactManagerApp(MDApp):
    def build(self):
        self.contacts = []
        self.screen = MDScreen()
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style = "Dark"
        self.toolbar = MDTopAppBar(title="Contact Manager")
        self.toolbar.pos_hint = {"top": 1}
        self.toolbar.right_action_items = [["magnify", lambda x: self.search_contact()]]
        self.screen.add_widget(self.toolbar)
        self.add_contact_button = MDRaisedButton(
            text="Add New Contact",
            pos_hint={"center_x": 0.5, "center_y": 0.1},
            on_release=self.add_contact
        )
        self.screen.add_widget(self.add_contact_button)

        self.contact_list = MDList()
        self.scroll = ScrollView()
        self.scroll.add_widget(self.contact_list)
        self.scroll.pos_hint = {"top": 0.9}
        self.scroll.size_hint_y = 0.8
        self.screen.add_widget(self.scroll)

        return self.screen

    def add_contact(self, instance):
        self.dialog = MDDialog(
            title="Add Contact",
            type="custom",
            content_cls=MDBoxLayout(
                MDTextField(hint_text=" Name"),
                MDTextField(hint_text="Phone Number"),
                MDTextField(hint_text="Email"),
                MDTextField(hint_text="Address"),
                orientation="vertical",
                spacing="12dp",
                size_hint_y=None,
                height="300dp"
            ),
            buttons=[
                MDFlatButton(text="CANCEL", on_release=self.close_dialog),
                MDRaisedButton(text="ADD", on_release=self.save_contact)
            ]
        )
        self.dialog.open()

    def close_dialog(self, instance):
        self.dialog.dismiss()

    def save_contact(self, instance):
        name = self.dialog.content_cls.children[3].text
        phone_number = self.dialog.content_cls.children[2].text
        email = self.dialog.content_cls.children[1].text
        address = self.dialog.content_cls.children[0].text
        contact = {
            "name": name,
            "phone_number": phone_number,
            "email": email,
            "address": address
        }
        self.contacts.append(contact)
        self.contact_list.add_widget(
            OneLineListItem(text=f"{name} - {phone_number}", on_release=lambda x, c=contact: self.view_contact(c))
        )
        self.dialog.dismiss()

    def view_contact(self, contact):
        self.dialog = MDDialog(
            title="View Contact",
            type="custom",
            content_cls=MDBoxLayout(
                MDLabel(text=f" Name: {contact['name']}"),
                MDLabel(text=f"Phone Number: {contact['phone_number']}"),
                MDLabel(text=f"Email: {contact['email']}"),
                MDLabel(text=f"Address: {contact['address']}"),
                orientation="vertical",
                spacing="12dp",
                size_hint_y=None,
                height="200dp"
            ),
            buttons=[
                MDFlatButton(text="CLOSE", on_release=self.close_dialog),
                MDFlatButton(text="DELETE", on_release=lambda x: self.delete_contact(contact)),
                MDRaisedButton(text="EDIT", on_release=lambda x: self.edit_contact(contact))
            ]
        )
        self.dialog.open()

    def edit_contact(self, contact):
        self.dialog.dismiss()
        self.dialog = MDDialog(
            title="Edit Contact",
            type="custom",
            content_cls=MDBoxLayout(
                MDTextField(text=contact["name"], hint_text="Name"),
                MDTextField(text=contact["phone_number"], hint_text="Phone Number"),
                MDTextField(text=contact["email"], hint_text="Email"),
                MDTextField(text=contact["address"], hint_text="Address"),
                orientation="vertical",
                spacing="12dp",
                size_hint_y=None,
                height="200dp"
            ),
            buttons=[
                MDFlatButton(text="CANCEL", on_release=self.close_dialog),
                MDRaisedButton(text="SAVE", on_release=lambda x: self.update_contact(contact))
            ]
        )
        self.dialog.open()

    def update_contact(self, contact):
        contact["name"] = self.dialog.content_cls.children[3].text
        contact["phone_number"] = self.dialog.content_cls.children[2].text
        contact["email"] = self.dialog.content_cls.children[1].text
        contact["address"] = self.dialog.content_cls.children[0].text
        self.refresh_contact_list()
        self.dialog.dismiss()

    def delete_contact(self, contact):
        self.contacts.remove(contact)
        self.refresh_contact_list()
        self.dialog.dismiss()

    def refresh_contact_list(self):
        self.contact_list.clear_widgets()
        for contact in self.contacts:
            self.contact_list.add_widget(
                OneLineListItem(text=f"{contact['name']} - {contact['phone_number']}",
                                on_release=lambda x, c=contact: self.view_contact(c))
            )

    def search_contact(self):
        self.dialog = MDDialog(
            title="Search Contact",
            type="custom",
            content_cls=MDBoxLayout(
                MDTextField(hint_text="Enter name or phone number"),
                orientation="vertical",
                spacing="12dp",
                size_hint_y=None,
                height="100dp"
            ),
            buttons=[
                MDFlatButton(text="CANCEL", on_release=self.close_dialog),
                MDRaisedButton(text="SEARCH", on_release=self.perform_search)
            ]
        )
        self.dialog.open()

    def perform_search(self, instance):
        query = self.dialog.content_cls.children[0].text.lower()
        self.contact_list.clear_widgets()
        for contact in self.contacts:
            if query in contact["name"].lower() or query in contact["phone_number"]:
                self.contact_list.add_widget(
                    OneLineListItem(text=f"{contact['name']} - {contact['phone_number']}",
                                    on_release=lambda x, c=contact: self.view_contact(c))
                )
        self.dialog.dismiss()


if __name__ == '__main__':
    ContactManagerApp().run()
