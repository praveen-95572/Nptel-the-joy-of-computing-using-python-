import speech_recognition as sr
AUDIO_FILE="sample.wav"

r=sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    audio=r.record(source)
try:
    print("Audio file contains:")
    print(r.recognize_google(audio))
except sr.UnknownValueError:
    print("Google search could not understand audio")
except sr.RequestError:
    print("couldn't get the results from Google Speech Recognition")
