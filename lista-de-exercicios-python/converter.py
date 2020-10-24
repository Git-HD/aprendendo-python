import operator
import os
x = {"+": operator.add, "-": operator.sub, "": operator.mul, "/": operator.truediv, "*": operator.pow}
y = {"bin": bin, "oct": oct, "hex": hex}


def conversions():
    try:
        print('-'*51)
        num_to_convert = str(input('Write in a number: '))
        base_num_to_convert = int(input("Write in the number's base: "))
        final_num_base = input('To which base do you want to convert that number?\n'
                               '>').lower()
        if final_num_base == 'decimal':
            return int(num_to_convert, base_num_to_convert)
        else:
            return y[final_num_base](int(num_to_convert, base_num_to_convert))[2:]
    except ValueError:
        return "Input not supported, please try again"
    except TypeError:
        return "Input not supported, please try again"


def calc_repetition():
    try:
        exp = input("Write in expression: ")
        exp = exp.replace("(", " ")
        exp = exp.replace(")", " ")
        exp = exp.replace("[", " ")
        exp = exp.replace("]", " ")
        exp = exp.split()
        le = len(exp)
        if le <= 5:
            n = (x[exp[4]](int(exp[0], int(exp[1])), int(exp[2], int(exp[3]))))
            return n
        else:
            n = (x[exp[4]](int(exp[0], int(exp[1])), int(exp[2], int(exp[3]))))
            c = 5
            v = 6
            z = 7
            item = []
            while c <= len(exp):
                while v <= len(exp):
                    while z <= len(exp):
                        a = int(exp[c], int(exp[v]))
                        b = (x[exp[z]](n, a))
                        n = b
                        c = c+3
                        v = v+3
                        z = z+3
                        item.append(n)
                    return item[-1]
    except ValueError:
        return "Input not supported, please try again"
    except ZeroDivisionError:
        return 'Please, do not divide by zero'
    except IndexError:
        return ('Your entry is not supported. Please try to input in the following sequence:'
                '\nNumber1 Number1_Base Number2_Base Operator1')
    except TypeError:
        return "Input not supported, please try again"


def calc():
    try:
        first_number = input("Write in the first number: ")
        first_base = int(input("Type in the base of the first number: "))
        second_number = input("Write in the second number: ")
        second_base = int(input("Type in the base of the second number: "))
        op = input("Input the arithmetic operational sign: ")
        final = input("Type in the final base (result's base): ")
        if final == "10":
            return x[op](int(first_number, first_base), int(second_number, second_base))
        else:
            return y[final](x[op](int(first_number, first_base), int(second_number, second_base)))[2:]
    except ZeroDivisionError:
        print('Kill yourself!')
        from sys import exit
        exit(0)
    except TypeError:
        return "Input not supported, please try again"
    except ValueError:
        return "Input not supported, please try again"


menu_choices = {1: conversions, 2: calc_repetition, 3: calc}
repeater = -1
print('-'*51, '\nHello there,', '\nThis is a base convert program, please follow the instructions.' + '\n' +
      '-'*51)
os.environ["TERM"] = "xterm-256color"
while repeater != 0:
    try:
        repeater = int(input('Select one of the following options:\n'
                             '\t1 -> Convert'
                             '\n\t2 -> Operate an expression'
                             '\n\t3 -> Operate two numbers'
                             '\n\t4 -> Exit'
                             '\n\t  ->'))
        os.system("clear")
        if repeater == 4:
            exit(0)
        print(menu_choices[repeater]())
    except KeyError:
        print('Your choice is not listed, please, try again'
              '\n' + '-'*51)
    except ValueError:
        print('Your choice is not listed, please, try again'
              '\n' + '-'*51)
    except TypeError:
        print("Input not supported, please try again")


# def calc_decimal():
#     ip = input("insira o primeiro numero")
#     iniciali = int(input("insira a base do primeiro numero"))
#     j = input("insira o segundo numero")
#     inicialj = int(input("insira a base do segundo numero"))
#     op = input("insira a operação")
#     print(x[op](int(ip, iniciali), int(j, inicialj)))
#
#
# def calc_outras_bases():
#     ip = input("insira o primeiro numero")
#     iniciali = int(input("insira a base do primeiro numero"))
#     j = input("insira o segundo numero")
#     inicialj = int(input("insira a base do segundo numero"))
#     op = input("insira a operação")
#     final = input("insira a base final")
#     print((y[final](x[op](int(ip, iniciali), int(j, inicialj))))[2:])
#
# def conversions_decimal():
#     num_to_convert = str(input('Write in a number: '))
#     base_num_to_convert = int(input("Write in the number's base: "))
#     return int(num_to_convert, base_num_to_convert)
#
#
# def conversions_other_bases():
#     num_to_convert = str(input('Write in a number: '))
#     base_num_to_convert = int(input("Write in the number's base: "))
#     final_num_base = input('To which base do you want to convert that number?\n'
#                            '-> ').lower()
#     return y[final_num_base](int(num_to_convert, base_num_to_convert))[2:]

