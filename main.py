import tkinter as tk
import PyPDF2
from PIL import Image, ImageTk

root = tk.Tk()

canvas = tk.Canvas(root, width = 600, height = 300)
canvas.grid(columnspan=3) #creates 3 columns in the canvas/window
title_label = tk.Label(root, text = 'PDF_Extractor', font = ('Helvetica', 30))
title_label.grid(columnspan=3, column=0, row=0)

instructions = tk.Label(root, text = 'Select a PDF on your computer to extract text from.', font = 'Helvetica')
instructions.grid(columnspan=3, column=0, row=1)


root.mainloop()