#! ./scaler-env/bin/ python

import inquirer
import os
import tkinter as tk
from tkinter import filedialog

# Open tk file dialog
root = tk.Tk()
root.withdraw()
# Retrieve filename
filename = filedialog.askopenfilename()

if filename == None:
    print("Must select a pdf file")

# Select output name
outputname = input('Nome del file in output-> ')

print(outputname)

quality_list = [
    inquirer.List(
        "size",
        message="What quality do you need?",
        choices=["Z4RDOZ", "medium", "small"],
    ),
]

quality = inquirer.prompt(quality_list)

q = ""

if quality["size"] == "Z4RDOZ":
    q = "/printer"

elif quality["size"] == "medium":
    q = "/ebook"

elif quality["size"] == "small":
    q = "/screen"

# Do
os.system(
    f"gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS={q} -dNOPAUSE -dQUIET -dBATCH -sOutputFile={outputname}re {filename} "
)

print("ALL DONE, THX FOR USING Z4RDOZ' PDF RESIZE")