# Python program to create a simple GUI
# calculator using Tkinter

# import everything from tkinter module
from tkinter import *

# globally declare the expression variable
expression = ""


# Function to update expressiom
# in the text entry box
def press(num):
	# point out the global expression variable
	global expression

	# concatenation of string
	expression = expression + str(num)

	# update the expression by using set method
	equation.set(expression)


# Function to evaluate the final expression
def equalpress():
	# Try and except statement is used
	# for handling the errors like zero
	# division error etc.

	# Put that code inside the try block
	# which may generate the error
	try:

		global expression

		# eval function evaluate the expression
		# and str function convert the result
		# into string
		total = str(eval(expression))

		equation.set(total)

		# initialze the expression variable
		# by empty string
		expression = ""

	# if error is generate then handle
	# by the except block
	except:

		equation.set(" error ")
		expression = ""


# Function to clear the contents
# of text entry box
def clear():
	global expression
	expression = ""
	equation.set("")


# Driver code
if __name__ == "__main__":
	# create a GUI window
	gui = Tk()

	# set the background colour of GUI window
	gui.configure(background="light green")

	# set the title of GUI window
	gui.title("Simple Calculator")

	# set the configuration of GUI window
	gui.geometry("265x125")

	# StringVar() is the variable class
	# we create an instance of this class
	equation = StringVar()

	# create the text entry box for
	# showing the expression .
	expression_field = Entry(gui, textvariable=equation)

	# grid method is used for placing
	# the widgets at respective positions
	# in table like structure .
	expression_field.grid(columnspan=4, ipadx=70)

	equation.set('enter your expression')

	# create a Buttons and place at a particular
	# location inside the root window .
	# when user press the button, the command or
	# function affiliated to that button is executed .
	button1 = Button(gui, text=' 1 ', fg='black', bg='red',
					command=lambda: press(1), height=1, width=7)
	button1.grid(row=2, column=0)

	button2 = Button(gui, text=' 2 ', fg='black', bg='red',
					command=lambda: press(2), height=1, width=7)
	button2.grid(row=2, column=1)

	button3 = Button(gui, text=' 3 ', fg='black', bg='red',
					command=lambda: press(3), height=1, width=7)
	button3.grid(row=2, column=2)

	button4 = Button(gui, text=' 4 ', fg='black', bg='red',
					command=lambda: press(4), height=1, width=7)
	button4.grid(row=3, column=0)

	button5 = Button(gui, text=' 5 ', fg='black', bg='red',
					command=lambda: press(5), height=1, width=7)
	button5.grid(row=3, column=1)

	button6 = Button(gui, text=' 6 ', fg='black', bg='red',
					command=lambda: press(6), height=1, width=7)
	button6.grid(row=3, column=2)

	button7 = Button(gui, text=' 7 ', fg='black', bg='red',
					command=lambda: press(7), height=1, width=7)
	button7.grid(row=4, column=0)

	button8 = Button(gui, text=' 8 ', fg='black', bg='red',
					command=lambda: press(8), height=1, width=7)
	button8.grid(row=4, column=1)

	button9 = Button(gui, text=' 9 ', fg='black', bg='red',
					command=lambda: press(9), height=1, width=7)
	button9.grid(row=4, column=2)

	button0 = Button(gui, text=' 0 ', fg='black', bg='red',
					command=lambda: press(0), height=1, width=7)
	button0.grid(row=5, column=0)

	plus = Button(gui, text=' + ', fg='black', bg='red',
				command=lambda: press("+"), height=1, width=7)
	plus.grid(row=2, column=3)

	minus = Button(gui, text=' - ', fg='black', bg='red',
				command=lambda: press("-"), height=1, width=7)
	minus.grid(row=3, column=3)

	multiply = Button(gui, text=' * ', fg='black', bg='red',
					command=lambda: press("*"), height=1, width=7)
	multiply.grid(row=4, column=3)

	divide = Button(gui, text=' / ', fg='black', bg='red',
					command=lambda: press("/"), height=1, width=7)
	divide.grid(row=5, column=3)

	equal = Button(gui, text=' = ', fg='black', bg='red',
				command=equalpress, height=1, width=7)
	equal.grid(row=5, column=2)

	clear = Button(gui, text='Clear', fg='black', bg='red',
				command=clear, height=1, width=7)
	clear.grid(row=5, column='1')


	# start the GUI
	gui.mainloop()
