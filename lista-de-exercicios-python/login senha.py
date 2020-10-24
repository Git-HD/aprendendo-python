from tkinter import *
from tkinter import messagebox
import pickle

root = Tk()
root.geometry("300x500")
root.title("INSCRIÇÃO")

def registrar():
    text = Label(text='Cadastro De Contas !')
    text_log = Label(text='Digite o usuário:')
    regist_log = Entry()
    text_pass = Label(text='Digite a senha:')
    regist_pass = Entry(show='*')
    text_pass2 = Label(text='Digite novamente:')
    regist_pass2 = Entry(show="*")
    bot_regist = Button(text='Registrar', command=lambda: salvar())
    text.pack()
    text_log.pack()
    regist_log.pack()
    text_pass.pack()
    regist_pass.pack()
    text_pass2.pack()
    regist_pass2.pack()
    bot_regist.pack()

    def salvar():
        login_pass_save = {}
        login_pass_save[regist_log.get()] = regist_pass.get()
        f = open("login.txt", "wb")
        pickle.dump(login_pass_save, f)
        f.close()
        login()

def login():
    text_log = Label(text='ENTRAR')
    text_enter_login = Label(text='Nome de usuário:')
    enter_login = Entry()
    text_enter_pass = Label(text='Senha:')
    enter_pass = Entry(show="*")
    bot_enter = Button(text='ACESSAR', command=lambda: log_pass())
    text_log.pack()
    text_enter_login.pack()
    enter_login.pack()
    text_enter_pass.pack()
    enter_pass.pack()
    bot_enter.pack()

    def log_pass():
        f = open('login.txt', 'rb')
        a = pickle.load(f)
        f.close()
        if enter_login.get() in a:
            if enter_pass.get() == a[enter_login.get()]:
                messagebox.showinfo('Bem vindo', 'CADASTRO REALIZADO')
            else:
                messagebox.showerror('Erro', 'Você digitou a senha errada')

registrar()

root.mainloop()