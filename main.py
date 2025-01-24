import streamlit as st
from PyPDF2 import PdfReader
from gtts import gTTS
import os

# Function to convert text to speech
def text_to_speech(text):
    tts = gTTS(text)
    file_path = "temp_audio.mp3"
    tts.save(file_path)  # Save the file temporarily
    return file_path

# Function to read PDF content
def extract_text_from_pdf(pdf_file):
    pdf_reader = PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

# Streamlit app
st.title("PDF to Audio Reader")
st.markdown("Upload a PDF file to convert it to audio.")

# File upload
pdf_file = st.file_uploader("Upload PDF", type="pdf")

if pdf_file:
    # Extract text from the PDF
    text = extract_text_from_pdf(pdf_file)
    
    # If text is found in the PDF
    if text:
        st.write("Here is the extracted text from the PDF:")
        st.write(text)
        
        # Convert the text to audio
        audio_file_path = text_to_speech(text)
        
        # Play audio
        with open(audio_file_path, "rb") as f:
            audio_bytes = f.read()
            st.audio(audio_bytes, format="audio/mp3")
    else:
        st.write("Could not extract text from the PDF.")

