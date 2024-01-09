import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout

#โค้ดที่ start -> icon
class MenuApp(App):

    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # สร้างปุ่ม Play
        play_button = Button(text="Play", size_hint=(1, 0.5))
        play_button.bind(on_press=self.play_game)
        layout.add_widget(play_button)

        # สร้างปุ่ม Setting
        setting_button = Button(text="Setting", size_hint=(1, 0.5))
        setting_button.bind(on_press=self.open_settings)
        layout.add_widget(setting_button)

        return layout

class MenuApp(App):

    def build(self):
        self.screen_manager = ScreenManager()

        # ... [โค้ดเดิมสำหรับสร้าง Screen สำหรับหน้าเมนูและหน้าเล่นเกม]
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

        
        # สร้าง Screen สำหรับหน้าเลือกไอคอน
        self.icon_selection_screen = Screen(name='icon_selection')
        icon_layout = GridLayout(cols=3, spacing=10, padding=10)

        # สร้างปุ่มไอคอน
        icon_names = ['icon1.png', 'icon2.png', 'icon3.png']  # ระบุชื่อไฟล์ไอคอนที่คุณมี
        for icon_name in icon_names:
            icon_button = Button(background_normal=icon_name, size_hint=(0.3, 0.3))
            icon_button.bind(on_press=self.select_icon)  # ผูกเชื่อมกับฟังก์ชันเลือกไอคอน
            icon_layout.add_widget(icon_button)

        self.icon_selection_screen.add_widget(icon_layout)
        self.screen_manager.add_widget(self.icon_selection_screen)

        return self.screen_manager

    def switch_to_play_screen(self, instance):
        self.screen_manager.current = 'icon_selection'  # เปลี่ยนไปยังหน้าเลือกไอคอน

    def play_game(self, instance):
        print("Start popcat with Name:", self.name_input.text)

    def open_settings(self, instance):
        print("Opensetting")

    def select_icon(self, instance):
        print(f"Selected icon: {instance.background_normal}")


#codeที่start->enter name
# class MenuApp(App):

#     def build(self):
#         self.screen_manager = ScreenManager()

#         # สร้าง Screen สำหรับหน้าเมนู
#         self.menu_screen = Screen(name='menu')
#         layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
#         play_button = Button(text="Play", size_hint=(1, 0.5))
#         play_button.bind(on_press=self.switch_to_play_screen)
#         layout.add_widget(play_button)
#         setting_button = Button(text="Setting", size_hint=(1, 0.5))
#         setting_button.bind(on_press=self.open_settings)
#         layout.add_widget(setting_button)
#         self.menu_screen.add_widget(layout)
#         self.screen_manager.add_widget(self.menu_screen)

#         # สร้าง Screen สำหรับหน้าเล่นเกม
#         self.play_screen = Screen(name='play')
#         play_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
#         play_layout.add_widget(Label(text="Enter your name:"))
#         self.name_input = TextInput(hint_text="Enter Name", size_hint=(1, 0.2))
#         play_layout.add_widget(self.name_input)
#         self.play_screen.add_widget(play_layout)
#         self.screen_manager.add_widget(self.play_screen)

#         # สร้าง Screen สำหรับหน้าเลือก icon 
#         self.play_screen = Screen(name='icon')
#         play_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
#         play_layout.add_widget(Label(text="Enter your name:"))
#         self.name_input = TextInput(hint_text="Enter Name", size_hint=(1, 0.2))
#         play_layout.add_widget(self.name_input)
#         self.play_screen.add_widget(play_layout)
#         self.screen_manager.add_widget(self.play_screen)

#         #สร้าง screen สำหรับ หน้าเลือกicon
#         self.icon_selection_screen = Screen(name='icon_selection')
#         icon_layout = GridLayout(cols=3, spacing=10, padding=10)

#         # สร้างปุ่มicon
#         icon_names = ['icon1.png', 'icon2.png', 'icon3.png']  # ระบุชื่อไฟล์ไอคอนที่คุณมี
#         for icon_name in icon_names:
#             icon_button = Button(background_normal=icon_name, size_hint=(0.3, 0.3))
#             icon_button.bind(on_press=self.select_icon)  # ผูกเชื่อมกับฟังก์ชันเลือกไอคอน
#             icon_layout.add_widget(icon_button)

#         self.icon_selection_screen.add_widget(icon_layout)
#         self.screen_manager.add_widget(self.icon_selection_screen)


#         return self.screen_manager

#     def switch_to_play_screen(self, instance):
#         self.screen_manager.current = 'play'

#     def play_game(self, instance):
#         print("Start popcat with Name:", self.name_input.text)

#     def open_settings(self, instance):
#         print("Opensetting")

#     def select_icon(self, instance):
#         print(f"Selected icon: {instance.background_normal}")



if __name__ == "__main__":
    MenuApp().run()


