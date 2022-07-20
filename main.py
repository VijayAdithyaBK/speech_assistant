import speech_recognition as sr
import webbrowser
import time
import random
from playsound import playsound
import os
from gtts import gTTS
from time import ctime


r = sr.Recognizer()

def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            guruji_speaks(ask)
        '''
        `Recognizer` r listens to the source(microphone)
        using the `listen()` and stores the audio clip in var `audio`
        '''
        audio = r.listen(source)
        voice_data = ''
        '''
        `Recognizer` r uses the api `recognize_google()`
        to convert/store the audio into var `voice_data`
        '''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            guruji_speaks('Sorry, did not catch that')
        except sr.RequestError:
            guruji_speaks('Sorry, severs are down')
        return voice_data


def guruji_speaks(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 10000000)
    audio_file = 'audio-'+ str(r) + '.mp3'
    tts.save(audio_file)
    playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

def respond(voice_data):
    if 'what is your name' in voice_data:
        guruji_speaks('I am Guruji')
    if 'what is the time' in voice_data:
        guruji_speaks('Time now is ' + str(ctime()))
    if 'search' in voice_data:
        search = record_audio('what do you want to search for')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        guruji_speaks('Here is what I found for ' + search)
    if 'find location' in voice_data:
        location = record_audio('which location')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        guruji_speaks('Here is the location ' + location)
    if 'exit' or 'bye' in  voice_data:
        guruji_speaks('bye!')
        exit()

time.sleep(1)
guruji_speaks('I am listening..')
while 1:
    voice_data = record_audio()
    # print your voice/command
    print(voice_data)
    respond(voice_data)
