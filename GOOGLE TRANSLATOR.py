from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import messagebox
from deep_translator import GoogleTranslator

root = tk.Tk()
root.title('Language Translator')
root.geometry('530x330')
root.maxsize(530, 330)
root.minsize(530, 330)

def translate():
    language_1 = t1.get("1.0", "end-1c")
    c1 = choose_language.get()

    if language_1 == '':
        messagebox.showerror('Language Translator', 'Please fill the box')
    else:
        output = GoogleTranslator(source='auto', target=c1.lower()).translate(language_1)
        t2.insert('end', output)

def clear():
    t1.delete(1.0, 'end')
    t2.delete(1.0, 'end')

img = ImageTk.PhotoImage(Image.open('googletranslogo1.png'))
label = Label(image=img)
label.place(x=0, y=0)

a = tk.StringVar()
auto_detect = ttk.Combobox(root, width=20, textvariable=a, state='readonly')
auto_detect['values'] = ('Auto Detect',)
auto_detect.place(x=30, y=70)
auto_detect.current(0)

l = tk.StringVar()
choose_language = ttk.Combobox(root, width=20, textvariable=l, state='readonly')
choose_language['values'] = (
    'afrikaans', 'albanian', 'arabic', 'armenian', 'azerbaijani', 'basque', 'belarusian', 'bengali', 'bosnian',
    'bulgarian', 'catalan', 'cebuano', 'dutch', 'danish', 'dari', 'english', 'egyptian', 'french', 'filipino',
    'flemish', 'georgian', 'galician', 'gikuyu', 'hindi', 'hakka', 'hebrew', 'iban', 'ilonggo', 'indonesian',
    'japanese', 'jewish', 'kannada', 'korean', 'kamba', 'kanuri', 'ladin', 'latin', 'ladakhi', 'malayalam',
    'madurese', 'macedonian', 'nepali', 'nuer', 'nemadi', 'oriya', 'polish', 'punjabi', 'persian', 'portuguese',
    'russian', 'romany', 'rajasthani', 'sanskrit', 'serbian', 'slovenian', 'somali', 'spanish', 'sudanese', 'swedish',
    'telugu', 'tamil', 'thai', 'turkish', 'tatar', 'tajik', 'ukrainian', 'urdu', 'uzbek', 'vietnamese', 'yala',
    'yoruba', 'yumaa', 'zulu'
)
choose_language.place(x=290, y=70)
choose_language.current(0)

t1 = Text(root, width=30, height=10, borderwidth=5, relief=RIDGE)
t1.place(x=10, y=100)

t2 = Text(root, width=30, height=10, borderwidth=5, relief=RIDGE)
t2.place(x=260, y=100)

button = Button(root, text="Translate", relief=RIDGE, borderwidth=3, font=('verdana', 10, 'bold'), cursor="hand2", command=translate)
button.place(x=150, y=280)

clear_button = Button(root, text="Clear", relief=RIDGE, borderwidth=3, font=('verdana', 10, 'bold'), cursor="hand2", command=clear)
clear_button.place(x=280, y=280)

root.mainloop()
