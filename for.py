tabuada = int(input('Digite um numero para mostrar a tabuada: '))
print('Tabuada do numero ', tabuada)


for valor in range(1,11,1):
    print(str(tabuada) + ' x ' + str(valor) + ' = ' + str((tabuada*valor)))
    

numero = int(input('Digite um numero: '))

while numero < 101:
    print('\t' + str(numero))
    numero = numero + 1
print('Laco Encerrado! ')
