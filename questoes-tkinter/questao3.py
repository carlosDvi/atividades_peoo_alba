from tkinter import *
from tkinter import messagebox

def validar_login():
    usuario_correto = "admin"
    senha_correta = "12345"

    usuario = campo_usuario.get()
    senha = campo_senha.get()

    if usuario == usuario_correto and senha == senha_correta:
        messagebox.showinfo("Login", "Acesso permitido")
    else:
        messagebox.showerror("Login", "Acesso negado")

janela = Tk()
janela.title("Tela de Login")
janela.geometry("300x150")

rotulo_usuario = Label(janela, text="Usuário:")
rotulo_usuario.grid(row=0, column=0, padx=10, pady=10)

campo_usuario = Entry(janela)
campo_usuario.grid(row=0, column=1)

rotulo_senha = Label(janela, text="Senha:")
rotulo_senha.grid(row=1, column=0, padx=10, pady=10)

campo_senha = Entry(janela, show="*")
campo_senha.grid(row=1, column=1)

botao_entrar = Button(janela, text="Entrar", command=validar_login)
botao_entrar.grid(row=2, column=1, pady=10)

janela.mainloop()
