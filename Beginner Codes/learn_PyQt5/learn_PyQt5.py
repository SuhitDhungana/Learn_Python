import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__() 
        self.setWindowTitle("My first GUI!") # Sets title for our window
        self.setGeometry(0, 0, 500, 500) # Sets where the window will load initially (x, y, width, height)
        self.setWindowIcon(QIcon("D:\SUHIT\Coding\Learn_Python\Beginner Codes\learn_PyQt5\Goofy Dog Pictures.gif")) # Sets Window's icon's picture
    

def main():
    app = QApplication(sys.argv) 
    window = MainWindow() # Opens a window
    window.show() # Shows the window for longer time
    sys.exit(app.exec_())
    
    
if __name__ == "__main__":
    main()