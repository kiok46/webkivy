import os

import kivy.app
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.core.audio import SoundLoader

Builder.load_string("""
<HelloWorldScreen>:
    BoxLayout:
        Button:
            text: 'Play sound'
            on_press:
                self.parent.parent.play_sound()
        Button:
            text: 'Quit'
            on_press:
                self.parent.parent.quit()

""")


class HelloWorldScreen(Screen):

    def play_sound(self):
        """Play a sample sound file to give satisfaction to the user."""
        # http://soundbible.com/2103-1-Person-Cheering.html
        my_path = os.path.dirname(__file__)
        sound_path = os.path.join(my_path, 'yay.mp3')
        sound = SoundLoader.load(sound_path)
        sound.play()

    def quit(self):
        """Switch back to the loader screen."""
        app = kivy.app.App.get_running_app()
        landing_screen = app.reset_landing_screen()
        self.manager.switch_to(landing_screen)

def run():
    return HelloWorldScreen()