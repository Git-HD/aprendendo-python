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