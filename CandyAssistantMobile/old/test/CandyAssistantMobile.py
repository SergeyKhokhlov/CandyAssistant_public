from kivy.app import App
from kivy.uix.button import Button
import sys
import pyttsx3
import speech_recognition as sr
from kivy.uix.scatter import Scatter
from kivy.uix.floatlayout import FloatLayout
from kivy.config import Config

Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '550')

message_user = ""
sounds_and_voices = 1
message_candy = ""

speak_engine = pyttsx3.init()


def say(message):
    speak_engine.say(message)
    speak_engine.runAndWait()
    speak_engine.stop()


class CandyAssistantApp(App):
    def build(self):
        s = Scatter()
        fl = FloatLayout(size=(500, 500))
        s.add_widget(fl)
        fl.add_widget(Button(text='Candy',
                             font_size=30,
                             pos=(100, 50),
                             size_hint=(.4, .1),
                             on_press=self.commands_user))
        return s

    def commands_user(self, instance):
        global message_user
        global message_candy, sounds_and_voices
        try:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                r.pause_threshold = 1
                if sounds_and_voices == 1:
                    say('Я вас слушаю...')
                r.adjust_for_ambient_noise(source, duration=2)
                audio = r.listen(source)
            try:
                message_user = r.recognize_google(audio, language="ru-RU").lower()
            except sr.UnknownValueError:
                if sounds_and_voices == 1:
                    say("Я вас не поняла")
                    self.commands_user()
                elif sounds_and_voices == 2:
                    message_user = ""
                    for i in range(5):
                        say("")
        except OSError:
            say("Подключите микрофон, для корректной работы программы!")
            sys.exit()
        except sr.RequestError:
            say("Проверьте подключение к интернету")
            sys.exit()


if __name__ == "__main__":
    CandyAssistantApp().run()
