import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout

class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super(MenuScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        play_button = Button(text="Play", size_hint=(1, 0.5))
        play_button.bind(on_press=self.switch_to_play_screen)
        layout.add_widget(play_button)

        setting_button = Button(text="Setting", size_hint=(1, 0.5))
        setting_button.bind(on_press=self.open_settings)
        layout.add_widget(setting_button)

        how_to_play_button = Button(text="How to Play", size_hint=(1, 0.5))
        how_to_play_button.bind(on_press=self.open_how_to_play)
        layout.add_widget(how_to_play_button)

        self.add_widget(layout)

    def switch_to_play_screen(self, instance):
        self.manager.current = 'play'

    def open_settings(self, instance):
        self.manager.current = 'sound_setting'

    def open_how_to_play(self, instance):
        self.manager.current = 'how_to_play'


class SoundSettingScreen(Screen):
    def __init__(self, **kwargs):
        super(SoundSettingScreen, self).__init__(**kwargs)
        self.sound_on = True  # เพิ่มตัวแปรสถานะสำหรับเสียง

        sound_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        sound_label = Label(text="Sound Settings")
        sound_layout.add_widget(sound_label)

        audio_button = Button(text="Audio On" if self.sound_on else "Audio Off", size_hint=(1, 0.5))
        audio_button.bind(on_press=self.toggle_audio)
        sound_layout.add_widget(audio_button)

        back_button = Button(text="Back", size_hint=(1, 0.5))
        back_button.bind(on_press=self.go_back)
        sound_layout.add_widget(back_button)

        self.add_widget(sound_layout)

    def toggle_audio(self, instance):
        self.sound_on = not self.sound_on
        instance.text = "Audio On" if self.sound_on else "Audio Off"
        # เพิ่มโค้ดเพื่อทำงานเมื่อเปิดหรือปิดเสียง
        if self.sound_on:
            print("Audio is now Off")
        else:
            print("Audio is now On")

    def go_back(self, instance):
        self.manager.current = 'menu'
        
class HowToPlayScreen(Screen):
    def __init__(self, **kwargs):
        super(HowToPlayScreen, self).__init__(**kwargs)
        how_to_play_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        how_to_play_label = Label(text="How to Play: [Your Instructions Here]")
        how_to_play_layout.add_widget(how_to_play_label)
        self.add_widget(how_to_play_layout)


class PlayScreen(Screen):
    def __init__(self, **kwargs):
        super(PlayScreen, self).__init__(**kwargs)
        play_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        play_layout.add_widget(Label(text="Enter your name:"))
        self.name_input = TextInput(hint_text="Enter Name", size_hint=(1, 0.2))
        play_layout.add_widget(self.name_input)
        confirm_button = Button(text="Confirm", size_hint=(1, 0.2))
        confirm_button.bind(on_press=self.confirm_name)
        play_layout.add_widget(confirm_button)
        self.add_widget(play_layout)

    def confirm_name(self, instance):
        name = self.name_input.text
        if name:
            print(f"Confirmed Name: {name}")
            self.manager.current = 'icon_selection'
        else:
            print("Please enter a name before confirming.")


class IconSelectionScreen(Screen):
    def __init__(self, **kwargs):
        super(IconSelectionScreen, self).__init__(**kwargs)
        icon_layout = GridLayout(cols=3, spacing=10, padding=10)
        icon_names = ['cat.png', 'icon2.png', 'icon3.png']
        for icon_name in icon_names:
            icon_button = Button(background_normal=icon_name, size_hint=(0.3, 0.3))
            icon_button.bind(on_press=self.select_icon)
            icon_layout.add_widget(icon_button)
        self.add_widget(icon_layout)

    def select_icon(self, instance):
        print(f"Selected icon: {instance.background_normal}")


class MenuApp(App):
    def build(self):
        self.screen_manager = ScreenManager()

        self.menu_screen = MenuScreen(name='menu')
        self.sound_setting_screen = SoundSettingScreen(name='sound_setting')
        self.how_to_play_screen = HowToPlayScreen(name='how_to_play')
        self.play_screen = PlayScreen(name='play')
        self.icon_selection_screen = IconSelectionScreen(name='icon_selection')

        self.screen_manager.add_widget(self.menu_screen)
        self.screen_manager.add_widget(self.sound_setting_screen)
        self.screen_manager.add_widget(self.how_to_play_screen)
        self.screen_manager.add_widget(self.play_screen)
        self.screen_manager.add_widget(self.icon_selection_screen)

        return self.screen_manager

if __name__ == "__main__":
    MenuApp().run()