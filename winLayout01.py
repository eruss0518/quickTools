import tkinter as tk
from tkinter import messagebox
import subprocess

class MyGui:

    def __init__(self):

        self.root = tk.Tk()
        self.root.geometry("1920x1080")

        #x = subprocess.call(['C:\Windows\System32\Taskmgr.exe'])

        self.label = tk.Label(self.root, text = "Launcher", font = ('Arial', 18))
        self.label.pack(padx = 10, pady = 10)

        buttonFrame = tk.Frame(self.root)
        buttonFrame.columnconfigure(0, weight = 1)
        buttonFrame.columnconfigure(1, weight = 1)

        button1 = tk.Button(buttonFrame, text = "Task Manager", font = ('Arial', 18), command = self.openT)
        button1.grid(row = 0, column = 0, padx = 10, pady = 10)

        button2 = tk.Button(buttonFrame, text = "Ping Test", font = ('Arial', 18), command = self.pingT)
        button2.grid(row = 0, column = 1, padx = 10, pady = 10)

        button3 = tk.Button(buttonFrame, text = "Resource Monitor", font = ('Arial', 18), command = self.openRM)
        button3.grid(row = 1, column = 0, padx = 10, pady = 10)

        button4 = tk.Button(buttonFrame, text = "System Info", font = ('Arial', 18), command = self.openSysfo)
        button4.grid(row = 1, column = 1, padx = 10, pady = 10)

        buttonFrame.pack(fill = 'x')

        

        self.root.mainloop()

    def openT(self):
        subprocess.call(['C:\Windows\System32\Taskmgr.exe'], shell = True)


    def pingT(self):
        c = subprocess.run("ping google.com -n 10", stdout = subprocess.PIPE)
        messagebox.showinfo(title = "Ping", message = c)

    def openRM(self):
        subprocess.call(['C:\Windows\System32\\resmon.exe'], shell = True)

    def openSysfo(self):
        sfo = subprocess.run("systeminfo", stdout = subprocess.PIPE)
        messagebox.showinfo(title = "System Info", message = sfo)

MyGui()