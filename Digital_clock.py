import tkinter as tk
from time import strftime

def updat_time():

    time = strftime('%H:%M,%S %p')
    ibl.config(text = time)
    ibl.after(1000,updat_time)


root = tk.Tk()

root.title("Digital clock")

ibl = tk.Label ( root , font = ('LCD solid',50,'bold'),bg = 'black' ,fg = 'green')
ibl.pack(anchor = 'center')
updat_time()

root.mainloop()