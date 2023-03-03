# testing environment for gui

import os

from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import StringProperty

from kivymd.app import MDApp

from kivymd.uix.filemanager import MDFileManager
from kivymd.toast import toast
from kivymd.uix.menu import MDDropdownMenu


KV = '''
MDBoxLayout:
    orientation: "vertical"

    MDTopAppBar:
        title: "Image Converter"
        elevation: 3

    MDLabel:
        text:"Image converter for file formats: jpg, png and webp.  Select the image you would like to convert using the button below.  Converted image will be saved in the same folder as the original image."
        halign:"center"
        padding:[20,20]

    MDFloatLayout:

        MDRoundFlatIconButton:
            text: "Select Image"
            icon: "folder"
            pos_hint: {"center_x": .25, "center_y": .5}
            on_release: app.file_manager_open()

        MDLabel:
            text: root.text_variable_1
            pos_hint: {"center_x":0.75, "center_y":.75}

        MDRaisedButton:
            id: button
            text: "Choose file type"
            pos_hint: {"center_x":0.75, "center_y":.5}
            on_release: app.menu.open()
            
        MDRoundFlatIconButton:
            text: "Select save location"
            icon: "folder"
            pos_hint: {"center_x": .5, "center_y": .5}
            on_release: app.file_manager_open()
        
        MDRaisedButton:
            text: "Convert"
            pos_hint: {"center_x":0.5, "center_y":.25}
            
'''


class Example(MDApp):
    text_variable_1 = StringProperty('text')
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        self.screen = Builder.load_string(KV)
        Window.bind(on_keyboard=self.events)
        self.manager_open = False
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager, select_path=self.select_path, preview=True
        )
        menu_items=[
            {"viewclass":"OneLineListItem" , "text":"pdf"},
            {"viewclass":"OneLineListItem" , "text":"jpg"},
            {"viewclass":"OneLineListItem" , "text":"png"},
            {"viewclass":"OneLineListItem" , "text":"webp"}
        ]
        self.menu= MDDropdownMenu(
            caller=self.screen.ids.button,
            items = menu_items,
            width_mult=4,
        )

        
       
    def menu_callback(self, text_item):
        print(text_item)

    def build(self):
        return self.screen

    def file_manager_open(self):
        self.file_manager.show(os.path.expanduser("~"))  # output manager to the screen
        self.manager_open = True

    def select_path(self, img_path: str):
        '''
        It will be called when you click on the file name
        or the catalog selection button.

        :param path: path to the selected directory or file;
        '''

        self.exit_manager()
        print(img_path)
        toast(img_path)

    def exit_manager(self, *args):
        '''Called when the user reaches the root of the directory tree.'''

        self.manager_open = False
        self.file_manager.close()

    def events(self, instance, keyboard, keycode, text, modifiers):
        '''Called when buttons are pressed on the mobile device.'''

        if keyboard in (1001, 27):
            if self.manager_open:
                self.file_manager.back()
        return True


Example().run()