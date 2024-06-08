import speech_recognition as sr
import pyttsx3

# Initialize recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

while True:
    try:
        with sr.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            print("Listening...")
            audio = recognizer.listen(mic)
            
            # Recognize speech using Google Web Speech API
            text = recognizer.recognize_google(audio)
            text = text.lower()
            
            print(f"Recognized: {text}")
            
            # Optional: Use text-to-speech to read back the recognized text
            engine.say(f"You said: {text}")
            engine.runAndWait()

    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        recognizer = sr.Recognizer()
        continue
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        break
