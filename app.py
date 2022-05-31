import pyttsx3
import speech_recognition
import datetime

def txt_to_speech():
    recognizer = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listining...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("recognizing...")
            data = recognizer.recognize_google(audio)
            print(data)
            return data
        except speech_recognition.UnknownValueError:
            print("Not Understand")

def speech_to_txt(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 130)
    engine.say(x)
    engine.runAndWait()

if __name__ == '__main__':
    data_2 = txt_to_speech()
    if "your name" in data_2:
        name = "my name is vikas and am 19 years old and i live in mohan garden new delhi"
        speech_to_txt(name)
    elif "time now" in data_2:
        time = datetime.datetime.now().strftime('%I%M%p')
        speech_to_txt(time)
    