import GUI.Email_Scrapper_GUI
import GUI.Main_Window
from Config import *

app = GUI.Email_Scrapper_GUI.QApplication(sys.argv)
Main = GUI.Main_Window.MainWindow() 
S = GUI.Email_Scrapper_GUI.SingleEmail(Main)
# M = GUI.Email_Scrapper_GUI.MultibleEmails(Main)
Main.central_widget.addWidget(S)
Main.central_widget.setCurrentWidget(S)
# Main.central_widget.deleteLater()
Main.show()
app.exec_()


print('heasaf')