# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 14:27:05 2021

@author: om
"""

import tkinter as tk
from tkinter import ttk, LEFT, END
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox as ms
import cv2
import sqlite3
import os
import numpy as np
import time
from tkvideo import tkvideo
'''import detection_emotion_practice as validate'''
#import video_capture as value
#import lecture_details as detail_data
#import video_second as video1

#import lecture_video  as video

global fn
fn = ""
##############################################+=============================================================
root = tk.Tk()
root.configure(background="white")
# root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Fake Profile ")

# 43
video_label =tk.Label(root)
video_label.pack()
# read video to display on label
player = tkvideo("bag.mp4", video_label,loop = 1, size = (w, h))
player.play()
# ++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
# image2 = Image.open('new5.jpg')
# image2 = image2.resize((1530, 900), Image.ANTIALIAS)

# background_image = ImageTk.PhotoImage(image2)

# background_label = tk.Label(root, image=background_image)

# background_label.image = background_image

# background_label.place(x=0, y=70)  # , relwidth=1, relheight=1)
#
label_l1 = tk.Label(root, text="Fake Profile System ",font=("Times New Roman", 25, 'bold'),
                    background="#00ffff", fg="#000000", width=80, height=1)
label_l1.place(x=0, y=0)

#T1.tag_configure("center", justify='center')
#T1.tag_add("center", 1.0, "end")

################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#def clear_img():
#    img11 = tk.Label(root, background='bisque2')
#    img11.place(x=0, y=0)


#################################################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
label=tk.Label(root,text='''
               What you give is what you get in life. You might not get it same time, but you will eventually get it one day. 
               Choosing to treat other people bad, cyber bullying and hurting them for no reason. Being mean and rude to other 
               people for no reason. Even if you are using fake or anonymous accounts. One day you will get what you 
               giving and what you are doing. Sometimes bad luck we create it ourselves by how we treat others.
               '''
               ,font=("Calibri",12),bg="pink",
               
               fg="black")
label.place(x=500,y=550)

################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# def cap_video():
    
#     video1.upload()
#     #from subprocess import call
#     #call(['python','video_second.py'])

def reg():
    from subprocess import call
    call(["python","registration.py"])

def log():
    from subprocess import call
    call(["python","login.py"])
    
    
def window():
  root.destroy()


button1 = tk.Button(root, text="LOGIN", command=log, width=14, height=1,font=('times', 20, ' bold '), bg="#FFEBCD", fg="black")
button1.place(x=20, y=300)

button2 = tk.Button(root, text="REGISTER",command=reg,width=14, height=1,font=('times', 20, ' bold '), bg="#FFEBCD", fg="black")
button2.place(x=20, y=190)

button3 = tk.Button(root, text="EXIT",command=window,width=14, height=1,font=('times', 20, ' bold '), bg="#FFEBCD", fg="black")
button3.place(x=20, y=400)

root.mainloop()