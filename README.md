# speech_assistant
Python Speech Assistant - Speech Assistant Documentation
The Speech Assistant is a Python script that allows users to interact with a voice-controlled assistant. It uses the SpeechRecognition library to capture and process voice input, and performs various actions based on user commands.

Prerequisites
Before using the Speech Assistant, make sure you have the following libraries installed:

speech_recognition
webbrowser
time
random
playsound
os
gtts (Google Text-to-Speech)
You can install these libraries using pip:

Copy code
pip install SpeechRecognition webbrowser playsound gtts
Usage
To use the Speech Assistant, follow these steps:

Import the required libraries:
python
Copy code
import speech_recognition as sr
import webbrowser
import time
import random
from playsound import playsound
import os
from gtts import gTTS
from time import ctime
Set up the speech recognizer:
python
Copy code
r = sr.Recognizer()
Define the record_audio function to capture voice input:
python
Copy code
def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            guruji_speaks(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            guruji_speaks('Sorry, did not catch that')
        except sr.RequestError:
            guruji_speaks('Sorry, servers are down')
        return voice_data
Define the guruji_speaks function to convert text to speech and play it:
python
Copy code
def guruji_speaks(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)
Define the respond function to perform actions based on user commands:
python
Copy code
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
    if 'exit' or 'bye' in voice_data:
        guruji_speaks('bye!')
        exit()
    if 'listen' in voice_data:
        rant = record_audio('Tell me what it is')
        if 'I am done' in rant:
            guruji_speaks('okay')
        else:
            rant = record_audio('continue')
Start the main loop of the assistant:
python
Copy code
time.sleep(1)
guruji_speaks('Ask Guruji what you need to know..')
while 1:
    voice_data = record_audio()
    respond(voice_data)
Run the script and interact with the assistant using voice commands.
Functionality
The Speech Assistant provides the following functionality:

Responds to the command "What is your name" with the answer "I am Guruji".
Responds to the command "What is the time" with the current time.
Allows users to search the web by saying "search" followed by the search query.
Provides the ability to find locations on Google Maps by saying "find location" followed by the desired location.
Exits the program when the user says "exit" or "bye".
Can listen to user input by saying "listen" and performs actions based on the input.
Please note that the assistant requires an active internet connection for speech recognition and accessing web resources.

Customization
You can customize the assistant's responses and add additional functionality by modifying the respond function. You can extend the list of recognized voice commands and define corresponding actions accordingly.

Limitations
The Speech Assistant relies on internet connectivity for speech recognition and accessing web resources. Therefore, a stable internet connection is required for optimal functionality. Additionally, the assistant's performance may vary depending on the quality of the microphone and ambient noise levels during voice input.

It's also worth noting that the Speech Assistant is a basic implementation and may not support advanced features such as natural language processing or complex dialog management. Consider using more sophisticated speech recognition and natural language understanding frameworks for advanced use cases.

Disclaimer
The Speech Assistant is provided as-is without any warranty. The accuracy and reliability of the speech recognition and web search results may vary based on external factors beyond the control of the script. Use the assistant responsibly and in compliance with the terms of service of the utilized web resources.




