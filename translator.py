# pip install googletrans==3.1.0a0
# pip install Speech_Recognition
# pip install PyAudio
# pip install gTTs
# pip install playsound==1.2.2

import googletrans
import speech_recognition
import gtts
import  playsound


recognizer = speech_recognition.Recognizer()
with speech_recognition.Microphone() as source:
    print (" speak Now")
    voice  = recognizer.listen(source)
    text = recognizer.recognize_google(voice,language ="hi")
    print(text)



    
translator = googletrans.Translator()
translation = translator.translate(text,dest="en")
print(translation.text)
converted_audio = gtts.gTTs(translation.text,lang="en")
converted_audio.save("hello.mp3")
playsound.playsound("hello.mp3")

#print(googletrans.LANGUAGES)
