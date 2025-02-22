import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget # Importing the essential functions / widgets # Importing for managing layouts    
''' Note: The imports (sys, QApplication, QMainWindow) are the most essential, for they are needed everytime'''

from PyQt5.QtGui import QIcon, QFont, QPixmap  # Importing GUI related functions
# QPixMap works with images and stuff

from PyQt5.QtCore import Qt # Useful for alignment


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__() 
        self.setWindowTitle("My first GUI!") # Sets title for our window
        self.setGeometry(0, 0, 700, 700) # Sets where the window will load initially (x, y, width, height)
        self.setWindowIcon(QIcon("D:\SUHIT\Coding\Learn_Python\Beginner Codes\learn_PyQt5\Goofy Dog Pictures.gif")) # Sets Window's icon's picture
        label = QLabel(self) # Sets the label (self refers to the 'window' object)
        label.setFont(QFont("Times New Roman", 30)) # Sets the font and size of the font (Font_name, font_size)
        label.setGeometry(100, 100, 200, 200) # Set position of label (x, y, width, height)
        label.setStyleSheet("color: black;" # CSS-like styling (we can use RGB values for color/background-color)
                            "background-color: blue;"
                            "font-weight: bold;"
                            "font-style: italic;"
                            "text-decoration: underline;")

        # For Vertical Alignments
        ''' label.setAlignment(Qt.AlignTop) # Aligns vertically at top
        label.setAlignment(Qt.AlignBottom) # Align vetically at bottom
        label.setAlignment(Qt.AlignVCenter) # Align vertically at center'''

        # For Horizontal Alignments
        '''label.setAlignment(Qt.AlignRight) # Aligns horizontally at right
        label.setAlignment(Qt.AlignLeft) # Aligns horizontally at left 
        label.setAlignment(Qt.AlignHCenter) # Aligns horizontally at center'''
        
        # For aligning horizontally and vertically simultaneously
        '''label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)'''
        
        # Trick for aligning in center directly
        label.setAlignment(Qt.AlignCenter)
        
        pixmap = QPixmap("D:\SUHIT\Coding\Learn_Python\Beginner Codes\learn_PyQt5\Goofy Dog Pictures.gif")
        label.setPixmap(pixmap) # Assigning the pixmap to label
        label.setScaledContents(True) # Set scale of pixmap to size of label (it wasn't before this)
        label.setGeometry(0, 0, label.width(), label.height()) # Set geometry of the image
        '''Note: for right-most x, do "self.width() - label.width()"
                 for bottom-most y, do "self.height() - label.height()"
                 for center y, x, do "self.height(OR width)() - label.height(OR width)() // 2"'''
        
        
        
def main():
    app = QApplication(sys.argv) 
    window = MainWindow() # Opens a window
    window.show() # Shows the window for longer time
    sys.exit(app.exec_()) # Exits the window
    
    
if __name__ == "__main__":
    main()
