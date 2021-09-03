import tkinter as tk
import PyPDF2
from PIL import Image, ImageTk

root = tk.Tk()

canvas = tk.Canvas(root, width = 600, height = 300)
canvas.grid(columnspan=3, rowspan=3) #creates 3 columns in the canvas/window

#title of the program
title_label = tk.Label(root, text = 'PDF_Extractor', font = ('Raleway', 30))
title_label.grid(columnspan=3, column=0, row=0)

#instructions for the user
instructions = tk.Label(root, text = 'Select a PDF on your computer to extract text from.', font = 'Raleway')
instructions.grid(columnspan=3, column=0, row=1)

#browse button
browse_text = tk.StringVar()
browse_button = tk.Button(root, textvariable= browse_text, font = 'Raleway', height = 2, width = 15)
browse_text.set('Browse')
browse_button.grid(column=1, row=2)

root.mainloop()