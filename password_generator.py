# Gerador de senhas criado em Python

import random

class Usuario():
    def __init__(self, Nome, Senha):
        self.Nome = Nome
        self.Senha = Senha

nome = input("Digite seu nome: ")

list_char = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m"
            , "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z" ]
random.shuffle(list_char)
list_special = ["!", "@", "#", "$", "%", "&", "*", "-", "_", "+", "=", "?" ]
random.shuffle(list_special)
list_number = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
random.shuffle(list_number)
list_total = []

def qt_char_upp():
    print("Quantos caracteres maiusculos tera sua senha? ")

    i = 1
    
    while i != 0:
        try:
            qt_upp = int(input())
            if 0 <= qt_upp <= 10:
                for j in range(qt_upp):  
                    list_total.append(list_char[j].upper())
                    random.shuffle(list_char)
                i -= 1
            else:
                print("Por favor, escolha um numero valido.")

        except ValueError:
            print("Sua entrada eh invalida. Digite um numero inteiro.")


def qt_char_low():
    print("Quantos caracteres minusculos tera sua senha? ")


    i = 1
    
    while i != 0:
        try:
            qt_low = int(input())
            if 0 <= qt_low <= 10:
                for j in range(qt_low):  
                    list_total.append(list_char[j].lower())
                    random.shuffle(list_char)
                i -= 1
            else:
                print("Por favor, escolha um numero valido.")

        except ValueError:
            print("Sua entrada eh invalida. Digite um numero inteiro.")


                
def qt_special():
    print("Quantos caracteres especiais tera sua senha? ")


    i = 1
    
    while i != 0:
        try:
            qt_special = int(input())
            if 0 <= qt_special <= 10:
                for j in range(qt_special):  
                    list_total.append(list_special[j])
                    random.shuffle(list_char)
                i -= 1
            else:
                print("Por favor, escolha um numero valido.")

        except ValueError:
            print("Sua entrada eh invalida. Digite um numero inteiro.")



def qt_number():
    print("Quantos caracteres numericos tera sua senha? ")


    i = 1
    
    while i != 0:
        try:
            qt_number = int(input())
            if 0 <= qt_number <= 10:
                for j in range(qt_number):  
                    list_total.append(list_number[j])
                    random.shuffle(list_char)
                i -= 1
            else:
                print("Por favor, escolha um numero valido.")

        except ValueError:
            print("Sua entrada eh invalida. Digite um numero inteiro.")

def print_password(usuario):
    print("A senha de {0} é {1}".format(usuario.Nome, usuario.Senha))

print("Olá, bem vindo ao gerador de senhas! \n")
qt_char_upp()
qt_char_low()
qt_special()
qt_number()

random.shuffle(list_total)
password = "".join(list_total)
usuario = Usuario(nome, password)
print_password(usuario)


