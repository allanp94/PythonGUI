import tkinter as tk 
from tkinter import *
from tkinter import ttk
from turtle import title
from PIL import Image, ImageTk
import PyPDF2 
from tkinter.filedialog import askopenfile

root = Tk()
canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3, rowspan=3)

# instructions
instructions = tk.Label(root, text="Select a PDF file on your computer to extract all its text")
instructions.grid(columnspan=3, column=0, row =1 )

def open_file():
    browse_text.set("loading...")    

    try: 
        file = askopenfile(parent=root, mode='rb',title="Choose a file" )
        if file:
            # print('file was successfully loaded')
            read_pdf = PyPDF2.PdfFileReader(file)
            page = read_pdf.getPage(0)
            page_content = page.extractText()
            # print(page_content)

            #text box 
            text_box = tk.Text(root, height=10, width=50, padx=15, pady=15)
            text_box.insert(1.0, page_content)
            text_box.grid(column=1, row=3)

            browse_text.set("Browse")
    except:
        print('could not open file')

#browse button
browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable=browse_text, command=lambda:open_file(), height=2, width=15)
browse_text.set("Browse")
browse_btn.grid(column=1, row=2)

canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3, rowspan=3)

root.mainloop()