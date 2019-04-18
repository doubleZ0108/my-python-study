import speech_recognition as sr

r = sr.Recognizer()

# Working with audio files
speech = sr.AudioFile('f1lcapae.wav')
with speech as source:
    r.adjust_for_ambient_noise(source, duration=0.5)    #减小噪音对识别的影响
    audio = r.record(source)

print(r.recognize_sphinx(audio))
