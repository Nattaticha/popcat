import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.core.audio import SoundLoader  # เพิ่มบรรทัดนี้
import os
from kivy.core.window import Window
from kivy.uix.widget import Widget 


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
        self.play_button.background_color = (0, 1, 0, 1)
        self.play_button.color = (1, 1, 1, 1)
        layout.add_widget(self.play_button)

        setting_button = Button(text="Setting",font_size= 25, size_hint=(1, 0.2))
        setting_button.bind(on_press=self.open_settings)
        setting_button.background_color = (0.5, 0.5, 0.5, 1)
        setting_button.color = (1, 1, 1, 1)
        layout.add_widget(setting_button)

        how_to_play_button = Button(text="How to Play ?", font_size= 25,size_hint=(1, 0.2))
        how_to_play_button.bind(on_press=self.open_how_to_play)
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
        self.sound_on = True

        backgroundImage = 'setting.png'
        self.setting = Button(text='Sound Setting', font_size=100, size_hint=(1,None), size=(1200, 400), color=(0,0,0,1))
        self.setting.background_normal = backgroundImage

        sound_layout = BoxLayout(orientation='vertical', padding=10, spacing=20)
        sound_layout.add_widget(self.setting)

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
        
        if self.sound_on:
            print("Audio is now On")
            if not App.get_running_app().background_music.state == 'play':
                App.get_running_app().background_music.play()
        else:
            print("Audio is now Off")
            if App.get_running_app().background_music.state == 'play':
                App.get_running_app().background_music.stop()

    def go_back(self, instance):
        self.manager.current = 'menu'

class HowToPlayScreen(Screen):
    def __init__(self, **kwargs):
        super(HowToPlayScreen, self).__init__(**kwargs)
        how_to_play_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        backgroundImage = 'how_to_play.png'

        self.how_to_play = Button()
        self.how_to_play.background_normal = backgroundImage
        self.add_widget(self.how_to_play)

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
        self.playlayout.color = (0, 0, 0, 1)

        play_layout.add_widget(self.playlayout)

        play_layout.add_widget(Label(text="Enter your meaw name :", font_size=25))
        self.name_input = TextInput(hint_text="Enter Name", font_size=30,size_hint=(1, 1.5))
        play_layout.add_widget(self.name_input)

        confirm_button = Button(text="Confirm", size_hint=(1, 0.75))
        confirm_button.bind(on_press=self.confirm_name)

        confirm_button.background_color = (0, 1, 0, 1)
        confirm_button.color = (1, 1, 1, 1)

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

        backgroundImage = 'selection1.png'

        self.iconselection = Button()
        self.iconselection.background_normal = backgroundImage
        self.add_widget(self.iconselection)

        main_layout = BoxLayout(orientation='vertical', spacing=10, padding=10, size_hint=(1, 1))

        self.username_label = Label(text="Username: ", font_size=20, size_hint=(1, None), height=50)
        main_layout.add_widget(self.username_label)

        icon_layout = BoxLayout(orientation='horizontal', spacing=10, padding=10, size_hint=(1, 1))

        select_icon_label = Label(text="Select your icon", font_size=30, size_hint=(1, None), height=100)
        main_layout.add_widget(select_icon_label)

        image_path = os.path.join(os.path.dirname(__file__), 'iconcat1.png')
        self.icon_button1 = Button(size_hint=(None, None), size=(200, 200), background_normal=image_path)
        self.icon_button1.bind(on_press=self.select_icon)
        icon_layout.add_widget(self.icon_button1)
        

        image_path = os.path.join(os.path.dirname(__file__), 'iconcat2.png')
        self.icon_button2 = Button(size_hint=(None, None), size=(200, 200), background_normal=image_path)
        self.icon_button2.bind(on_press=self.select_icon02)
        icon_layout.add_widget(self.icon_button2)

        image_path = os.path.join(os.path.dirname(__file__), 'iconcat3.png')
        self.icon_button3 = Button(size_hint=(None, None), size=(200, 200), background_normal=image_path)
        self.icon_button3.bind(on_press=self.select_icon03)
        icon_layout.add_widget(self.icon_button3)


        image_path = os.path.join(os.path.dirname(__file__), 'iconcat4.png')
        self.icon_button4 = Button(size_hint=(None, None), size=(200, 200), background_normal=image_path)
        self.icon_button4.bind(on_press=self.select_icon04)
        icon_layout.add_widget(self.icon_button4)



        self.selected_icon_path = None
        main_layout.add_widget(icon_layout)
        main_layout.add_widget(Widget())  
        self.add_widget(main_layout)

    def set_player_name(self, name):
        self.username_label.text = f"Player: {name}"
        self.username_label.font_size = 30

    def select_icon(self, instance):
        selected_icon_path = instance.background_normal
        print(f"Selected icon: {selected_icon_path}")
        self.set_selected_icon_path(selected_icon_path)
        
        # เพิ่มโค้ดต่อไปนี้เพื่อแสดงหน้า CatScreen เมื่อกดปุ่ม iconcat1.png
        if selected_icon_path.endswith('iconcat1.png'):
            self.manager.current = 'cat_screen'
        else:
            self.CatScreen()


    def set_selected_icon_path(self, selected_icon_path):
        self.selected_icon_path = selected_icon_path

    def select_icon02(self, instance):
        selected_icon_path = instance.background_normal
        print(f"Selected icon: {selected_icon_path}")
        self.set_selected_icon_path(selected_icon_path)
        
        # เพิ่มโค้ดต่อไปนี้เพื่อแสดงหน้า CatScreen02 เมื่อกดปุ่ม iconcat2.png
        if selected_icon_path.endswith('iconcat2.png'):
            self.manager.current = 'cat_screen02'
        else:
            self.manager.current = 'cat_screen'

    def select_icon03(self, instance):
            selected_icon_path = instance.background_normal
            print(f"Selected icon: {selected_icon_path}")
            self.set_selected_icon_path(selected_icon_path)
            
            # เพิ่มโค้ดต่อไปนี้เพื่อแสดงหน้า CatScreen02 เมื่อกดปุ่ม iconcat2.png
            if selected_icon_path.endswith('iconcat3.png'):
                self.manager.current = 'cat_screen03'
            else:
                self.manager.current = 'cat_screen'

    def select_icon04(self, instance):
            selected_icon_path = instance.background_normal
            print(f"Selected icon: {selected_icon_path}")
            self.set_selected_icon_path(selected_icon_path)
            
            # เพิ่มโค้ดต่อไปนี้เพื่อแสดงหน้า CatScreen02 เมื่อกดปุ่ม iconcat2.png
            if selected_icon_path.endswith('iconcat4.png'):
                self.manager.current = 'cat_screen04'
            else:
                self.manager.current = 'cat_screen'


