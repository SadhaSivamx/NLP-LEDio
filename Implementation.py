from Base import MakePredictions
import speech_recognition as sr
import pyttsx3

def text_to_speech(text):
    # Initialize the TTS engine
    engine = pyttsx3.init()

    # Set properties (optional)
    # You can set properties like rate (speed) and volume
    # engine.setProperty('rate', 150)  # Speed (words per minute)
    # engine.setProperty('volume', 0.9)  # Volume (0.0 to 1.0)

    # Convert the text to speech
    engine.say(text)

    # Wait for the speech to finish
    engine.runAndWait()

def Get_Input():
    text_to_speech("Listening...")
    x=input("Listening... : ")
    text_to_speech(MakePredictions(x))
if __name__ == "__main__":
    while True:
        Get_Input()
