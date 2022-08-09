import sys
from tkinter import Label
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel

class Janela (QMainWindow):
    
    def __init__(self):
        super(). __init__()

        self.topo = 100
        self.esquerda = 100
        self.largura = 800
        self.altura = 600 
        self.titulo = "Primeira Janela"

        btn = QPushButton('Botão',self) 
        btn.setGeometry(100,100,150,80)

        label = QLabel('Casamento',self)
        label.move(400, 100)
        label.setStyleSheet('fonte-size: 50px')
        label.setStyleSheet('fonte-family 30px')
        label.adjustSize()
        self.CarregarJanela()

    def CarregarJanela(self):
        self.setGeometry(self.esquerda,self.topo,self.largura,self.altura)
        self.setWindowTitle(self.titulo)
        self.show()

aplicacao = QApplication(sys.argv)
j = Janela()
sys.exit(aplicacao.exec_())

