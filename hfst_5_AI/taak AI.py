#importing modules
import tkinter as tk
from translate import Translator
from tkinter import filedialog

tekst = "Ik ben Menno en ik ben dom."

# initializing window
Screen = tk.Tk()
Screen.title("vertalen")

InputLanguageChoice = tk.StringVar()
TranslateLanguageChoice = tk.StringVar()

#tuple for choosing languages
LanguageChoices = {'Hausa','Bengali','Hindi','Urdu','Bulgarian','Chinese','Czech','Danish','Dutch','English','Estonian','Finnish','French','German','Greek','Hungarian','Indonesian','Italian','Japanese','Korean','Latvian','Lithuanian','Norwegian','Polish','Portuguese','Romanian','Russian','Slovak','Slovenian','Spanish','Swedish','Turkish','Ukrainian','Arabic','latin'}
InputLanguageChoice.set('Dutch')
TranslateLanguageChoice.set('Hindi')

def Translate():
    translator = Translator(from_lang= InputLanguageChoice.get(),to_lang=TranslateLanguageChoice.get())
    Translation = translator.translate(tekst)
    tk.messagebox.showwarning("vertaling",Translation)

#choice for input language
InputLanguageChoiceMenu = tk.OptionMenu(Screen,InputLanguageChoice,*LanguageChoices)
tk.Label(Screen,text="Choose a Language").grid(row=0,column=1)
InputLanguageChoiceMenu.grid(row=1,column=1)

#choice in which the language is to be translated
NewLanguageChoiceMenu = tk.OptionMenu(Screen,TranslateLanguageChoice,*LanguageChoices)
tk.Label(Screen,text="Translated Language").grid(row=0,column=2)
NewLanguageChoiceMenu.grid(row=1,column=2)

#Button for calling function
B = tk.Button(Screen,text="Translate",command=Translate, relief = tk.GROOVE).grid(row=3,column=1,columnspan = 3)

tk.mainloop()