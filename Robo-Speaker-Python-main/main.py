import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

if __name__ == '__main__':
    print("🤖 Welcome to ROBO SPEAKER by Vignesh 🔊")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("Enter what you want me to speak: ")

        if user_input.strip().lower() == "exit":
            speak("Exiting ROBO SPEAKER. Goodbye!")
            print("👋 Exiting... Have a nice day!")
            break

        if user_input.strip() == "":
            print("⚠️ You didn't enter anything.")
            continue

        speak(user_input)
