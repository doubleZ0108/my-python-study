import speech_recognition as sr

r = sr.Recognizer()

# Working with Microphones
mic = sr.Microphone()
with mic as source:
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)        # 直到检测到静音时自动停止
# r.recognize_sphinx(audio)
print('The statement you said is {' + r.recognize_sphinx(audio) + '}')
