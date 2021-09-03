from os import read
import tkinter as tk
from tkinter.constants import CENTER
import PyPDF2
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile

root = tk.Tk()

canvas = tk.Canvas(root, width = 600, height = 300)
canvas.grid(columnspan=3, rowspan=3) #creates 3 columns in the canvas/window

#title of the program
title_label = tk.Label(root, text = 'PDF_Extractor', font = ('Raleway', 30))
title_label.grid(columnspan=3, column=0, row=0)

#instructions for the user
instructions = tk.Label(root, text = 'Select a PDF on your computer to extract text from.', font = 'Raleway')
instructions.grid(columnspan=3, column=0, row=1)

#function to perform when user tries to select a file to extract text from
def open_pdf():
    browse_text.set('Searching...')
    file_var = askopenfile(parent=root, mode='rb', title='Choose a file', filetypes=[('Pdf file', '*.pdf')])
    if file_var:
        read_pdf = PyPDF2.PdfFileReader(file_var)
        page = read_pdf.getPage(0)
        page_text = page.extractText()

        #text box to display the text form the PDF
        text_box = tk.Text(root, height=10, width=50, padx=15, pady=15)
        text_box.insert(1.0, page_text)
        text_box.tag_configure('center', justify='center')
        text_box.tag_add('center', 1.0, 'end')
        text_box.grid(column=1, row=3)
        browse_text.set('Browse')

#browse button
browse_text = tk.StringVar()
browse_button = tk.Button(root, textvariable= browse_text, command = lambda:open_pdf(), font = 'Raleway', height = 2, width = 15)
browse_text.set('Browse')
browse_button.grid(column=1, row=2)

root.mainloop()