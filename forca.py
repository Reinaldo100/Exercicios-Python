secreta = 'casamento'
digitadas = []
chances = 3

while True:
    letra = input('Digite uma letra: ')

    if chances <= 0:
        print('Voce Pedeu!!!')
        break
    elif letra not in secreta:
        chances -= 1
    print(f'Voce ainda tem {chances} chances.')

    if len(letra) > 1:
        print('Não vale! somente digite uma letra. ')
        continue
    digitadas.append(letra)

    if letra in secreta:
        print(f'Voce acertou!!! a palavra {letra} ')
    else:
        print(f'Vixiii ERROU!!! não existe essa palavra {letra}')
        digitadas.pop()

    secreta_temporario = ''
    for letra_secreta in secreta:
        if letra_secreta in digitadas:
            secreta_temporario += letra_secreta
        else:
            secreta_temporario += '*'

    if secreta_temporario != secreta:
        print(f'A palavra secreta esta assim: {secreta_temporario}')
    else:
        print(f'Voce Ganhou!!! a palavra secreta era assim: {secreta_temporario}')
        break
    

