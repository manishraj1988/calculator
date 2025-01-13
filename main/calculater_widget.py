from tkinter import ttk
import tkinter as tk

calc = tk.Tk()
value = tk.StringVar()
calc.geometry("600x400")
calc.title("Calculator")
calc.grid()
calc.rowconfigure(0, weight=1)
calc.rowconfigure(1, weight=1)
calc.rowconfigure(2, weight=1)
calc.rowconfigure(3, weight=1)
calc.rowconfigure(4, weight=1)

calc.columnconfigure(0, weight = 1)
calc.columnconfigure(1, weight = 1)
input_box = tk.Entry(calc, textvariable=value)
input_box.grid(row=3, column=1)

calc.mainloop()