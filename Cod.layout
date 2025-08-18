import tkinter as tk

janela = tk.Tk()
janela.title("Calculadora")

entrada = tk.Entry(janela, width=35, borderwidth=5)
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

botoes = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

row_val = 1
col_val = 0

for botao in botoes:
 
    tk.Button(janela, text=botao, padx=20, pady=20).grid(row=row_val, column=col_val)
    
    col_val += 1

    if col_val > 3:
        col_val = 0
        row_val += 1

janela.mainloop()
