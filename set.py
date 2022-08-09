#add(adicionar), update(atualizar), clear(limpar), discard(discartar)
#union | (une)
# intersection & (todos os elementos presentes nos dois sets)
# difference - (elementos apenas no set da esquerda)
# symetric_difference ^ (elementos que estão nos dois sets, mas não em ambos)

l1 = [1,2,3,3,3,3,3,3,4,4,5,5,6,7,7,8,9,10,'Reinaldo', 'Augusto', 'Augusto']
l1 = set(l1)
l1 = list(l1)
print(l1)

s1 = {1,2,3,4,5,7}
s2 = {1,2,3,4,5,6,}
s3 = s1 ^ s2

print(s3)


lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 2, 1, 6, 8, 3],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]

def encontra_primeiro_duplicado(param_lista_de_inteiro):
    numeros_checados = set()
    primeiro_duplicado = -1

    for numero in param_lista_de_inteiro:
        if numero in numeros_checados:
            primeiro_duplicado = numero
            break

        numeros_checados.add(numero)

    return primeiro_duplicado

for lista_de_inteiros in lista_de_listas_de_inteiros:
    print(lista_de_inteiros, encontra_primeiro_duplicado(lista_de_inteiros))