import tkinter as tk
import PyPDF2
from PIL import Image, ImageTk

root = tk.Tk()

canvas = tk.Canvas(root, width = 1920, height = 1080)
canvas.grid(columnspan=3) #creates 3 columns in the canvas/window
title_label = tk.Label(root, text = 'PDF_Extractor', font = ('Helvetica', 30))
title_label.place(x = 620, y = 10)

root.mainloop()