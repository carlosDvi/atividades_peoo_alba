import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage


def mostrar_mensagem():
    texto = entry.get()  
    messagebox.showinfo("Mensagem", f"voce digitou: {texto}")  

#
def sair():
    root.quit()


root = tk.Tk()
root.title("Interface Tkinter")


root.geometry("400x300")


try:
    imagem = PhotoImage(file="imagem.png")
    label_imagem = tk.Label(root, image=imagem)
    label_imagem.pack(pady=10)
except tk.TclError:
    label_imagem = tk.Label(root, text="Imagem não encontrada", fg="red")
    label_imagem.pack(pady=10)


label = tk.Label(root, text="Digite algo:", fg="blue", font=("Helvetica", 14))
label.pack(pady=10)


entry = tk.Entry(root, width=30)
entry.pack(pady=5)


button_mensagem = tk.Button(root, text="Mostrar Mensagem", command=mostrar_mensagem)
button_mensagem.pack(pady=10)


button_sair = tk.Button(root, text="Sair", command=sair, fg="red")
button_sair.pack(pady=10)


root.mainloop()