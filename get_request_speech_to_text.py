import speech_recognition as sr

import get_request


class get_request_speech_to_text(get_request.get_request):

    __lang = ""
    __credentials = ""

    def __init__(self, lang, google_cloud_credentials=""):
        self.__lang = lang
        self.__credentials = google_cloud_credentials


    def get_request(self):
        return self.__speech_to_text()

    def __speech_to_text(self):
        # create object Recognizer
        recognizer = sr.Recognizer()
        # Recording audio from microphone
        with sr.Microphone() as source:
            print("Waiting for speech:")
            audio = recognizer.listen(source)
            # recognize
            try:
                if len(self.__credentials) > 0:
                    text = recognizer.recognize_google_cloud(audio, language=self.__lang, credentials_json=self.__credentials)
                else:
                    text = recognizer.recognize_google(audio, language=self.__lang)
                print("Recognized text:", text)
                return text
            except sr.UnknownValueError:
                print("Speesh does not recognized")
            except sr.RequestError as e:
                print(f"Error: {e}")

            return ""