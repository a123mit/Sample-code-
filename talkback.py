from tkinter.tix import Tk
import  pyttsx3 
import pypdf2
import tkinter as tk 
from tkinter.filedialog import * 

b = askopenfilename()
reader = pyPDF.pdffilereader(b)
pg= pdfreader.numpages

for num in range (0, pages):
    pg = pdfreader.getpage(num)
    text=pg.extractText()
    play= pyttsx3.init()
    play.say(text)
    play.runandwait()