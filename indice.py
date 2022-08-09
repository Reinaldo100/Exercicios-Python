clubes = []
cidade = []
estado = []
pais = []
resposta = 'S'

while resposta == 'S':
    clubes.append(input('Nome do clube: '))
    cidade.append(input('Nome da cidade: '))
    estado.append(input('Estado: '))
    pais.append(input('Pais Origem: '))
    resposta = input('Digite \'S\' para continuar: ').upper()

for indice in range(0, len(clubes)):
    print('\nClube..: ', (indice+1))
    print('Nome..: ', clubes[indice])
    print('Cidade..: ', cidade[indice])
    print('Estado..: ', estado[indice])
    print('Pais..: ', pais[indice])
