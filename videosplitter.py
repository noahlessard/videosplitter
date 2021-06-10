#vid splitter
import os
import cv2
import tkinter as tk
from tkinter import *

def splitter():

    og_directory_path = os.getcwd()

    ospath = entry_widget_2.get()
        
    savepath = os.path.join(og_directory_path, ospath)

    os.makedirs(savepath)

    entrypath = entry_widget_1.get()

    framefreq = entry_widget_3.get()
    
    print(savepath)

    print(entrypath)

    print(type(framefreq))
    try:
        video = cv2.VideoCapture(entrypath)
    except:
        print('no entry found')
        
    count = 0
    filecount = 1
    success = 1

    while success:
        success, image = video.read()
        count +=1
        if (count % int(framefreq) == 0):
            cv2.imwrite(os.path.join(savepath, '%d.jpg' % filecount), image)
            print('wrote frame %d' % count)
            filecount += 1
            
    print('done')

window = Tk()

window.geometry('400x400')

entrypath = tk.StringVar()
entry_widget_1 = tk.Entry(window, textvariable=entrypath)
entry_widget_1.pack()


ospath = tk.StringVar()
entry_widget_2 = tk.Entry(window, textvariable=ospath)
entry_widget_2.pack()


framefreq = tk.StringVar()
entry_widget_3 = tk.Entry(window, textvariable=framefreq)
entry_widget_3.pack()

btn = Button(window, text="Start Program", font=("Arial Bold", 12), command = splitter)
btn.pack()


text = Label(window, text="Path to Video")
text.place(x=55,y=5)


text = Label(window, text="Name of Folder")
text.place(x=50,y=25)

text = Label(window, text="Frame Frequence (2 - 5)")
text.place(x=7, y=40)


window.mainloop()
