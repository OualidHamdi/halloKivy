from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (300, 500)

screen_helper = """
Screen:
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'Demo'
            left_action_items: [["menu",lambda x: app.navigation_draw()]]
            right_action_items: [["clock",lambda x: app.navigation_draw()]]
            elevayion: 8
        MDLabel:
            text: 'Hello Word'
            halign: 'center'
            
        MDBottomAppBar:
            MDToolbar:
                left_action_items: [["coffee",lambda x: app.navigation_draw()]]
                mode: 'end'
                type: 'bottom"
                on_action_button: app.navigation_draw()
             
"""


class DemoApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = 'Red'
        screen = Builder.load_string(screen_helper)
        return screen


DemoApp().run()
