lista = [
    ['P1', 13],
    ['P2', 6],
    ['P3', 7],
    ['P4', 8],
    ['P5', 50],
    ['P6', 9],
]

#def func(item):
#   return item [1]

lista.sort(key=lambda item: item[1], reverse=False)
print(lista)


funcao = [
    ['Reinaldo'],
    ['Renata'],
    ['Amanda'],
]
funcao.sort(key=lambda i: i[0], reverse=False)
print(funcao)

