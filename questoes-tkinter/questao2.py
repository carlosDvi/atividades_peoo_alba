from tkinter import *

def calcular(operacao):
    try:
        v1 = float(campo1.get())
        v2 = float(campo2.get())

        if operacao == "soma":
            resultado = v1 + v2
        elif operacao == "subtracao":
            resultado = v1 - v2
        elif operacao == "multiplicacao":
            resultado = v1 * v2
        elif operacao == "divisao":
            if v2 == 0:
                resultado = "Erro"
            else:
                resultado = v1 / v2

        campo3.config(state="normal")
        campo3.delete(0, END)
        campo3.insert(0, resultado)
        campo3.config(state="disabled")
    except ValueError:
        campo3.config(state="normal")
        campo3.delete(0, END)
        campo3.insert(0, "Inválido")
        campo3.config(state="disabled")

janela = Tk()
janela.title("Calculadora")
janela.geometry("300x150")

rotulo1 = Label(janela, text="Valor 1:")
rotulo1.grid(row=0, column=0)

campo1 = Entry(janela)
campo1.grid(row=0, column=1)

rotulo2 = Label(janela, text="Valor 2:")
rotulo2.grid(row=1, column=0)

campo2 = Entry(janela)
campo2.grid(row=1, column=1)

rotulo3 = Label(janela, text="RESULTADO =")
rotulo3.grid(row=2, column=0)

campo3 = Entry(janela, state="disabled")
campo3.grid(row=2, column=1)

botao_soma = Button(janela, text="Somar", width=10, command=lambda: calcular("soma"))
botao_soma.grid(row=3, column=0)

botao_subtracao = Button(janela, text="Subtrair", width=10, command=lambda: calcular("subtracao"))
botao_subtracao.grid(row=3, column=1)

botao_multiplicacao = Button(janela, text="Multiplicar", width=10, command=lambda: calcular("multiplicacao"))
botao_multiplicacao.grid(row=4, column=0)

botao_divisao = Button(janela, text="Dividir", width=10, command=lambda: calcular("divisao"))
botao_divisao.grid(row=4, column=1)

janela.mainloop()
