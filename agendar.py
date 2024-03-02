# Importe a biblioteca Tkinter
import tkinter as tk
from tkinter import messagebox

# Função para agendar o horário
def agendar_horario():
    nome_cliente = entry_nome.get()
    horario_desejado = entry_horario.get()

    # Valide os campos (você pode adicionar mais validações aqui)
    if not nome_cliente or not horario_desejado:
        messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
        return

    # Salve os detalhes do agendamento (substitua isso pela sua lógica)
    with open("agendamentos.txt", "a") as arquivo:
        arquivo.write(f"Cliente: {nome_cliente}, Horário: {horario_desejado}\n")

    # Exiba uma mensagem de sucesso
    messagebox.showinfo("Sucesso", f"Agendamento para {nome_cliente} às {horario_desejado} realizado!")

# Crie a janela principal
root = tk.Tk()
root.title("Agendamento de Horário na Barbearia")

# Crie rótulos e campos de entrada
label_nome = tk.Label(root, text="Nome do Cliente:")
entry_nome = tk.Entry(root)
label_horario = tk.Label(root, text="Horário Desejado:")
entry_horario = tk.Entry(root)

# Crie um botão para agendar o horário
botao_agendar = tk.Button(root, text="Agendar", command=agendar_horario)

# Organize os widgets usando o layout grid
label_nome.grid(row=0, column=0, padx=10, pady=10)
entry_nome.grid(row=0, column=1, padx=10, pady=10)
label_horario.grid(row=1, column=0, padx=10, pady=10)
entry_horario.grid(row=1, column=1, padx=10, pady=10)
botao_agendar.grid(row=2, columnspan=2, padx=10, pady=10)

# Inicie o loop principal do evento
root.mainloop()
