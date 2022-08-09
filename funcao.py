def func():
    outra_variavel = 'Reinaldo augusto'
    return outra_variavel

def func2(arg):
    print(arg)

var = func()
func2(var)

print('*******************')

def ola():
    return 'Ola mundo!'

def mestre(funcao):
    return funcao()

print(ola())

print('*********************')

def mestra(func, *args, **kwargs):
    return func(*args, **kwargs)

def fala_oi(nome):
    return f'Oi {nome}'

def saudacao(nome, saudacao):
    return f'{nome} {saudacao}'

executando = mestra(fala_oi, 'Luiz')
executando2 = mestra(saudacao, 'Luiz,', 'Bom dia!')
print(executando)
print(executando2)

print('*******************************')

def besta(func, *args, **kwargs):
    return func(*args, **kwargs)

def trouxa(nome):
    return f'Seu Bosta! {nome}'

mostra = besta(trouxa, 'Reinaldo')
print(mostra)

def olha(func, *args, **kwargs):
    return func(*args, **kwargs)

def hora(name):
    return f'Parabens... {name}'

aplica = olha(hora, 'Renata!')
print(aplica)