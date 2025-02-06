

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
from subprocess import call
import tkinter as tk
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from PIL import Image, ImageTk
from tkinter import ttk
from sklearn.decomposition import PCA
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
#import video_capture as value
#import lecture_details as detail_data
#import video_second as video1

#import lecture_video  as video

global fn
fn = ""
##############################################+=============================================================
root = tk.Tk()
root.configure(background="brown")
# root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Fake Profile Detection System")

# 43

# ++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
image2 = Image.open('img3.jpg')
image2 = image2.resize((1530, 900), Image.LANCZOS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0)  # , relwidth=1, relheight=1)
#
label_l1 = tk.Label(root, text="Fake Profile System",font=("Times New Roman", 30, 'bold'),
                    background="Maroon", fg="white", width=75, height=1)
label_l1.place(x=0, y=0)

#T1.tag_configure("center", justify='center')
#T1.tag_add("center", 1.0, "end")

################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#def clear_img():
#    img11 = tk.Label(root, background='bisque2')
#    img11.place(x=0, y=0)


#################################################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
label=tk.Label(root,text='''
               People who hide under fake accounts and anonymous account. Have nothing good to say. 
               They always talk trash about others. Influence hate , bullying and abuse. They are 
               instigators. They use this accounts to say filthy things and to ruin people lives. 
               What they don't know is that Karma knows their real identity.
               '''
               ,font=("Calibri",12),bg="pink",
               
               fg="black")
label.place(x=500,y=550)

################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

#

def reg():
    
    data = pd.read_csv("insta_train.csv")
    data.head()

    data = data.dropna()

    """One Hot Encoding"""

    le = LabelEncoder()
    data['profile_pic'] = le.fit_transform(data['profile_pic'])
    data['nums_length_username'] = le.fit_transform(data['nums_length_username'])
    data['fullname_words'] = le.fit_transform(data['fullname_words'])
    data['nums_length_fullname'] = le.fit_transform(data['nums_length_fullname'])
    data['name_username'] = le.fit_transform(data['name_username'])
    data['description_length'] = le.fit_transform(data['description_length'])
    data['external_URL'] = le.fit_transform(data['external_URL'])
    data['private'] = le.fit_transform(data['private'])
    data['posts'] = le.fit_transform(data['posts'])
    data['followers'] = le.fit_transform(data['followers'])
    data['follows'] = le.fit_transform(data['follows'])
   
   
       

    """Feature Selection => Manual"""
    x = data.drop(['fake'], axis=1)
    data = data.dropna()

    print(type(x))
    y = data['Class']
    print(type(y))
    x.shape
    

    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.30,random_state=15)


    # from sklearn.svm import SVC
    # svcclassifier = SVC(kernel='linear')
    # svcclassifier.fit(x_train, y_train)
    
    from sklearn.svm import SVC
    svcclassifier = SVC(kernel='linear')
    svcclassifier.fit(x_train, y_train)

    y_pred = svcclassifier.predict(x_test)
    print(y_pred)

    
    print("=" * 40)
    print("==========")
    print("Classification Report : ",(classification_report(y_test, y_pred)))
    print("Accuracy : ",accuracy_score(y_test,y_pred)*100)
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy: %.2f%%" % (accuracy * 100.0))
    ACC = (accuracy_score(y_test, y_pred) * 100)
    repo = (classification_report(y_test, y_pred))
    
    label4 = tk.Label(root,text =str(repo),width=45,height=10,bg='khaki',fg='black',font=("Tempus Sanc ITC",14))
    label4.place(x=205,y=200)
    
    label5 = tk.Label(root,text ="Accracy : "+str(ACC)+"%\nModel saved as SVM.joblib",width=45,height=3,bg='khaki',fg='black',font=("Tempus Sanc ITC",14))
    label5.place(x=205,y=420)
    from joblib import dump
    dump (svcclassifier,"SVM.joblib")
    print("Model saved as SVM.joblib")


    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.30,random_state=9999)


    from sklearn.ensemble import RandomForestClassifier  
    svcclassifier =RandomForestClassifier(n_estimators= 10, criterion="entropy")
 # from sklearn.svm import SVC
 # svcclassifier = SVC(kernel='linear')
 # svcclassifier.fit(x_train, y_train)
 
    from sklearn.ensemble import RandomForestClassifier
    svcclassifier = RandomForestClassifier(kernel='linear')
    svcclassifier.fit(x_train, y_train)

    y_pred = svcclassifier.predict(x_test)
    print(y_pred)

 
    print("=" * 40)
    print("==========")
    print("Classification Report : ",(classification_report(y_test, y_pred)))
    print("Accuracy : ",accuracy_score(y_test,y_pred)*100)
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy: %.2f%%" % (accuracy * 100.0))
    ACC = (accuracy_score(y_test, y_pred) * 100)
    repo = (classification_report(y_test, y_pred))
 
    label4 = tk.Label(root,text =str(repo),width=45,height=10,bg='khaki',fg='black',font=("Tempus Sanc ITC",14))
    label4.place(x=205,y=200)
 
    label5 = tk.Label(root,text ="Accracy : "+str(ACC)+"%\nModel saved as RF.joblib",width=45,height=3,bg='khaki',fg='black',font=("Tempus Sanc ITC",14))
    label5.place(x=205,y=420)
    from joblib import dump
    dump (svcclassifier,"RF.joblib")
    print("RF.joblib")

    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.30,random_state=9999)


    from sklearn.tree import DecisionTreeClassifier   
    clf_entropy = DecisionTreeClassifier( 
            criterion = "entropy", random_state = 100, 
            max_depth = 3, min_samples_leaf = 5)
 # from sklearn.svm import SVC
 # svcclassifier = SVC(kernel='linear')
 # svcclassifier.fit(x_train, y_train)
 
    from sklearn.tree import DecisionTreeClassifier
    svcclassifier = DecisionTreeClassifier(kernel='linear')
    svcclassifier.fit(x_train, y_train)

    y_pred = DecisionTreeClassifier.predict(x_test)
    print(y_pred)

 
    print("=" * 40)
    print("==========")
    print("Classification Report : ",(classification_report(y_test, y_pred)))
    print("Accuracy : ",accuracy_score(y_test,y_pred)*100)
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy: %.2f%%" % (accuracy * 100.0))
    ACC = (accuracy_score(y_test, y_pred) * 100)
    repo = (classification_report(y_test, y_pred))
 
    label4 = tk.Label(root,text =str(repo),width=45,height=10,bg='khaki',fg='black',font=("Tempus Sanc ITC",14))
    label4.place(x=205,y=200)
 
    label5 = tk.Label(root,text ="Accracy : "+str(ACC)+"%\nModel saved as RF.joblib",width=45,height=3,bg='khaki',fg='black',font=("Tempus Sanc ITC",14))
    label5.place(x=205,y=420)
    from joblib import dump
    dump (svcclassifier,"DT.joblib")
    print("DT.joblib")


def log():
   from subprocess import call
   call(["python","Check.py"])
    
def window():
  root.destroy()


# button1 = tk.Button(root, text="Model Training", command=reg, width=12, height=1,font=('times', 20, ' bold '), bg="black", fg="white")
# button1.place(x=80, y=160)


button3 = tk.Button(root, text="Check Profile",command=log,width=14, height=1,font=('times', 20, ' bold '), bg="black", fg="white")
button3.place(x=80, y=250)

button4 = tk.Button(root, text="Exit",command=window,width=14, height=1,font=('times', 20, ' bold '), bg="red", fg="black")
button4.place(x=80, y=460)

root.mainloop()