class CatScreen(Screen):
    def __init__(self, **kwargs):
        super(CatScreen, self).__init__(**kwargs)
        self.cat_button = Button(background_normal='iconcat1.png', on_press=self.on_cat_button_press)
        self.add_widget(self.cat_button)
        self.current_image = 1  # 1 หมายถึงรูปแมวที่ 1

        
    def on_cat_button_press(self, instance):
        # ทำงานเมื่อปุ่มถูกกด
        if self.current_image == 1:
            self.cat_button.background_normal = 'iconcat1.png'
            self.current_image = 2
        else:
            self.cat_button.background_normal = 'iconcat1_1.png'
            self.current_image = 1
        
        # Clock.schedule_interval(self.change_cat_image, 1)

    def change_cat_image(self, dt):
        # เปลี่ยนรูปแมวทุก 1000 มิลลิวินาที
        if self.current_image == 1:
            self.cat_button.background_normal = 'iconcat2.png'
            self.current_image = 2
        else:
            self.cat_button.background_normal = 'iconcat1.png'
            self.current_image = 1

class CatScreen02(Screen):
    def __init__(self, **kwargs):
        super(CatScreen02, self).__init__(**kwargs)
        self.cat_button = Button(background_normal='iconcat2.png', on_press=self.on_cat_button_press)
        self.add_widget(self.cat_button)
        self.current_image = 1  # 1 หมายถึงรูปแมวที่ 1

        
    def on_cat_button_press(self, instance):
        # ทำงานเมื่อปุ่มถูกกด
        if self.current_image == 1:
            self.cat_button.background_normal = 'iconcat2.png'
            self.current_image = 2
        else:
            self.cat_button.background_normal = 'iconcat1.png'
            self.current_image = 1
        

    def change_cat_image(self, dt):
        # เปลี่ยนรูปแมวทุก 1000 มิลลิวินาที
        if self.current_image == 1:
            self.cat_button.background_normal = 'iconcat2.png'
            self.current_image = 2
        else:
            self.cat_button.background_normal = 'iconcat1.png'
            self.current_image = 1

