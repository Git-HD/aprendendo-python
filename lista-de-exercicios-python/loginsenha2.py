from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("300x500")
root.title("CADASTRO")


def writeFile(file_name, txt):
    arquivo = open(file_name, "rb")
    arquivo.writelines(txt)
    arquivo.close()


def registrar():
    text = Label(text='Cadastro De Contas !')
    text_log = Label(text='Digite o usuário')
    regist_log = Entry()
    text_pass = Label(text='Digite a senha')
    regist_pass = Entry()
    text_pass2 = Label(text='Digite novamente')
    regist_pass2 = Entry(show="*")
    bot_regist = Button(text='Registrar')
    text.pack()
    text_log.pack()
    regist_log.pack()
    text_pass.pack()
    regist_pass.pack()
    text_pass2.pack()
    regist_pass2.pack()
    bot_regist.pack()

registrar()

root.mainloop()
