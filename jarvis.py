import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize voice engine
engine = pyttsx3.init()

def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()

# Listen function
def listen():

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")

        recognizer.adjust_for_ambient_noise(source)

        audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)

    try:
        command = recognizer.recognize_google(audio)

        print("You said:", command)

        return command.lower()

    except:
        return ""

# Start Jarvis
speak("Hello Aditya, I am Jarvis.")

while True:

    command = listen()

    # Open YouTube
    if "youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")

    # Open Google
    elif "google" in command:
        speak("Opening Google")
        webbrowser.open("https://google.com")

    # Tell time
    elif "time" in command:

        time = datetime.datetime.now().strftime("%I:%M %p")

        speak(f"The time is {time}")

    # Stop Jarvis
    elif "stop" in command or "exit" in command:

        speak("Goodbye")

        break