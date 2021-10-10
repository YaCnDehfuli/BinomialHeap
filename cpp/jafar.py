from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from googletrans import Translator
import pyttsx3 as pt

root = Tk()
root.title()
root.resizable("False","False")
root.minsize(530,330)
root.config(background="#6595ed")

def translate():
    language_1 = t1.get("1.0","end-1c")
    cl = choose_language.get()

    if language_1 == "":
        messagebox.showerror("Language Translator","Please fill the box")
    else:
        t2.delete(1.0,"end")
        translator = Translator()
        output = translator.translate(language_1,dest=cl)
        t2.insert("end",output.text)

def clear():
    t1.delete(1.0,"end")
    t2.delete(1.0,"end")

def play_sound():
    engine = pt.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-30)
    engine.say(t2.get("1.0","end-1c"))
    engine.runAndWait()


a=StringVar()
auto_detect = ttk.Combobox(root,width=20,textvariable=a,state="readonly",font=("verdana",10,"bold"))
auto_detect["values"]=("Auto Detect",)
auto_detect.place(x=30,y=70)
auto_detect.current(0)

l=StringVar()
choose_language = ttk.Combobox(root,width=20,textvariable=l,state="readonly",font=("verdana",10,"bold"))
choose_language["values"]=("English","Persian","French")
choose_language.place(x=290,y=70)
choose_language.current(0)

t1 = Text(root,width=30,height=10,borderwidth=5,relief=RIDGE)
t1.place(x=10,y=100)

t2 = Text(root,width=30,height=10,borderwidth=5,relief=RIDGE)
t2.place(x=260,y=100)

button = Button(root,text="Translate",width=10 ,font=("vedana",10,"bold"),cursor="hand2",command=translate,bg = "#323233" , fg="#fff")
button.place(x=150,y=280)


clear = Button(root,text="Clear",width=10,font=("vedana",10,"bold"),cursor="hand2",command=clear,bg = "#323233" , fg="#fff")
clear.place(x=280,y=280)

voice = Button(root,text="Voice",width=4,font=("vedana",10,"bold"),cursor="hand2",command=play_sound,bg = "#323233" , fg="#fff")
voice.place(x=464,y=240) 

root.mainloop()
