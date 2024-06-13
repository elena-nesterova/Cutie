import os

from gtts import gTTS
import random
from playsound import playsound

import give_reaction


class give_reaction_text_to_speech(give_reaction.give_reaction):

    __lang = 'ru'

    def __init__(self, lang):
        self.__lang = lang

    def give_reaction(self, source):

        # Создание объекта gTTS с текстом
        print(source)
        speech = gTTS(source, lang=self.__lang)

        # Сохранение в файл и воспроизведение
        r = random.randint(1, 100000)
        audio_file = "audio_" + str(r) + ".mp3"

        speech.save(audio_file)
        playsound(audio_file)
        # os.system(audio_file)
        os.remove(audio_file)


def give_reaction_text_to_speech_f(reacties, lang):
    # Создание объекта gTTS с текстом
    reaction = random.choice(reacties)
    print(reaction)
    speech = gTTS(reaction, lang=lang)
    # Сохранение в файл и воспроизведение
    r = random.randint(1,100000)
    audio_file = "audio_" + str(r) + ".mp3"
    speech.save(audio_file)
    playsound(audio_file)
    os.remove(audio_file)
    #os.system("start example_speech.mp3")
