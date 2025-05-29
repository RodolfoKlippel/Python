from PyQt5.QtWidgets import QApplication,QMainWindow,QLabel,QWidget
from PyQt5.QtGui import QPixmap
import sys

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setGeometry(700,300,1000,600)
		self.label1 = QLabel("",self)
		self.label2 = QLabel("",self)
		self.label3 = QLabel("",self)
		self.label4 = QLabel("",self)
		self.label5 = QLabel("",self)
		self.label6 = QLabel("",self)
		self.label7 = QLabel("",self)
		self.label8 = QLabel("",self)
		self.label9 = QLabel("",self)
		self.label10 = QLabel("",self)
		self.label11 = QLabel("",self)
		self.label12 = QLabel("",self)
		labelp = QLabel(self)
		
		
		self.label1.setGeometry(10,0,1000,100)
		self.label1.setStyleSheet("background-color: #E62929")
		self.label2.setGeometry(10,100,1000,100)
		self.label2.setStyleSheet("background-color: #FF8C30")
		self.label3.setGeometry(10,200,1000,100)
		self.label3.setStyleSheet("background-color: #FBFF30")
		self.label4.setGeometry(10,300,1000,100)
		self.label4.setStyleSheet("background-color: #5FCF03")
		self.label5.setGeometry(10,400,1000,100)
		self.label5.setStyleSheet("background-color: #034ACF")
		self.label6.setGeometry(10,500,1000,100)
		self.label6.setStyleSheet("background-color: #8B45AB")
		self.label7.setGeometry(500,0,1000,100)
		self.label7.setStyleSheet("background-color: #50E3F6")
		self.label8.setGeometry(500,100,1000,100)
		self.label8.setStyleSheet("background-color: #FFA4F1")
		self.label9.setGeometry(500,200,1000,100)
		self.label9.setStyleSheet("background-color: white")
		self.label10.setGeometry(500,300,1000,100)
		self.label10.setStyleSheet("background-color: white")
		self.label11.setGeometry(500,400,1000,100)
		self.label11.setStyleSheet("background-color: #FFA4F1")
		self.label12.setGeometry(500,500,1000,100)
		self.label12.setStyleSheet("background-color: #50E3F6")
		labelp.setGeometry(375,200,250,250)
		pixmap = QPixmap("download.png")
		labelp.setPixmap(pixmap)
		labelp.setScaledContents(True)
	
		
def Main():
	app = QApplication([])
	window = MainWindow()
	window.show()
	sys.exit(app.exec_())
	
if __name__=="__main__":
	Main()
