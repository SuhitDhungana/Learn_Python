import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, # Essential imports 
                             QWidget, QVBoxLayout, QHBoxLayout, QGridLayout) 
                            # Imports for layout management

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 500, 500)
        self.initUI()
        
    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        label1 = QLabel("1", self) # In these, 'self' isn't mandatory
        label2 = QLabel("2", self)
        label3 = QLabel("3", self)
        label4 = QLabel("4", self)
        label5 = QLabel("5", self)
        
        label1.setStyleSheet("background-color: red;")
        label2.setStyleSheet("background-color: red;")
        label3.setStyleSheet("background-color: red;")
        label4.setStyleSheet("background-color: red;")
        label5.setStyleSheet("background-color: red;")
        

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
    
    
if __name__ == "__main__":
    main()