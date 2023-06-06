from kivy.lang.builder import Builder
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config
from kivy.core.window import Window

Config.set('graphics', 'width', '950')
Config.set('graphics', 'height', '950')
Window.clearcolor = (0.205, 0.205, 0.205)  # 343434


class dotDesktopUI(GridLayout):
    pass


class DotDesktopCreateApp(App):
    title = "Мастер Создания .Desktop"

    def build(self):
        return dotDesktopUI()


Builder.load_file('UI-Markup.kv')
dApp = DotDesktopCreateApp()
dApp.run()
