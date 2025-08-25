import tkinter as tk


def clicar(botao):
    if botao == "C":
        entrada.delete(0, tk.END)  
    elif botao == "=":
        try:
            resultado = eval(entrada.get())
            entrada.delete(0, tk.END)
            entrada.insert(tk.END, str(resultado))
        except:
            entrada.delete(0, tk.END)
            entrada.insert(tk.END, "Erro")
    else:
        entrada.insert(tk.END, botao)  


janela = tk.Tk()
janela.title("Calculadora")
janela.configure(bg="#2b2b2b")  


entrada = tk.Entry(
    janela, width=20, borderwidth=0,
    font=("Arial", 24), justify="right",
    bg="#3c3c3c", fg="white", insertbackground="white"
)
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=20, sticky="nsew")


botoes = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]


cores = {
    "numero": "#4a4a4a",
    "operador": "#f39c12",
    "funcao": "#e74c3c",
    "igual": "#27ae60"
}

row_val = 1
col_val = 0


for botao in botoes:
    if botao.isdigit():  
        cor_bg = cores["numero"]
    elif botao in ["/", "*", "-", "+"]:
        cor_bg = cores["operador"]
    elif botao == "=":
        cor_bg = cores["igual"]
    else:
        cor_bg = cores["funcao"]

    tk.Button(
        janela,
        text=botao,
        font=("Arial", 18, "bold"),
        bg=cor_bg,
        fg="white",
        activebackground="#666",
        activeforeground="white",
        bd=0,
        relief="flat",
        command=lambda b=botao: clicar(b)
    ).grid(row=row_val, column=col_val, sticky="nsew", padx=5, pady=5, ipadx=10, ipady=10)

    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

for i in range(4):
    janela.grid_columnconfigure(i, weight=1)
for i in range(row_val+1):
    janela.grid_rowconfigure(i, weight=1)

janela.mainloop()
