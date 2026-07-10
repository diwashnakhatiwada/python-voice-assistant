import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import cv2
from playsound import playsound

# ==============================
# Voice Engine
# ==============================
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)   # Male voice
# engine.setProperty('voice', voices[1].id) # Female voice (Uncomment if available)

engine.setProperty("rate", 170)

# ==============================
# Speak Function
# ==============================
def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

# ==============================
# Speech Recognition
# ==============================
recognizer = sr.Recognizer()

def listen():
    with sr.Microphone() as source:

        print("\nListening...")

        recognizer.adjust_for_ambient_noise(source, duration=1)

        try:
            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=8
            )

            command = recognizer.recognize_google(audio)

            command = command.lower()

            print("You:", command)

            return command

        except sr.UnknownValueError:
            print("Could not understand.")
            return ""

        except sr.WaitTimeoutError:
            return ""

        except Exception as e:
            print(e)
            return ""

# ==============================
# Assistant Ready
# ==============================
speak("Hello. I am your Python Voice Assistant. How can I help you?")

# ==============================
# Main Loop
# ==============================
while True:

    command = listen()

    # ------------------------------
    # Greeting
    # ------------------------------
    if "hi" in command or "hello" in command:

        speak("Hello Diwashna. Nice to meet you.")

    # ------------------------------
    # How are you
    # ------------------------------
    elif "how are you" in command:

        speak("I am doing great. Thank you for asking.")

    # ------------------------------
    # Assistant Name
    # ------------------------------
    elif "your name" in command:

        speak("I am your Python Voice Assistant.")

    # ------------------------------
    # Date
    # ------------------------------
    elif "today" in command and "date" in command:

        today = datetime.datetime.now().strftime("%d %B %Y")

        speak("Today's date is")

        speak(today)

    # ------------------------------
    # Time
    # ------------------------------
    elif "time" in command:

        current = datetime.datetime.now().strftime("%I:%M %p")

        speak("Current time is")

        speak(current)

    # ------------------------------
    # Camera
    # ------------------------------
    elif "camera" in command:

        speak("Opening camera.")

        cap = cv2.VideoCapture(0)

        while True:

            ret, frame = cap.read()

            if not ret:
                break

            cv2.imshow("Camera", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()

        cv2.destroyAllWindows()

    # ------------------------------
    # Play Music
    # ------------------------------
    elif "play music" in command or "play song" in command:

        speak("Playing music.")

        try:
            playsound("music.mp3")
        except:
            speak("Music file not found.")

    # ------------------------------
    # Google
    # ------------------------------
    elif "open google" in command:

        speak("Opening Google.")

        webbrowser.open("https://www.google.com")

    # ------------------------------
    # YouTube
    # ------------------------------
    elif "open youtube" in command:

        speak("Opening YouTube.")

        webbrowser.open("https://www.youtube.com")

    # ------------------------------
    # Introduce Diwashna
    # ------------------------------
    elif "introduce" in command:

        intro = """
        Diwashna Khatiwada is a Computer Science Engineering student at Aditya University,
        Andhra Pradesh, India.

        She is originally from Nepal and is currently pursuing her Bachelor of Technology.

        She is passionate about Artificial Intelligence, Cyber Security,
        Data Analysis, Computer Networks, and Web Development.

        She has developed projects such as a Smart Factory Monitoring System,
        a Shopping Application, and a Personal Portfolio Website.

        Her technical skills include Python, Java, HTML, CSS, JavaScript,
        SQL, and Machine Learning fundamentals.

        Apart from academics, she enjoys dancing,
        voice expression, reading books, and learning new technologies.

        Her career goal is to become a successful software engineer
        and contribute to innovative technologies around the world.
        """

        speak(intro)

    # ------------------------------
    # Education
    # ------------------------------
    elif "education" in command:

        speak("Diwashna is pursuing a Bachelor of Technology in Computer Science Engineering at Aditya University, Andhra Pradesh, India.")

    # ------------------------------
    # Skills
    # ------------------------------
    elif "skills" in command:

        speak("Her skills include Python, Java, HTML, CSS, JavaScript, SQL, Artificial Intelligence, Cyber Security, Computer Networks, and Web Development.")

    # ------------------------------
    # Projects
    # ------------------------------
    elif "projects" in command:

        speak("She has completed a Smart Factory Monitoring System, a Shopping Application, and a Personal Portfolio Website.")

    # ------------------------------
    # Country
    # ------------------------------
    elif "where is diwashna from" in command:

        speak("Diwashna is originally from Nepal and is currently studying in India.")

    # ------------------------------
    # Goal
    # ------------------------------
    elif "goal" in command or "career" in command:

        speak("Her goal is to become a successful software engineer specializing in Artificial Intelligence and Cyber Security.")

    # ------------------------------
    # Exit
    # ------------------------------
    elif "exit" in command or "stop" in command or "goodbye" in command:

        speak("Goodbye Diwashna. Have a wonderful day.")

        break

    # ------------------------------
    # Unknown Command
    # ------------------------------
    elif command != "":

        speak("Sorry, I did not understand that command.")