class CatScreen03(Screen):
    def __init__(self, **kwargs):
        super(CatScreen03, self).__init__(**kwargs)
        self.cat_button = Button(background_normal='iconcat3.png', on_press=self.on_cat_button_press)
        self.add_widget(self.cat_button)
        self.current_image = 1  # 1 หมายถึงรูปแมวที่ 1

        
    def on_cat_button_press(self, instance):
        # ทำงานเมื่อปุ่มถูกกด
        if self.current_image == 1:
            self.cat_button.background_normal = 'iconcat2.png'
            self.current_image = 2
        else:
            self.cat_button.background_normal = 'iconcat1.png'
            self.current_image = 1
        

    def change_cat_image(self, dt):
        # เปลี่ยนรูปแมวทุก 1000 มิลลิวินาที
        if self.current_image == 1:
            self.cat_button.background_normal = 'iconcat2.png'
            self.current_image = 2
        else:
            self.cat_button.background_normal = 'iconcat1.png'
            self.current_image = 1

class CatScreen04(Screen):
    def __init__(self, **kwargs):
        super(CatScreen04, self).__init__(**kwargs)
        self.cat_button = Button(background_normal='iconcat4.png', on_press=self.on_cat_button_press)
        self.add_widget(self.cat_button)
        self.current_image = 1  # 1 หมายถึงรูปแมวที่ 1

        
    def on_cat_button_press(self, instance):
        # ทำงานเมื่อปุ่มถูกกด
        if self.current_image == 1:
            self.cat_button.background_normal = 'iconcat2.png'
            self.current_image = 2
        else:
            self.cat_button.background_normal = 'iconcat1.png'
            self.current_image = 1
        

    def change_cat_image(self, dt):
        # เปลี่ยนรูปแมวทุก 1000 มิลลิวินาที
        if self.current_image == 1:
            self.cat_button.background_normal = 'iconcat2.png'
            self.current_image = 2
        else:
            self.cat_button.background_normal = 'iconcat1.png'
            self.current_image = 1



class CatApp(App):
    def build(self):
        sm = ScreenManager()
        cat_screen = CatScreen(name='cat_screen')
        cat_screen02 = CatScreen02(name='cat_screen02')
        cat_screen03 = CatScreen03(name='cat_screen03')
        cat_screen04 = CatScreen04(name='cat_screen04')

        sm.add_widget(cat_screen)
        sm.add_widget(cat_screen02)
        sm.add_widget(cat_screen03)
        sm.add_widget(cat_screen04)
        return sm
                
class SelectedIconScreen(Screen):
    def __init__(self, icon_path, **kwargs):
        super(SelectedIconScreen, self).__init__(**kwargs)
        selected_icon = Image(source=icon_path, size_hint=(1, 1), allow_stretch=True)
        self.add_widget(selected_icon)

class IconButton(Button):
    def __init__(self, image, **kwargs):
        super(IconButton, self).__init__(**kwargs)
        self.add_widget(image)
        self.image = image  

class MenuApp(App):
    def build(self):
        self.screen_manager = ScreenManager()

        self.menu_screen = MenuScreen(name='menu')
        self.sound_setting_screen = SoundSettingScreen(name='sound_setting')
        self.how_to_play_screen = HowToPlayScreen(name='how_to_play')
        self.play_screen = PlayScreen(name='play')
        self.icon_selection_screen = IconSelectionScreen(name='icon_selection')

        self.cat_screen = CatScreen(name='cat_screen')
        self.cat_screen02 = CatScreen02(name='cat_screen02')
        self.cat_screen03 = CatScreen03(name='cat_screen03')
        self.cat_screen04 = CatScreen04(name='cat_screen04')
        
        self.screen_manager.add_widget(self.menu_screen)
        self.screen_manager.add_widget(self.sound_setting_screen)
        self.screen_manager.add_widget(self.how_to_play_screen)
        self.screen_manager.add_widget(self.play_screen)
        self.screen_manager.add_widget(self.icon_selection_screen)
        self.screen_manager.add_widget(self.cat_screen)
        self.screen_manager.add_widget(self.cat_screen02)
        self.screen_manager.add_widget(self.cat_screen03)
        self.screen_manager.add_widget(self.cat_screen04)

        self.background_music = SoundLoader.load('C:\\Users\\ASUS\\Desktop\\241-152\\learn_kivy\\venv\\kivyproject\\catsong.mp3')  
        if self.background_music:
            self.background_music.play()

        return self.screen_manager

if __name__ == "__main__":
    MenuApp().run()
