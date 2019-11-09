#-*- coding: UTF-8 -*-

def HelloWorld():
    # Faça um código que apresente "Hello World" na tela
    print("Hello World")


def BemVindo():
    # Faça um código que solicite nome, sobrenome e idade do usuário.
    # Depois dê uma mensagem de boas-vindas
    # Verifique se ele tem menos ou mais de 18 anos

    nome = input("Nome: ")
    sobrenome = input("Sobrenome: ")
    idade = int(input("Idade: "))

    print("Seja bem-vindo {} {}\n".format(nome, sobrenome))
    if idade < 18 and idade > 0:
        print("Você tem menos de 18 anos!")
    elif idade > 18 and idade < 150:
        print("Você tem mais de 18 anos!")
    else:
        print("Idade inválida!")

def Antecessor_Sucessor():
    # Faça um Programa que peça um número e apresente na tela o antecessor e o sucessor dele.
    numero = float(input("Digite um número: "))
    antecessor = numero - 1
    print("Antecessor: {}".format(antecessor))
    sucessor = numero + 1
    print("Sucessor: {}".format(sucessor))

def Soma_Dois_Numeros():
    # Faça um Programa que peça dois números e imprima a soma deles.
    primeiro_num = float(input("Primeiro número: "))
    segundo_num = float(input("Segundo número: "))
    
    soma = primeiro_num + segundo_num

    print("Resultado de {} + {} = {}".format(primeiro_num, segundo_num, soma))
    
def Media_Notas():
    # Faça um Programa que peça as 4 notas bimestrais e mostre a média aritmética.
    primeira_nota = float(input("Nota 1: "))
    segunda_nota = float(input("Nota 2: "))
    terceira_nota = float(input("Nota 3: "))
    quarta_nota = float(input("Nota 4: "))
    
    soma = primeira_nota + segunda_nota + terceira_nota + quarta_nota
    media = soma / 4

    print("Média {}".format(media))


Media_Notas()
