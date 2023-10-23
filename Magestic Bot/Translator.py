import random
import datetime
import webbrowser
import pyttsx3
import wikipedia
from pygame import mixer
import speech_recognition as sr
import pyaudio
import streamlit as st
import threading
import requests
from bs4 import BeautifulSoup
from googletrans import Translator

# Initialize the translator
translator = Translator()

with open('style1.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.title('Majestic Translater')

# ... (Your other code)
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
volume = engine.getProperty('volume')
engine.setProperty('volume', 10.0)
rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 30)

# Create the "Translate" button outside the while loop
translate_button = st.button('Translate')

def process_voice_input():
    global song_played
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Tell me something:")
        audio = r.listen(source)
        try:
            recognized_results = r.recognize_google(audio, show_all=True)
            if "alternative" in recognized_results:
                recognized_text = recognized_results["alternative"][0]["transcript"].lower()
            else:
                recognized_text = ""
            st.write("You said: " + recognized_text)
            return recognized_text
        except sr.UnknownValueError:
            st.write("Could not understand audio")
            return ""

# Function to process voice input and perform translation
def process_and_translate_voice_input():
    if translate_button:  # Check if the "Translate" button is clicked
        recognized_text = process_voice_input()
    
        # Print the original English text
        st.write("You said (in English): " + recognized_text)
        
        # Translate the English text to Hindi
        translated_text = translator.translate(recognized_text, src='en', dest='hi').text
        
        # Print the translated text in Hindi
        
        st.write("Translated text (in Hindi): " + translated_text)
        


while True:
    process_and_translate_voice_input()
