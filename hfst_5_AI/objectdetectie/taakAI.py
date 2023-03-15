from PIL import Image
from pytesseract import Output
import pytesseract
import numpy as np
import cv2
import keyboard
import continuous_threading
from matplotlib import pyplot as plt
from deep_translator import GoogleTranslator
import tkinter as tk
from tkinter.messagebox import showinfo
from detectie import open_camera, yolo_verwerking, realtime, get_camera_src
text = ""
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
def realtime_time():
    global text
    def plt_imshow(title, image):
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        plt.imshow(image)
        plt.title(title)
        plt.grid(False)
        plt.show()
    # define a video capture object
    vid = cv2.VideoCapture(2, cv2.CAP_DSHOW)

    def get_grayscale(image):
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # noise removal
    def remove_noise(image):
        return cv2.medianBlur(image,5)

    #thresholding
    def thresholding(image):
        return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    #dilation
    def dilate(image):
        kernel = np.ones((5,5),np.uint8)
        return cv2.dilate(image, kernel, iterations = 1)
        
    #erosion
    def erode(image):
        kernel = np.ones((5,5),np.uint8)
        return cv2.erode(image, kernel, iterations = 1)

    #opening - erosion followed by dilation
    def opening(image):
        kernel = np.ones((5,5),np.uint8)
        return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

    #canny edge detection
    def canny(image):
        return cv2.Canny(image, 100, 200)

    #skew correction
    def deskew(image):
        coords = np.column_stack(np.where(image > 0))
        angle = cv2.minAreaRect(coords)[-1]
        if angle < -45:
            angle = -(90 + angle)
        else:
            angle = -angle
        (h, w) = image.shape[:2]
        center = (w // 2, h // 2)
        M = cv2.getRotationMatrix2D(center, angle, 1.0)
        rotated = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
        return rotated

    #template matching
    def match_template(image, template):
        return cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED) 

    while(True):
        
        # Capture the video frame
        # by frame
        ret, frame = vid.read()
        cv2.imwrite(r"C:\Users\TeJu171204\Documents\6IICT_PROG4_oef\hfst_5_AI\objectdetectie\TaakAI.png", frame)
        image = cv2.imread(r"C:\Users\TeJu171204\Documents\6IICT_PROG4_oef\hfst_5_AI\objectdetectie\TaakAI.png")
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        if vid:
            # save the image
            gray = get_grayscale(image)

            d = pytesseract.image_to_data(gray, output_type=Output.DICT)
            n_boxes = len(d['text'])
            for i in range(n_boxes):
                if int(d['conf'][i]) > 60:
                    (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
                    frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            custom_config = r'--oem 3 --psm 6'
            if keyboard.is_pressed('shift'):
                if keyboard.is_pressed('s'):
                    text = pytesseract.image_to_string(gray)
                    print(f"output:{text}")
                if keyboard.is_pressed('i'):
                    cv2.imshow('gray', gray)
            cv2.imshow('frame', frame)
        else:
            print("error")
    
    # After the loop release the cap object
    vid.release()
    # Destroy all the windows
    cv2.destroyAllWindows()

thread = continuous_threading.ContinuousThread(target = realtime_time)
thread.allow_shutdown()
thread.start()

lijst = ['afrikaans', 'albanian', 'amharic', 'arabic', 'armenian', 'assamese', 'aymara', 'azerbaijani', 'bambara', 'basque', 'belarusian', 'bengali', 'bhojpuri', 'bosnian', 'bulgarian', 'catalan', 'cebuano', 'chichewa', 'chinese (simplified)', 'chinese (traditional)', 'corsican', 'croatian', 'czech', 'danish', 'dhivehi', 'dogri', 'dutch', 'english', 'esperanto', 'estonian', 
         'ewe', 'filipino', 'finnish', 'french', 'frisian', 'galician', 'georgian', 'german', 'greek', 'guarani', 'gujarati', 'haitian creole', 'hausa', 'hawaiian', 'hebrew', 'hindi', 'hmong', 'hungarian', 'icelandic', 'igbo', 'ilocano', 'indonesian', 'irish', 'italian', 'japanese', 'javanese', 'kannada', 'kazakh', 'khmer', 'kinyarwanda', 'konkani', 'korean', 'krio', 'kurdish (kurmanji)',
         'kurdish (sorani)', 'kyrgyz', 'lao', 'latin', 'latvian', 'lingala', 'lithuanian', 'luganda', 'luxembourgish', 'macedonian', 'maithili', 'malagasy', 'malay', 'malayalam', 'maltese', 'maori', 'marathi', 'meiteilon (manipuri)', 'mizo', 'mongolian', 'myanmar', 'nepali', 'norwegian', 'odia (oriya)', 'oromo', 'pashto', 'persian', 'polish', 'portuguese', 'punjabi', 'quechua', 'romanian', 
         'russian', 'samoan', 'sanskrit', 'scots gaelic', 'sepedi', 'serbian', 'sesotho', 'shona', 'sindhi', 'sinhala', 'slovak', 'slovenian', 'somali', 'spanish', 'sundanese', 'swahili', 'swedish', 'tajik', 'tamil', 'tatar', 'telugu', 'thai', 'tigrinya', 'tsonga', 'turkish', 'turkmen', 'twi', 'ukrainian', 'urdu', 'uyghur', 'uzbek', 'vietnamese', 'welsh', 'xhosa', 'yiddish', 'yoruba', 'zulu']



venster = tk.Tk()

taal = ""

listbox = tk.Listbox(venster)
listbox.grid(row=5,column=0)

def Translate():
    global text
    global taal
    print(f"output2: {text}")
    translated = GoogleTranslator(source='auto', target=taal).translate(text)
    print(translated)
    showinfo(title='vertaalde tekst', message=translated)

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