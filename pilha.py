class celula():
    def __init__(self):
        self.valor = None
        self.chave = None

class Pilha:
    def __init__(self):
        self.topo = None

    def push(self, x):
        nova = celula()
        nova.valor = x
        nova.chave = self.topo
        self.topo = nova

    def pop(self):
        if self.topo != None:
            x = self.topo.valor
            self.topo = self.topo.chave
            return x
        else:
            return "Pilha Vazia!"

    def imprime(self):
        x = self.topo

        while x.chave != None:
            print(x.valor)
            x = x.chave
        print(x.valor)
    
    def insere(self, v):
        for x in v:
            self.push(x)

    def remove(self, x):
        w = []
        for i in range(x):
            r = self.pop()
            if r != "Pilha Vazia!":
                w.append(r)
        return w

p = Pilha()
v = [10, 20, 30, 40, 50]
p.insere(v)
p.imprime()
w = p.remove(10)
print(w)
