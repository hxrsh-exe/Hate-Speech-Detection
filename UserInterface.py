# Libraries Import
from main import scanner
from tkinter import *
import tkinter.messagebox as tmsg
from PIL import Image, ImageTk
from tkinter import filedialog

# Window
h_root = Tk()

# Interface Dimensions
h_root.geometry("1024x720")
h_root.minsize(300, 100)
h_root.maxsize(1200, 988)
h_root.config(bg='black')

# Interface Icon
try:
    h_root.iconbitmap('icon.ico')
except Exception as e:
    print(f"Error loading icon: {e}")

# Interface Title
h_root.title("Hate Speech Detection Software")

# Background Image
try:
    image = Image.open("bg.jpg")
    photo = ImageTk.PhotoImage(image)
    label = Label(h_root, image=photo)
    label.place(x=0, y=0)
except Exception as e:
    print(f"Error loading background image: {e}")

# Scanning Function
def scan():
    try:
        data = scanner(inputvalue.get())
        tmsg.showinfo("Scanned!!", data)
    except Exception as e:
        tmsg.showerror("Error", f"Error scanning text: {e}")

# File Open Function
def fileopen():
    try:
        textfile = filedialog.askopenfilename(initialdir="/C", title="Select a File", filetypes=(("txt files", "*.txt"),))
        with open(textfile, 'r') as file:
            textdata = file.read()
            data1 = scanner(textdata)
            tmsg.showinfo("Scanned!!", data1)
    except Exception as e:
        tmsg.showerror("Error", f"Error opening file: {e}")

# Text Input Box
inputvalue = StringVar()
userentry = Entry(h_root, textvariable=inputvalue, borderwidth=4)
userentry.place(x=750, y=70)

# Buttons Frame
f1 = Frame(h_root, bg="black", borderwidth=5, relief=SUNKEN)
f1.pack(side=RIGHT, anchor="ne", pady=120, padx=170)

# Buttons
b1 = Button(f1, bg="#8B0000", fg="white", text="   SCAN   ", command=scan, borderwidth=2, relief=RAISED)
b1.pack()

b2 = Button(f1, text="Open File", bg="#8B0000", fg="white", command=fileopen, borderwidth=2, relief=RAISED)
b2.pack(pady=2)

h_root.mainloop()
