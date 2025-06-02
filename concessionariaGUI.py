import sys
import datetime
import random
import time
from datetime import datetime
from datetime import timedelta
from PyQt5.QtWidgets import QApplication, QMainWindow,QLineEdit
from PyQt5.QtCore import QTimer,Qt
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPushButton,QGridLayout,QWidget,QVBoxLayout

class MainWindow(QWidget):
	def __init__(self):
		super().__init__()
		self.setGeometry(700,300,300,150)
		self.Texto = QLabel("O que você deseja fazer?",self)
		self.botao1 = QPushButton("COMPRA",self)
		self.botao2 = QPushButton("VENDA",self)
		self.botao3 = QPushButton("ALUGUEL",self)
		self.botao5 = QPushButton("PLANILHA",self)
		self.botao4 = QPushButton("SAIR",self)

		self.line_edit = QLineEdit(self)
		self.botaoLE = QPushButton("SUBMIT",self)
		self.comp = QLabel("Que carro você gostaria de comprar?",self)
		self.vend = QLabel("Qual o nome do carro que você deseja vender?",self)

		self.line_edit.hide()
		self.botaoLE.hide()
		self.comp.hide()
		self.vend.hide()

		self.lista=[["MUSTANG","FERRARI","LAMBORGHINI","BULGATI","LIMOUSINE"],
        [10000,15000,14000,20000,40000],
        [1,1,1,1,1]]
		self.caixa=[15000]

		self.initUI()

	def initUI(self):
		self.vbox = QVBoxLayout()

		self.vbox.addWidget(self.Texto)
		self.vbox.addWidget(self.botao1)
		self.vbox.addWidget(self.botao2)
		self.vbox.addWidget(self.botao3)
		self.vbox.addWidget(self.botao5)
		self.vbox.addWidget(self.botao4)

		self.setLayout(self.vbox)

		self.Texto.setAlignment(Qt.AlignCenter)

		self.Texto.setStyleSheet("font-size:15px; font-family:Comic Sans MS;")
		self.setStyleSheet("""
					QPushButton{ font-size:15px;
					font-family:Comic Sans MS;
					}
				""")
		self.botao1.clicked.connect(self.compra)
		self.botao2.clicked.connect(self.venda)
		self.botao3.clicked.connect(self.aluguel)
	
	def compra(self):
		self.some()

		self.comp.show()
		self.line_edit.show()
		self.botaoLE.show()

		self.vbox.addWidget(self.comp)
		self.vbox.addWidget(self.line_edit)
		self.vbox.addWidget(self.botaoLE)

		self.setLayout(self.vbox)

		self.comp.setAlignment(Qt.AlignCenter)

		self.botaoLE.clicked.connect(self.aparece)

		# if self.carroComprado in self.lista[0]:
		# 	self.carroComprado = self.line_edit.text()
		# else:
		# 	self.carroComprado = "Carro não encontrado."

	def venda(self):
		self.some()

		self.vend.show()
		self.line_edit.show()
		self.botaoLE.show()

		self.vbox.addWidget(self.vend)
		self.vbox.addWidget(self.line_edit)
		self.vbox.addWidget(self.botaoLE)

		self.setLayout(self.vbox)

		self.vend.setAlignment(Qt.AlignCenter)

		self.botaoLE.clicked.connect(self.aparece)

	def aluguel(self):
		pass

	def some(self):
		self.Texto.hide()
		self.botao1.hide()
		self.botao2.hide()
		self.botao3.hide()
		self.botao4.hide()
		self.botao5.hide()
	
	def aparece(self):
		self.comp.hide()
		self.line_edit.hide()
		self.botaoLE.hide()

		self.Texto.show()
		self.botao1.show()
		self.botao2.show()
		self.botao3.show()
		self.botao4.show()
		self.botao5.show()

def main():
	aplicativo = QApplication(sys.argv)
	window = MainWindow()
	window.show()
	sys.exit(aplicativo.exec_())
	
if __name__ == "__main__":
	main()