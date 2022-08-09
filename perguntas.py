print()

print('Questoes de Matematica ')

perguntas = {
    'Pergunta 1' : {
        'pergunta': 'Quanto eh 2+2? ',
        'respostas' : {'a' : '2', 'b' : '4', 'c' : '6',},
        'resposta_certa' : 'b',
    },
    'Pergunta 2' : {
        'pergunta': 'Quanto eh 5+5? ',
        'respostas' : {'a' : '20', 'b' : '40', 'c' : '10',},
        'resposta_certa' : 'c',
    },
    'Pergunta 3' : {
        'pergunta': 'Quanto eh 10*10? ',
        'respostas' : {'a' : '100', 'b' : '50', 'c' : '110',},
        'resposta_certa' : 'a',
    },
    'Pergunta 4' : {
        'pergunta': 'Quanto eh 50/2? ',
        'respostas' : {'a' : '20', 'b' : '25', 'c' : '60',},
        'resposta_certa' : 'b',
    },
}
print()

respostas_certas = 0

for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')

    print('Respostas: ')

    for rk, rv in pv['respostas'].items():
        print(f'[{rk}]: {rv}')

    resposta_usuario = input('Sua Resposta: ')

    if resposta_usuario == pv['resposta_certa']:
        print('Voce Acertou!!!')
        respostas_certas += 1
    else:
        print('Voce Errou!!!')

    print()

qtd_perguntas = len(perguntas)
porcentagem_acerto = respostas_certas / qtd_perguntas * 100

print(f'Voce Acertou {respostas_certas} das respostas.')
print(f'Sua porcentagem de acertos foram de {porcentagem_acerto}%.')

if porcentagem_acerto < 80:
    print('Desculpe! Tente Outra Vez. ')
else:
    print('Parabens!!! Voce esta Aprovado!')

print()