from kivy.config import Config
Config.set('graphics', 'position', 'custom')
Config.set('graphics', 'left', 0)
Config.set('graphics', 'top',  0)
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.core.window import Window
Window.size = (1920, 1080)
from random import choice
import pygame
from pygame.mixer import music

WORDS = ["YOU'RE", "A", "GAY", "APE"]
COLOURS = ["ff0099", "00ffff", "00ff00", "ffff00", "ff0000"]

pygame.init()

kv = """
<ColourLabel>:
    text: app.text
    font_size: 225
    markup: True
BoxLayout:
    orientation: "vertical"
    BoxLayout:
        orientation: "vertical"
        id: box
"""


class ColourLabel(Label):
    pass


class GayApe(App):
    text = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.i = 0

    def build(self):
        self.root = Builder.load_string(kv)
        self.begin()
        return self.root

    def on_stop(self):
        self.interval_flash.cancel()

    def begin(self):
        music.load('hamster_dance.wav')
        music.play(-1)
        box = self.root.ids.box
        box.clear_widgets()
        label = ColourLabel()
        box.add_widget(label)
        Clock.schedule_once(self.flash, 0)
        self.interval_flash = Clock.schedule_interval(self.flash, 0.45)

    def flash(self, *args):
        self.text = f'[b][color={choice(COLOURS)}]{WORDS[self.i]}[/color][/b]'
        self.i += 1
        if self.i >= len(WORDS):
            self.i = 0


if __name__ == '__main__':
    GayApe().run()
