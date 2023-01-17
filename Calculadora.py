from tkinter import *
from tkinter import ttk

#Definindo Cores 
cor1 = "#4d4b47" #cinza
cor2 = "#fcfcfc" #branca
cor3 = "#eb9617" #laranja
cor4 = "#1773eb" #azul
cor5 = "#000308" #preto

#Criando Janelas
janela =Tk()
janela.title("Calculadora")
janela.geometry("235x310")
janela.config(bg=cor1)

#Criando Frames 
frame_tela = Frame(janela, width=235, height=50, bg=cor2)
frame_tela.grid(row=0, column=0)

#Criando o Corpo
frame_corpo = Frame(janela, width=235, height=268)
frame_corpo.grid(row=1, column=0)

#varialvel todos valores
todos_valores = ''

valor_texto = StringVar()
#Criando Função
def entrar_valores(event):

    global todos_valores

    todos_valores = todos_valores + str(event)
    
    valor_texto.set(str(todos_valores))

#Função que irá validar

def calcular():
    resultado = eval(todos_valores)
    valor_texto.set(str(resultado))

#Função limpar Tela

def limpar_tela():
    global todos_valores
    todos_valores = ""
    valor_texto.set("")




#Criando label

app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 18 '), bg=cor1, fg=cor2)
app_label.place(x=0, y=0)
#Criando Botões

b_1 = Button(frame_corpo, command=limpar_tela, text="C", width=13, height=2)
b_1.place(x=0, y=0)
b_2 = Button(frame_corpo, command=lambda: entrar_valores('%'), text="%", width=8, height=2)
b_2.place(x=105, y=0)
b_3 = Button(frame_corpo, command=lambda: entrar_valores('/'), text="/", width=6, height=2)
b_3.place(x=180, y=0)
b_3.config(bg=cor3)
b_4 = Button(frame_corpo, command=lambda: entrar_valores('7'), text="7", width=6, height=2)
b_4.place(x=0, y=50)
b_5 = Button(frame_corpo, command=lambda: entrar_valores('4'), text="4", width=6, height=2)
b_5.place(x=0, y=100)
b_6 = Button(frame_corpo, command=lambda: entrar_valores('1'), text="1", width=6, height=2)
b_6.place(x=0, y=150)
b_7 = Button(frame_corpo, command=lambda: entrar_valores('0'), text="0", width=15, height=2)
b_7.place(x=0, y=200)
b_8 = Button(frame_corpo, command=lambda: entrar_valores('8'), text="8", width=6, height=2)
b_8.place(x=60, y=50)
b_9 = Button(frame_corpo, command=lambda: entrar_valores('5'), text="5", width=6, height=2)
b_9.place(x=60, y=100)
b_10 = Button(frame_corpo, command=lambda: entrar_valores('2'), text="2", width=6, height=2)
b_10.place(x=60, y=150)
b_11 = Button(frame_corpo, command=lambda: entrar_valores('9'), text="9", width=6, height=2)
b_11.place(x=120, y=50)
b_12 = Button(frame_corpo, command=lambda: entrar_valores('6'), text="6", width=6, height=2)
b_12.place(x=120, y=100)
b_13 = Button(frame_corpo, command=lambda: entrar_valores('3'), text="3", width=6, height=2)
b_13.place(x=120, y=150)
b_14 = Button(frame_corpo, command=lambda: entrar_valores('*'), text="*", width=6, height=2)
b_14.place(x=180, y=50)
b_14.config(bg=cor3)
b_15 = Button(frame_corpo, command=lambda: entrar_valores('-'), text="-", width=6, height=2)
b_15.place(x=180, y=100)
b_15.config(bg=cor3)
b_16 = Button(frame_corpo, command=lambda: entrar_valores('+'), text="+", width=6, height=2)
b_16.place(x=180, y=150)
b_16.config(bg=cor3)
b_17 = Button(frame_corpo, command=calcular, text="=", width=6, height=2)
b_17.place(x=180, y=200)
b_17.config(bg=cor3)
b_17 = Button(frame_corpo, command=lambda: entrar_valores(','), text=",", width=6, height=2)
b_17.place(x=120, y=200)





janela.mainloop()