def subtracao(x, y):
    z = x-y
    print('O resultado da subtração é:', z)

def divisao(x, y):
    if y == 0:
        print("Não é possível dividir por zero")
    else:
        z = x / y
        print('O resultado da divisão é:', z)

def multiplicacao(x, y):
    z = x * y
    print('O resultado da multiplicação é:', z)

def soma(x, y):
    z = x + y
    print('O resultado da soma é:', z)

def calculadora():
    numero_1 = int(input("Digite o primeiro número: "))
    numero_2 = int(input("Digite o segundo número: "))
    
    operacao = input("Escolha a operação (multiplicacao/soma/subtracao/divisao): ").lower()

    if operacao == 'multiplicacao':
        multiplicacao(numero_1, numero_2)
    elif operacao == 'subtracao':
        subtracao(numero_1, numero_2)
    elif operacao == 'divisao':
        divisao(numero_1, numero_2)
    elif operacao == 'soma':
        soma(numero_1, numero_2)
    else:
        print("Operação inválida. Por favor, escolha uma operação válida.")

calculadora()