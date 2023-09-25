import tkinter as tk
from tkinter import messagebox
import winsound

senha_atual = 1
senhas_anteriores = []


def gerar_senha():
    global senha_atual
    senha_atual += 1
    if senha_atual == 1000:
        senha_atual = 1
    return senha_atual

def chamar_senha():
    global senha_atual
    senha_atual = gerar_senha()
    senhas_anteriores.append(senha_atual)
    if len(senhas_anteriores) > 3:
        senhas_anteriores.pop(0)  # Remove a mais antiga se houver mais de 3
    winsound.PlaySound('sistema\som.wav', winsound.SND_FILENAME) # Toca o alerta
    atualizar_senhas()


def resetar_senha():
    resposta = messagebox.askquestion("Resetar senha", "Deseja resetar a senha para 001?")
    if resposta == "yes":
        global senha_atual, senhas_anteriores
        senha_atual = 1
        senhas_anteriores = []
        atualizar_senhas()


def emitir_alerta():
    winsound.PlaySound('sistema\som.wav', winsound.SND_FILENAME) # Toca o alerta

def resetar_senha():
    resposta = messagebox.askquestion("Resetar senha", "Deseja resetar a senha para 001?")
    if resposta == "yes":
        global senha_atual, senhas_anteriores
        senha_atual = 1
        senhas_anteriores = []
        atualizar_senhas()

def atualizar_senhas():
    lbl_senha_atual_exibicao.config(text=f"Senha atual: {senha_atual:03d}")

    for i in range(3):
        if i < len(senhas_anteriores):
            senha_anterior = senhas_anteriores[i] - 1
            if senha_anterior > 0:
                lbl_senhas_anteriores[i].config(text=f"{senha_anterior:03d}")
            else:
                lbl_senhas_anteriores[i].config(text="---")
        else:
            lbl_senhas_anteriores[i].config(text="---")

    lbl_senha_atual_atendente.config(text=f"Senha atual: {senha_atual:03d}")

    for i in range(3):
        if i < len(senhas_anteriores):
            senha_anterior = senhas_anteriores[i] - 1
            if senha_anterior > 0:
                lbl_senhas_anteriores[i].config(text=f"{senha_anterior:03d}")
            else:
                lbl_senhas_anteriores[i].config(text="---")
        else:
            lbl_senhas_anteriores[i].config(text="---")

    lbl_senha_atual_atendente.config(text=f"Senha atual: {senha_atual:03d}")

# Janela para a exibição
janela_exibicao = tk.Tk()
janela_exibicao.title("Exibição de Senhas")

lbl_senha_atual_exibicao = tk.Label(janela_exibicao, text="Senha atual:", font=("Arial", 20, "bold"))
lbl_senha_atual_exibicao.pack(pady=10)

quadro_senhas_anteriores = tk.Frame(janela_exibicao)
quadro_senhas_anteriores.pack()

titulo_senhas_anteriores = tk.Label(quadro_senhas_anteriores, text="Senhas Anteriores:", font=("Arial", 16, "bold"))
titulo_senhas_anteriores.grid(row=0, column=0, columnspan=3, pady=5)

lbl_senhas_anteriores = [tk.Label(quadro_senhas_anteriores, text="---", font=("Arial", 14), width=5, relief="solid") for _ in range(3)]
for i, lbl in enumerate(lbl_senhas_anteriores):
    lbl.grid(row=1, column=i, padx=10, pady=5)

# Logo
logo = tk.PhotoImage(file="sistema\imagem.png")
logo = logo.subsample(2, 2)  # Redimensiona a logo
lbl_logo = tk.Label(janela_exibicao, image=logo)
lbl_logo.pack(pady=10)

# Janela para o atendente
janela_atendente = tk.Tk()
janela_atendente.title("Atendente")
janela_atendente.geometry("200x200")  # Mantendo o tamanho da janela

lbl_senha_atual_atendente = tk.Label(janela_atendente, text="Senha atual:", font=("Arial", 16, "bold"))
lbl_senha_atual_atendente.pack()

btn_chamar_senha = tk.Button(janela_atendente, text="Chamar senha", command=chamar_senha, font=("Arial", 14))
btn_chamar_senha.pack(pady=10)

btn_emitir_alerta = tk.Button(janela_atendente, text="Emitir alerta", command=emitir_alerta, font=("Arial", 14))
btn_emitir_alerta.pack(pady=10)

btn_resetar_senha = tk.Button(janela_atendente, text="Resetar senha", command=resetar_senha, font=("Arial", 14))
btn_resetar_senha.pack(pady=10)

# Inicia a atualização das senhas
atualizar_senhas()

janela_exibicao.mainloop()
janela_atendente.mainloop()