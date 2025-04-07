from tkinter import *
def Train():
    """GUI"""
    import tkinter as tk
    import numpy as np
    import pandas as pd
    import PIL
    from sklearn.decomposition import PCA
    from sklearn.preprocessing import LabelEncoder
    from PIL import Image ,ImageTk
    root = tk.Tk()

    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry("%dx%d+0+0" % (w, h))
    root.title("Fake Profile System")
    root.configure(background="deeppink")
    
   
    
    
    
    w,h = root.winfo_screenwidth(),root.winfo_screenheight()
    
    bg = Image.open(r"C:\Users\Lenovo\Desktop\proj_demo/instaimage.jpg")
    bg.resize((1366,500),Image.LANCZOS)
    print(w,h)
    bg_img = ImageTk.PhotoImage(bg)
    bg_lbl = tk.Label(root,image=bg_img)
    bg_lbl.place(x=600,y=0)
    
    
    
    profile_pic = tk.IntVar()
    nums_length_username = tk.IntVar()
    fullname_words = tk.IntVar()
    nums_length_fullname = tk.IntVar()
    name_username = tk.IntVar()
    description_length = tk.IntVar()
    external_URL = tk.IntVar()
    private = tk.IntVar()
    posts= tk.IntVar()
    followers = tk.IntVar()
    follows = tk.DoubleVar()
    
    
    #===================================================================================================================
    def Detect():
        e1=profile_pic.get()
        print(e1)
        e2=nums_length_username.get()
        print(e2)
        e3=fullname_words.get()
        print(e3)
        e4=nums_length_fullname.get()
        print(e4)
        e5=name_username.get()
        print(e5)
        e6=description_length.get()
        print(e6)
        e7=external_URL.get()
        print(e7)
        e8=private.get()
        print(e8)
        e9=posts.get()
        print(e9)
        e10=followers.get()
        print(e10)
        e11=follows.get()
        print(e11)
       
        
       #####For background Image
 # , relwidth=1, relheight=1)
        
        
        #########################################################################################
        
        from joblib import dump , load
        a1=load(r'SVM.joblib')
        v= a1.predict([[e1, e2, e3, e4, e5, e6, e7, e8, e9,e10, e11]])
        print(v)
        if v[0]==0:
            print("yes")
            yes = tk.Label(root,text="Fake profile detected",background="red",foreground="white",font=('times', 20, ' bold '),width=15)
            yes.place(x=450,y=600)
        
       
        else:
            print("no")
            no = tk.Label(root, text="Real profile detected", background="green", foreground="white",font=('times', 20, ' bold '),width=15)
            no.place(x=450, y=600)
            


    l1=tk.Label(root,text="profile_pic :",background="deeppink",font=('times', 20, ' bold '),)
    l1.place(x=5,y=5)
    gender=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=profile_pic)
    gender.place(x=400,y=1)

    l2=tk.Label(root,text="nums_length_username :",background="deeppink",font=('times', 20, ' bold '),)
    l2.place(x=5,y=50)
    Nationlity=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=nums_length_username)
    Nationlity.place(x=400,y=50)

    l3=tk.Label(root,text="fullname_words :",background="deeppink",font=('times', 20, ' bold '),)
    l3.place(x=5,y=100)
    PlaceofBirth=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=fullname_words)
    PlaceofBirth.place(x=400,y=100)
    
    l4=tk.Label(root,text="nums_length_fullname :",background="deeppink",font=('times', 20, ' bold '),)
    l4.place(x=5,y=150)
    StageID=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=nums_length_fullname)
    StageID.place(x=400,y=160)

    l5=tk.Label(root,text="name_username :",background="deeppink",font=('times', 20, ' bold '),)
    l5.place(x=5,y=200)
    GradeID=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=name_username)
    GradeID.place(x=400,y=200)

    l6=tk.Label(root,text="description_length :",background="deeppink",font=('times', 20, ' bold '),)
    l6.place(x=5,y=250)
    Topic=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=description_length)
    Topic.place(x=400,y=250)

    l7=tk.Label(root,text="external_URL :",background="deeppink",font=('times', 20, ' bold '),)
    l7.place(x=5,y=300)
    Semester=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=external_URL)
    Semester.place(x=400,y=300)

    l8=tk.Label(root,text="private :",background="deeppink",font=('times', 20, ' bold '),)
    l8.place(x=5,y=350)
    VisitedResources=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=private)
    VisitedResources.place(x=400,y=350)

    l9=tk.Label(root,text="posts :",background="deeppink",font=('times', 20, ' bold '),)
    l9.place(x=5,y=400)
    AnnouncementsView=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=posts)
    AnnouncementsView.place(x=400,y=400)

    l10=tk.Label(root,text="followers :",background="deeppink",font=('times', 20, ' bold '),)
    l10.place(x=5,y=450)
    Discussion=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=followers)
    Discussion.place(x=400,y=450)

    l11=tk.Label(root,text="follows :",background="deeppink",font=('times', 20, ' bold '),)
    l11.place(x=5,y=500)
    ParentAnsweringSurvey=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=follows)
    ParentAnsweringSurvey.place(x=400,y=500)

   

    
    
    button1 = tk.Button(root,text="Submit",command=Detect,font=('times', 20, ' bold '),width=10)
    button1.place(x=600,y=650)


    root.mainloop()

Train()