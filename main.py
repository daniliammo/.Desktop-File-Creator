from GenerateDotDesktop import DotDesktop
from ConfigWrite import WriteConfig
from kivy.lang.builder import Builder
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config
from kivy.core.window import Window
import os
Config.set('graphics', 'width', '950')
Config.set('graphics', 'height', '950')
Window.clearcolor = (0.205, 0.205, 0.205) #343434

WriteConfig.WriteCFG('Minecraft', 'Application', 'v1.16.5', 'Comment', 'Games', 'mine.png', 'minecraft.x86', False)
DotDesktop.Generate()
os.remove('config.json')


class dotDesktopUI(GridLayout):
    from ConfigWrite import WriteConfig
    from GenerateDotDesktop import DotDesktop


class DotDesktopCreateApp(App):

    title = "Мастер Создания .Desktop"

    def build(self):
        return dotDesktopUI()

Builder.load_file('UI-Markup.kv')
dApp = DotDesktopCreateApp()
dApp.run()
