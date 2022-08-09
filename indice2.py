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

busca = input('\nDigite o nome do Clube que deseja buscar: ')
for indice in range(0, len(clubes)):
    if busca == clubes[indice]:
        print('Cidade..: ', cidade[indice])
        print('Pais..: ', pais[indice])

       
