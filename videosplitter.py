#vid splitter
import os
import cv2
import tkinter as tk
from tkinter import *
from tkinter import filedialog

def splitter():

    og_directory_path = os.getcwd()

    ospath = entry_widget_2.get()
        
    savepath = os.path.join(og_directory_path, ospath)

    os.makedirs(savepath)

    entrypath = entry_widget_1.get()

    framefreq = entry_widget_3.get()
    
    print("savepath :" + savepath)

    print("entrypath :" + entrypath)
    
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
            laplacian_var = cv2.Laplacian(image, cv2.CV_64F).var()
            print(laplacian_var)
            if (laplacian_var > 110): # make this an average?
                cv2.imwrite(os.path.join(savepath, '%d.jpg' % filecount), image)
                print('wrote frame %d' % count)
                filecount += 1
            else:
                print('image rejected due to high blur')
            
    print('done')

def browser():
    global entrypath
    entrypath = filedialog.askopenfilename(initialdir = "/")
    entry_widget_1.insert(0,entrypath)

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

startbtn = Button(window, text="Start Program", font=("Arial Bold", 12), command = splitter)
startbtn.pack()

broswebtn = Button(window, text="Browse for file", font=("Arial Bold", 12), command = browser)
broswebtn.pack()


text = Label(window, text="Path to Video")
text.place(x=55,y=5)


text = Label(window, text="Name of Folder")
text.place(x=50,y=25)

text = Label(window, text="Frame Frequence (2 - 5)")
text.place(x=7, y=40)


window.mainloop()
