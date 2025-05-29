import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPushButton


class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setGeometry(700,300,500,500)

		self.label = QLabel("0",self)
		self.moeda = 0
		self.upg1 = 0
		self.upg2 = 0
		self.upg3 = 0

		self.botão1 = QPushButton("+ Moeda",self)
		self.botão2 = QPushButton("Upgrade 50",self)
		self.botão3 = QPushButton("Upgrade 150",self)
		self.botão4 = QPushButton("Upgrade 300",self)
		self.initUI()
		
	def initUI(self):
		
		self.botão1.setGeometry(200,50,100,80)
		self.botão2.setGeometry(70,300,100,80)
		self.botão3.setGeometry(195,300,100,80)
		self.botão4.setGeometry(320,300,100,80)
		self.label.setGeometry(240,150,50,30)
		self.label.setStyleSheet("font-size:20px; font-family: Comic Sans MS;")

		self.setStyleSheet("""QPushButton{font-size: 15px;
					font-family: Comic Sans Ms;
					border: 2px solid;
					border-radius: 5px;}
					 
					QPushButton:hover{
					background-color: #999e9b;
					}
					""")
		
		self.botão1.clicked.connect(self.dinheiro)
		self.botão2.clicked.connect(self.Upg1)
		self.botão3.clicked.connect(self.Upg2)
		self.botão4.clicked.connect(self.Upg3)

	def dinheiro(self,estado):
		if estado == False:
			self.moeda+=1
			if self.upg1==1:
				self.moeda+=1
			if self.upg2==1:
				self.moeda+=1
			if self.upg3==1:
				self.moeda+=1
			self.label.setText(f"{self.moeda}")
	
	def Upg1(self,estado):
		if estado == False:
			if self.moeda > 50:
				self.moeda-=50
				self.upg1=1
				self.label.setText(f"{self.moeda}")
				self.botão2.setDisabled(True)
	
	def Upg2(self,estado):
		if estado == False:
			if self.moeda > 150:
				self.moeda-=150
				self.upg2=1
				self.label.setText(f"{self.moeda}")
				self.botão3.setDisabled(True)
	
	def Upg3(self,estado):
		if estado == False:
			if self.moeda > 300:
				self.moeda-=300
				self.upg3=1
				self.label.setText(f"{self.moeda}")
				self.botão4.setDisabled(True)

	
def main():
	aplicativo = QApplication(sys.argv)
	window = MainWindow()
	window.show()
	sys.exit(aplicativo.exec_())
	
if __name__ == "__main__":
	main()