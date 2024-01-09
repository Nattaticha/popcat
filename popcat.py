import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput

class MenuApp(App):

    def build(self):
        self.screen_manager = ScreenManager()

        # สร้าง Screen สำหรับหน้าเมนู
        self.menu_screen = Screen(name='menu')
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        play_button = Button(text="Play", size_hint=(1, 0.5))
        play_button.bind(on_press=self.switch_to_play_screen)
        layout.add_widget(play_button)
        setting_button = Button(text="Setting", size_hint=(1, 0.5))
        setting_button.bind(on_press=self.open_settings)
        layout.add_widget(setting_button)
        self.menu_screen.add_widget(layout)
        self.screen_manager.add_widget(self.menu_screen)

        # สร้าง Screen สำหรับหน้าเล่นเกม
        self.play_screen = Screen(name='play')
        play_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        play_layout.add_widget(Label(text="Enter your name:"))
        self.name_input = TextInput(hint_text="Enter Name", size_hint=(1, 0.2))
        play_layout.add_widget(self.name_input)
        self.play_screen.add_widget(play_layout)
        self.screen_manager.add_widget(self.play_screen)

        return self.screen_manager

    def switch_to_play_screen(self, instance):
        self.screen_manager.current = 'play'

    def play_game(self, instance):
        print("Start popcat with Name:", self.name_input.text)

    def open_settings(self, instance):
        print("Opensetting")

if __name__ == "__main__":
    MenuApp().run()


# class MenuApp(App):

#     def build(self):
#         layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

#         # สร้างปุ่ม Play
#         play_button = Button(text="Play", size_hint=(1, 0.5))
#         play_button.bind(on_press=self.play_game)
#         layout.add_widget(play_button)

#         # สร้างปุ่ม Setting
#         setting_button = Button(text="Setting", size_hint=(1, 0.5))
#         setting_button.bind(on_press=self.open_settings)
#         layout.add_widget(setting_button)

#         return layout

# class Screen(App):
#         def build(self):
#             self.screen_manager = ScreenManager()
#             # สร้าง Screen สำหรับหน้าเมนู
#             self.menu_screen = Screen(name='menu')
#             layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
#             play_button = Button(text="Play!", size_hint=(1, 1))
#             play_button.bind(on_press=self.switch_to_play_screen)
#             layout.add_widget(play_button)
#             self.menu_screen.add_widget(layout)
#             self.screen_manager.add_widget(self.menu_screen)

#             # สร้าง Screen สำหรับหน้าเล่นเกม
#             self.play_screen = Screen(name='play')
#             play_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
#             play_layout.add_widget(Label(text="Enter your name:"))
#             self.name_input = TextInput(hint_text="Enter Name", size_hint=(1, 0.2))
#             play_layout.add_widget(self.name_input)
#             self.play_screen.add_widget(play_layout)
#             self.screen_manager.add_widget(self.play_screen)

#             return self.screen_manager

#         def switch_to_play_screen(self, instance):
#             self.screen_manager.current = 'play'

#         def play_game(self, instance):
#             print("Start popcat with Name:", self.name_input.text)

#         def open_settings(self, instance):
#             print("Opensetting")
#     # def play_game(self, instance):
#     #     print("เริ่มเกม!")

#     # def open_settings(self, instance):
#     #     print("เปิดตั้งค่า!")

        


# if __name__ == "__main__":
#     MenuApp().run()


