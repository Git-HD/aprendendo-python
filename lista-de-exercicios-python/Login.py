import os

def readFile(file_name):
	arquivo = open(file_name, "r+")
	file = arquivo.readlines()
	arquivo.close()
	return file

def writeFile(file_name, txt):
	arquivo = open(file_name, "a+")
	arquivo.writelines(txt)
	arquivo.close()

def writeUser(login, password, cpf, bdate, education):
	user = login + ";" + password + ";" + cpf + ";" + bdate + ";" + education + ";" +"\n"
	writeFile("users.alho", user)

def validateUser(cpf, password):
	users = readFile("users.alho")
	for user in users:
		user_as_list = user.split(";")
		if user_as_list[1] == password and user_as_list[2] == cpf:
			return True 
	return False

def login():
	c = input("CPF: ")
	p = input("Pass: ")

	valid = validateUser(c, p)
	
	if valid:
		loginMenu()
	

def registerUser():
	l = input("Login: ")
	p = input("Pass: ")
	c = input("CPF: ")
	b = input("Birthdate: ")
	e = input("Education: ")
	
	writeUser(l,p,c,b,e)
	print("Registrado com sucesso!")

def meu_exit():
	print("Até logo!")

def searchUsersByYear(year):
	
	result = []
	all_users = readFile("users.alho")
	
	for user in all_users:
		user_as_list = user.split(";")
		bdate = user_as_list[3]
		bdate_as_list = bdate.split("-")
		user_year = int(bdate_as_list[2])
		if user_year >= year:
			result.append(user_as_list)
	return result

def searchYear():
	y = int(input("Year: "))
	
	result = searchUsersByYear(y)
	
	print(result)

def loginMenu():
	
	lm_options = {"1": searchYear, "0": meu_exit}
	
	option = "ENTRA"
	
	while option != "0":
		
		option = input("O que deseja fazer? \n"+
		      "1. Buscar por ano\n" +
		      "2. -------\n" +
		      "0. Sair\n ")
		
		lm_options[option]() 

def mainMenu():
	
	menu_option = {"1": registerUser, "2": login, "0": meu_exit}	
	
	option = "ENTRA"
	
	while option != "0":
		
		option = input("O que deseja fazer? \n"+
		      "1. Cadastrar \n" +
		      "2. Login \n" +
		      "0. Sair\n ")
		
		menu_option[option]() 
	
	
mainMenu()
