from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

# DO NOT MODIFY
Window.size = (450, 900)

# GOING TO MODIFY
class Menu(Screen):
    def go_game(self, *args):
        self.manager.current = "game"

    def go_settings(self, *args):
        self.manager.current = "settings"

    def exit_app(self, *args):
        app.stop()

class Settings(Screen):
    def go_menu(self, *args):
        self.manager.current = "menu"

class Game(Screen):
    def go_menu(self, *args):
        self.manager.current = "menu"

# ========================================================

# DO NOT MODIFY
class ClickerApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Menu(name="menu"))
        sm.add_widget(Game(name="game"))
        sm.add_widget(Settings(name="settings"))
        return sm

app = ClickerApp()
app.run()