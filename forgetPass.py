from tkinter import *
import tkinter as tk
from tkinter import messagebox as ms
from PIL import Image, ImageTk
import sqlite3

# Initialize the main window
root = tk.Tk()
root.configure(background='white')
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Forget Password")

# Default background in case the image is not found
background_image = None

# Attempt to load the background image
try:
    image2 = Image.open(r"C:\Users\Lenovo\Downloads\100% code Fake-Instagram-Profile (1)\100% code Fake-Instagram-Profile\pxfuel (8).jpg")  # Ensure this file is in the same directory as your script
    image2 = image2.resize((w, h), Image.LANCZOS)  # Use LANCZOS instead of ANTIALIAS
    background_image = ImageTk.PhotoImage(image2)
except FileNotFoundError:
    ms.showerror("Error", "Background image file not found. Please ensure 'pxfuel (8).jpg' is in the same directory.")
    # Proceed without the image

# Only place the background if it's loaded
if background_image:
    background_label = tk.Label(root, image=background_image)
    background_label.image = background_image  # Save a reference to avoid garbage collection
    background_label.place(x=0, y=0)

# Variables for user input
email = tk.StringVar()
password = tk.StringVar()
confirmPassword = tk.StringVar()

# Connect to the SQLite database
db = sqlite3.connect('crop1.db')
cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS registration"
               "(Fullname TEXT, address TEXT, Email TEXT, age TEXT, Gender TEXT, Phoneno TEXT, password TEXT)")
db.commit()

# Function to change password
def change_password():
    new_password_entry = password.get()
    confirm_password_entry = confirmPassword.get()
    
    # Check for the user in the database
    with sqlite3.connect('crop1.db') as db:
        c = db.cursor()
        find_user = ('SELECT * FROM registration WHERE Email=?')
        c.execute(find_user, [(str(email.get()))])
        result = c.fetchall()
        
        if result:
            if new_password_entry == confirm_password_entry:
                c.execute("UPDATE registration SET password=? WHERE Email=?", (str(new_password_entry), email.get()))
                db.commit()
                ms.showinfo('Congrats', 'Password changed successfully')
            else:
                ms.showerror('Error!', "Passwords didn't match")
        else:
            ms.showerror('Error!', "Email not found in the database.")

# UI Components
labl_1 = tk.Label(root, text="Forgot Password", width=15, font=("bold", 40), bg="white")
labl_1.place(x=350, y=200)

labl_1 = tk.Label(root, text="Email", width=10, font=("bold", 13), bg="white")
labl_1.place(x=370, y=330)

entry_1 = tk.Entry(root, textvariable=email)
entry_1.place(x=550, y=330, height=20, width=150)

labl_2 = tk.Label(root, text="New Password", width=15, font=("bold", 13), bg="white")
labl_2.place(x=370, y=370)

new_password_entry = tk.Entry(root, textvariable=password, show="*")  # Mask password input
new_password_entry.place(x=550, y=370, height=20, width=150)

labl_2 = tk.Label(root, text="Confirm Password", width=15, font=("bold", 13), bg="white")
labl_2.place(x=370, y=420)

confirm_password_entry = tk.Entry(root, textvariable=confirmPassword, show="*")  # Mask password input
confirm_password_entry.place(x=550, y=420, height=20, width=150)

forget_button = tk.Button(root, text="Change Password", font=("bold", 14), bg="red", fg="black", padx=20, pady=10, command=change_password)
forget_button.place(x=470, y=500, height=35, width=150)

root.mainloop()
