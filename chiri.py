import pyttsx3
import speech_recognition as sr
def take_commands():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening')
        r.pause_threshold = 0.7
        audio = r.listen(source)
        try:
            print("Recognizing")
            Query = r.recognize_google(audio)
            print("the query is printed='", Query, "'")
        except Exception as e:
            print(e)
            print("Say that again sir")
            return "None"
    return Query 
def Speak(audio):
    engine = pyttsx3.init()
    engine.say(audio)
    engine.runAndWait()

if __name__ == '__main__':
    while True:
        command = take_commands()
        if "exit" in command:
            Speak("Sure sir! as your wish")
            break
        if "insta" in command:
            Speak("Haii... Welcome to python projects")
        if "learn" in command:
            Speak("Learn to code, play with code")
        if "code" in command:
            Speak("Get you code from here")
