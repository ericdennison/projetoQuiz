import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
import pandas as pd
import random

# lendo arquivo excel | pegando 10 valores aleatórios
df = pd.read_excel('questions.xlsx')
questions = df.sample(n=10).values.tolist()

# variaveis globais
score = 0
current_question = 0


# função verificar resposta
def check_answer(answer):
    global score, current_question

    if answer == correct_answer.get():
        score += 1
    current_question += 1

    if current_question < len(questions):
        display_question()

# função exibir próxima pergunta
def display_question():
    question, option1, option2, option3, option4, answer = questions[current_question]
    question_label.config(text=question)
    option1_btn.config(text=option1, state=tk.NORMAL, command=lambda:check_answer(1))
    option2_btn.config(text=option2, state=tk.NORMAL, command=lambda:check_answer(2))
    option3_btn.config(text=option3, state=tk.NORMAL, command=lambda:check_answer(3))
    option4_btn.config(text=option4, state=tk.NORMAL, command=lambda:check_answer(4))


    correct_answer.set(answer)



# janela interface
janela=tk.Tk()
janela.title("Quiz")
janela.geometry('400x450')

# definindo cores
background_color = "#ECECEC"
text_color = "#333333"
button_color = "#4CAF50"
button_text_color = "#FFFFFF"


# configurações janela
janela.config(bg=background_color)
janela.option_add('*Font', 'Arial')

# Icone Tela
app_icon = PhotoImage(file="quizicone.png")
app_label = tk.Label(janela, image=app_icon, bg=background_color)
app_label.pack(pady=10)

# Componentes da interface
question_label = tk.Label(janela, text="", wraplength=380, bg=background_color, fg=text_color, font=("Arial", 12, "bold"))
question_label.pack(pady=20)

correct_answer = tk.IntVar()

# botões
option1_btn = tk.Button(janela, text="", width=30, bg=button_color, fg=button_text_color, state=tk.DISABLED, font=("Arial",10, "bold"))
option1_btn.pack(pady=10)

option2_btn = tk.Button(janela, text="", width=30, bg=button_color, fg=button_text_color, state=tk.DISABLED, font=("Arial",10, "bold"))
option2_btn.pack(pady=10)

option3_btn = tk.Button(janela, text="", width=30, bg=button_color, fg=button_text_color, state=tk.DISABLED, font=("Arial",10, "bold"))
option3_btn.pack(pady=10)
                    
option4_btn = tk.Button(janela, text="", width=30, bg=button_color, fg=button_text_color, state=tk.DISABLED, font=("Arial",10, "bold"))
option4_btn.pack(pady=10)
                                       
play_again_btn = tk.Button(janela, text="Jogar Novamente", width=30, bg=button_color, fg=button_text_color, font=("Arial",10, "bold"))
play_again_btn.pack(pady=10)
                    
                        
display_question()
janela.mainloop()


