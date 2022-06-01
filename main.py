# Import the gTTS module for text
# to speech conversion
from gtts import gTTS

# This module is imported so that we can
# play the converted audio

from playsound import playsound
import pyttsx3
import pdfplumber
import PyPDF2
operation=input("choose t for change text to speech, choose p for change pdf to speech:")
if operation=="t":
    #enter the text which is converting into speech
    text_val = input("enter the text:")

    # Here are converting in English Language
    language = 'en'

    # Passing the text and language to the engine,
    # here we have assign slow=False. Which denotes
    # the module that the transformed audio should
    # have a high speed
    obj = gTTS(text=text_val, lang=language, slow=False)

    # Here we are saving the transformed audio in a mp3 file named
    # exam.mp3
    obj.save("exam.mp3")

    # Play the exam.mp3 file
    playsound("exam.mp3")
elif operation=="p":
    file = input("enter file location:")

    #Creating a PDF File Object
    pdfFileObj = open(file, 'rb')

    # creating a pdf reader object
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    #Get the number of pages
    pages =pdfReader.numPages
    pdf_speaker=pyttsx3.init()
    choose_page=pdfReader.getPage(0)

    pdf_text=choose_page.extractText()
    pdf_speaker.say(pdf_text)
    pdf_speaker.runAndWait()
else:
    print("choose any operation")