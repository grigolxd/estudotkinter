import tkinter as tk
from tkinter import messagebox

# Criar a janela principal
root = tk.Tk()
root.title("Exemplo de Gerenciadores de Layout")
root.geometry("400x300")

# Usando pack() para adicionar um título
title_label = tk.Label(root, text="Gerenciadores de Layout no Tkinter", font=("Arial", 14))
title_label.pack(pady=10)

# Criar um Frame para usar grid()
grid_frame = tk.Frame(root)
grid_frame.pack(pady=10)

# Usando grid() para adicionar rótulos e campos de entrada no Frame
tk.Label(grid_frame, text="Nome:").grid(row=0, column=0, padx=10, pady=10)
name_entry = tk.Entry(grid_frame)
name_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(grid_frame, text="Idade:").grid(row=1, column=0, padx=10, pady=10)
age_entry = tk.Entry(grid_frame)
age_entry.grid(row=1, column=1, padx=10, pady=10)

# Usando place() para adicionar um botão
submit_button = tk.Button(root, text="Enviar", command=lambda: enviar_dados())
submit_button.place(x=150, y=200)

# Função para coletar dados e exibir mensagem
def enviar_dados():
    nome = name_entry.get()
    idade = age_entry.get()
    messagebox.showinfo("Dados Enviados", f"Nome: {nome}\nIdade: {idade}")

# Iniciar o loop da interface
root.mainloop()