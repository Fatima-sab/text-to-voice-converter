import streamlit as st
from gtts import gTTS
import os

# Title of the app
st.title("Text to Speech Converter")

# Text input from the user
text_input = st.text_area("Enter text to convert to audio:")

# Language option
language = st.selectbox("Select language:", ["en", "es", "fr", "de", "it"])

# Button to convert text to audio
if st.button("Convert to Audio"):
    if text_input:
        # Create gTTS object
        tts = gTTS(text=text_input, lang=language, slow=False)
        
        # Save the audio file
        audio_file = "output_audio.mp3"
        tts.save(audio_file)

        # Inform the user
        st.success("Audio file generated successfully!")

        # Display the audio player
        st.audio(audio_file)
    else:
        st.warning("Please enter some text to convert.")

# Option to clear the input
if st.button("Clear"):
    st.text_area("Enter text to convert to audio:", value="", height=150)
