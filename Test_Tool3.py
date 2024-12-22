import tkinter as tk

from tkinter import *
from tkinter import messagebox

import conversion03 as con
from conversion03 import *




class MainGUI:
    
    def __init__(self):

        self.root = tk.Tk()

        self.label = tk.Label(self.root, text = "Your Message!", font = ('Arial', 18))
        self.label.pack(padx = 10, pady = 10)


        self.unitNum = tk.Text(self.root, height = 1, font = ('Comic Sans', 18))
        self.unitNum.pack(padx = 10, pady = 10)

        

        self.button = tk.Button(self.root, text = "Show Message", font = ('Arial', 18), command = self.show_message)
        self.button.pack(padx = 10, pady = 10)

        self.radio = IntVar()
        
        self.r1 = Radiobutton(self.root, text = "MB/sec to GB/Hour", font = ('Comic Sans', 18), variable = self.radio, value = 1).pack(padx = 10, pady = 10)

        #self.radio = IntVar()
        
        self.r1 = Radiobutton(self.root, text = "KB/Sec to GB/Hour", font = ('Comic Sans', 18), variable = self.radio, value = 2).pack(padx = 10, pady = 10)

        self.r1 = Radiobutton(self.root, text = "Suck", font = ('Comic Sans', 18), variable = self.radio, value = 3).pack(padx = 10, pady = 10)


    
        self.root.mainloop()

    def show_message(self):

        num = self.unitNum.get('1.0', tk.END)

        unit = self.radio.get()


        num = float(num)

        
        obb = con.conv.unitOf(self, num, unit)

        messagebox.showinfo(title = "Message", message = obb)

MainGUI()