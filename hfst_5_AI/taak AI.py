lijst = ['afrikaans', 'albanian', 'amharic', 'arabic', 'armenian', 'assamese', 'aymara', 'azerbaijani', 'bambara', 'basque', 'belarusian', 'bengali', 'bhojpuri', 'bosnian', 'bulgarian', 'catalan', 'cebuano', 'chichewa', 'chinese (simplified)', 'chinese (traditional)', 'corsican', 'croatian', 'czech', 'danish', 'dhivehi', 'dogri', 'dutch', 'english', 'esperanto', 'estonian', 'ewe', 'filipino', 'finnish', 'french', 'frisian', 'galician', 'georgian', 'german', 'greek', 'guarani', 'gujarati', 'haitian creole', 'hausa', 'hawaiian', 'hebrew', 'hindi', 'hmong', 'hungarian', 'icelandic', 'igbo', 'ilocano', 'indonesian', 'irish', 'italian', 'japanese', 'javanese', 'kannada', 'kazakh', 'khmer', 'kinyarwanda', 'konkani', 'korean', 'krio', 'kurdish (kurmanji)', 'kurdish (sorani)', 'kyrgyz', 'lao', 'latin', 'latvian', 'lingala', 'lithuanian', 'luganda', 'luxembourgish', 'macedonian', 'maithili', 'malagasy', 'malay', 'malayalam', 'maltese', 'maori', 'marathi', 'meiteilon (manipuri)', 'mizo', 'mongolian', 'myanmar', 'nepali', 'norwegian', 'odia (oriya)', 'oromo', 'pashto', 'persian', 'polish', 'portuguese', 'punjabi', 'quechua', 'romanian', 'russian', 'samoan', 'sanskrit', 'scots gaelic', 'sepedi', 'serbian', 'sesotho', 'shona', 'sindhi', 'sinhala', 'slovak', 'slovenian', 'somali', 'spanish', 'sundanese', 'swahili', 'swedish', 'tajik', 'tamil', 'tatar', 'telugu', 'thai', 'tigrinya', 'tsonga', 'turkish', 'turkmen', 'twi', 'ukrainian', 'urdu', 'uyghur', 'uzbek', 'vietnamese', 'welsh', 'xhosa', 'yiddish', 'yoruba', 'zulu']
tekst = 'Ik ben menno en ik ben dom'

from deep_translator import GoogleTranslator
import tkinter as tk


venster = tk.Tk()

taal = ""

listbox = tk.Listbox(venster)
listbox.grid(row=5,column=0)

def Translate():
    global taal
    translated = GoogleTranslator(source='auto', target=taal).translate(text=tekst)
    print(translated)
    tk.messagebox.showinfo(title='vertaalde tekst', message=translated)

def cb_search(event):
      
    sstr = search_str.get()
    listbox.delete(0, tk.END)
    # If filter removed show all data
    if sstr == "":
        fill_listbox(lijst) 
        return
  
    filtered_data = list()
    for item in lijst:
        if item.find(sstr) >= 0:
            filtered_data.append(item)
   
    fill_listbox(filtered_data)

def fill_listbox(ld):
    for item in ld:
        listbox.insert(tk.END, item)

def items_selected(event):
    global taal
    # get all selected indices
    gesilecteerd = listbox.curselection()
    # get selected items
    taal = ",".join([listbox.get(i) for i in gesilecteerd])

search_str = tk.StringVar()
search = tk.Entry(venster, textvariable=search_str, width=10)
search.grid(row=7,column=0)
button = tk.Button(venster,text="Translate",command=Translate)
button.grid(row=10,column=0)
search.bind('<Return>', cb_search)
listbox.bind('<<ListboxSelect>>', items_selected)

fill_listbox(lijst)
venster.title("vertalen")
tk.mainloop()