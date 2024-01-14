import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
import os
from kivy.core.window import Window


class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super(MenuScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        backgroundImage = 'background1.png'
        self.game_name = Button(text='Pop Cat', font_size=100, size_hint=(1, None), size=(1200, 400))
        self.game_name.background_normal = backgroundImage
        layout.add_widget(self.game_name)

        self.play_button = Button(text="Play !", font_size= 25,size_hint=(1, 0.2))
        self.play_button.bind(on_press=self.switch_to_play_screen)
        # Fix here: Set background_color and color for the "Play" button
        self.play_button.background_color = (0, 1, 0, 1)
        self.play_button.color = (1, 1, 1, 1)
        layout.add_widget(self.play_button)

        setting_button = Button(text="Setting",font_size= 25, size_hint=(1, 0.2))
        setting_button.bind(on_press=self.open_settings)
        # Fix here: Set background_color and color for the "Setting" button
        setting_button.background_color = (0.5, 0.5, 0.5, 1)
        setting_button.color = (1, 1, 1, 1)
        layout.add_widget(setting_button)

        how_to_play_button = Button(text="How to Play ?", font_size= 25,size_hint=(1, 0.2))
        how_to_play_button.bind(on_press=self.open_how_to_play)
        # Fix here: Set background_color and color for the "How to Play" button
        how_to_play_button.background_color = (1, 0, 0, 1)
        how_to_play_button.color = (1, 1, 1, 1)
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

        backgroundImage = 'setting.png'
        self.setting = Button(text='Sound Setting', font_size=100, size_hint=(1,None), size=(1200, 400), color=(0,0,0,1))
        self.setting.background_normal = backgroundImage

        # Fix here: Create a new BoxLayout for sound_layout
        sound_layout = BoxLayout(orientation='vertical', padding=10, spacing=20)
        sound_layout.add_widget(self.setting)  # Add self.setting to sound_layout

        # # sound_label = Label(text="Sound Settings")
        # sound_layout.add_widget(sound_label)

        audio_button = Button(text="Audio On" if self.sound_on else "Audio Off", font_size=30,size_hint=(1, 3))
        audio_button.bind(on_press=self.toggle_audio)
        sound_layout.add_widget(audio_button)

        back_button = Button(text="Back",font_size=30, size_hint=(1, 2))
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
        
        backgroundImage = 'how_to_play.png'
        
        # Fix here: Create a new Button instance for how_to_play
        self.how_to_play = Button()
        self.how_to_play.background_normal = backgroundImage
        self.add_widget(self.how_to_play)  # Fix here: Use self instead of layout

        how_to_play_text = (
            " How to play Popcat?\n"
            " \n "
            " \n "
            " Popcat is pretty self-explanatory\n "
            " \n "
            " all you have to do is keep clicking incessantly on the cat's mouth.\n "
            " \n "
            " The cat will open and close its mouth with each click and make a 'popping' sound."
        )
        how_to_play_label = Label(text=how_to_play_text, font_size=25, color=(1, 0, 1, 1))
        how_to_play_layout.add_widget(how_to_play_label)

        # Fix here: Set background_color for the "Back" button
        back_button = Button(text="Back", size_hint=(1, 0.1), background_color=(1, 0.68, 1, 1))
        back_button.bind(on_press=self.go_back)
        how_to_play_layout.add_widget(back_button)

        self.add_widget(how_to_play_layout)

    def go_back(self, instance):
        self.manager.current = 'menu'

    

class EnterNameScreen(Screen):
    def __init__(self, **kwargs):
        super(EnterNameScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

class PlayScreen(Screen):
    def __init__(self, **kwargs):
        super(PlayScreen, self).__init__(**kwargs)
        play_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        backgroundImage = 'entername.png'
        self.playlayout = Button(text='Let play -w-', font_size=100, size_hint=(1, None), size=(1200, 400))
        self.playlayout.background_normal = backgroundImage

        # Fix here: Set color for the "Let PLAY" text
        self.playlayout.color = (0, 0, 0, 1)  # Black text

        play_layout.add_widget(self.playlayout)

        play_layout.add_widget(Label(text="Enter your meaw name :", font_size = 25))
        self.name_input = TextInput(hint_text="Enter Name", font_size = 30,size_hint=(1, 1.5))
        play_layout.add_widget(self.name_input)

        # Fix here: Change 'layout' to 'play_layout'
        confirm_button = Button(text="Confirm", size_hint=(1, 0.75))
        confirm_button.bind(on_press=self.confirm_name)

        # Fix here: Set background_color and color for the "Confirm" button
        confirm_button.background_color = (0, 1, 0, 1)  # Green background
        confirm_button.color = (1, 1, 1, 1)  # White text

        play_layout.add_widget(confirm_button)
        self.add_widget(play_layout)

    def confirm_name(self, instance):
        name = self.name_input.text
        if name:
            print(f"Confirmed Name: {name}")
            self.manager.get_screen('icon_selection').set_player_name(name)
            self.manager.current = 'icon_selection'
        else:
            print("Please enter a name before confirming.")

class IconSelectionScreen(Screen):
    def __init__(self, **kwargs):
        super(IconSelectionScreen, self).__init__(**kwargs)
        
        # Vertical BoxLayout to stack elements vertically
        main_layout = BoxLayout(orientation='vertical', spacing=10, padding=10, size_hint=(1, 1))

        # Label to display the username
        self.username_label = Label(text=" username: ", font_size=20, size_hint=(1, None), height=50)
        main_layout.add_widget(self.username_label)

        # Horizontal BoxLayout to center icon buttons
        icon_layout = BoxLayout(orientation='horizontal', spacing=10, padding=10, size_hint=(1, 1))

        # Set the main image for the first button
        image_path = os.path.join(os.path.dirname(__file__), 'iconcat4.png')
        self.icon_button1 = Button(size_hint=(None, None), size=(150, 150), background_normal=image_path)
        self.icon_button1.bind(on_press=self.select_icon)
        icon_layout.add_widget(self.icon_button1)

        # Set other buttons with placeholder images
        placeholder_names = ['iconcat1.png', 'iconcat2.png', 'iconcat3.png']
        for placeholder_name in placeholder_names:
            icon_button = Button(size_hint=(None, None), size=(150, 150), background_normal=placeholder_name)
            icon_button.bind(on_press=self.select_icon)
            icon_layout.add_widget(icon_button)

        main_layout.add_widget(icon_layout)
        self.add_widget(main_layout)

    def set_player_name(self, name):
        self.username_label.text = f" player: {name}"

    def select_icon(self, instance):
        selected_icon_path = instance.background_normal
        print(f"Selected icon: {selected_icon_path}")

class IconButton(Button):
    def __init__(self, image, **kwargs):
        super(IconButton, self).__init__(**kwargs)
        self.add_widget(image)
        self.image = image  # Store the Image widget for later access

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