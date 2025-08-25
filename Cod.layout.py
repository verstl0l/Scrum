# Função para adicionar um valor à expressão
def adicionar_valor(valor):
    global expressao
    expressao += str(valor)
    entrada.delete(0, tk.END)  # Limpa o campo
    entrada.insert(0, expressao)  # Insere a nova expressão

# Função para calcular a expressão
def calcular():
    global expressao
    try:
        resultado = str(eval(expressao))
        entrada.delete(0, tk.END)
        entrada.insert(0, resultado)
        expressao = resultado
    except:
        entrada.delete(0, tk.END)
        entrada.insert(0, "Erro")
        expressao = ""

# Função para limpar a tela
def limpar():
    global expressao
    expressao = ""
    entrada.delete(0, tk.END)

# Cria a janela principal
janela = tk.Tk()
janela.title("Calculadora")

# Campo de exibição
entrada = tk.Entry(janela, width=35, borderwidth=5)
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Botões de números e operadores
botoes = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

row_val = 1
col_val = 0
for botao in botoes:
    if botao == '=':
        tk.Button(janela, text=botao, padx=20, pady=20, command=calcular).grid(row=row_val, column=col_val)
    elif botao == 'C':
        tk.Button(janela, text=botao, padx=20, pady=20, command=limpar).grid(row=row_val, column=col_val)
    else:
        tk.Button(janela, text=botao, padx=20, pady=20, command=lambda b=botao: adicionar_valor(b)).grid(row=row_val, column=col_val)
    
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

janela.mainloop()
