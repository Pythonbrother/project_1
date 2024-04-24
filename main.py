from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from plyer import gps
from kivy.clock import Clock, mainthread
from kivy.uix.popup import Popup
from kivy.uix.label import Label

class GPS_Access(App):
    pass

class APP_Widget(BoxLayout):
    content = ObjectProperty()

    def show_current_location(self):
        try:
            gps.configure(on_location=self.on_location)
            gps.start()
        except NotImplementedError:
            popup = Popup(title="GPS Error",content=Label(text="GPS support is not implemented on your platform")).open()
        Clock.schedule_once(lambda d: popup.dismiss(), 3)

    @mainthread
    def on_location(self, **kwargs):
        print(kwargs)
        self.content.text = kwargs
GPS_Access().run()