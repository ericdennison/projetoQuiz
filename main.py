import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
import pandas as pd
import random

# lendo arquivo excel | pegando 10 valores aleatórios
df = pd.read_excel('questions.xlsx')
questions = df.sample(n=10).values.tolist()

# interface
janela=tk.Tk()
janela.title("Quiz")
janela.geometry('400x450')
background_color = "#ECECEC"
text_color = "#333333"
button_color = "#4CAF50"
janela.config(bg=background_color)
janela.option_add('*Font', 'Arial')
janela.mainloop()
