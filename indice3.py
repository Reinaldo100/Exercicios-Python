inventario = []
resposta = 'S'

while resposta == 'S':
    veiculo = [input('Nome do veiculo: '),
        float(input('Valor: ')),
        int(input('Ano Fabricado: ')),
        input('Cor do veiculo ')]
    inventario.append(veiculo)
    resposta = input('Deseja \'S\' para continuar: ').upper()

for elemento in inventario:
    print('Nome.............: ', elemento[0])
    print('Valor............: ', elemento[1])
    print('Fabricacão.......: ', elemento[2])
    print('Cor Veiculo......: ', elemento[3])

busca = input('\nDigite o nome do Veiculo que deseja buscar: ')
for elemento in inventario:
    if busca == elemento[0]:
        print('Valor........: ', elemento[1])
        print('Fabricação...: ', elemento[2])

depreciacao = input('\nDigite o nome do Veiculo que será depreciado: ')
for elemento in inventario:
    if depreciacao == elemento[0]:
        print('Valor antigo: ', elemento[1])
        elemento[1] = elemento[1] * 0.9
        print('Novo valor: ', elemento[1])

serial = input('\nDigite o nome do veiculo que será excluido: ')
for elemento in inventario:
    if elemento[0] == serial:
        inventario.remove(elemento)

for elemento in inventario:
    print('Nome................: ', elemento[0])
    print('Valor...............: ', elemento[1])
    print('Ano de Fabricação...: ', elemento[2])
    print('Cor Veiculo.........: ', elemento[3])

valores = []
for elemento in inventario:
    valores.append(elemento[1])
if len(valores) > 0:
    print('O Veiculo mais caro custa: ', max(valores))
    print('O Veiculo mais barato custa: ', min(valores))
    print('O total de Veiculos é de: ', sum(valores))