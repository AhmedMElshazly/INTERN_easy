try:
    from GUI.Config import *
except BaseException:
    from Config import *


#---This main window will hold each and every widget after some action (Centeral widget will hold Widgets)---  
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        #---Initiating the Stack --- Widgets will be added to that stack then showen 
        self.central_widget = QStackedWidget()
        self.setCentralWidget(self.central_widget)
        
        #---Set Geometry---
        self.setFixedSize(640, 480)

        #---Set Design---
        # self.setStyleSheet('background-color:#D3D3D3;')

        #--- Set Features---
        self.setWindowTitle("INTERN easy | Goodera")
        self.setWindowIcon(QIcon(QPixmap('imgs\logo.png')))
        self.mainBar = self.menuBar()
        self.mainBar.addMenu("File")
        self.mainBar.addMenu("Edit")
        self.setMenuBar(self.mainBar)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()