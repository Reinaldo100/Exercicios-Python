while True:

    numero = input('Digite um numero inteiro: ')
    numero2 = input('Digite outro numero inteiro: ')
    operador = input('Escolha um operador para o calculo: +, -, *, / ')

    if not numero.isnumeric() or not numero2.isnumeric():
        print('Escolha somente numeros inteiros.')

    numero = int(numero)
    numero2 = int(numero2)

    if operador == '+':
        print(numero + numero2)
    elif operador == '-':
        print(numero - numero2)
    elif operador == '*':
        print(numero * numero2)
    elif operador == '/':
        print(numero / numero2)
    else:
        print('Operador Invalido! ')

    sair = input('Deseja sair? [s] ou [n]: ')
    if sair == 's':
        break
    else:
        continue
    
 