#//Imports//
try:
    from GUI.Config import *
except BaseException:
    #??modify the sys path?? but not important now.
    from Config import *
try:
    from GUI.Main_Window import MainWindow
except BaseException:
    from Main_Window import MainWindow
    
try:
    from Modules import Email_Scrapping
except BaseException:
    from Modules.Email_Scrapping import GetEmail


#//Code//
class SingleEmail(QWidget):
    def __init__(self, parent=None):
        super(SingleEmail, self).__init__(parent)
        self.parent = parent
        #---initilizing the user Interface---
        self.initUi()

    #---The user Interfac code---
    def initUi(self):
        #--Header Photo--
        self.L_header = QLabel()
        self.L_header.setPixmap(QPixmap('imgs\Email-Scrap-up.png'))
        #-Align Top-
        self.L_header.setAlignment(Qt.AlignTop)
        #--compo container--
        self.comboLayout = QVBoxLayout()
        self.comboMainLabel = QLabel()
        self.TheCombo = QComboBox()
        #-combo prop-
        self.comboMainLabel.setText("Please Chose How many URLs/Websites do you have:- (*)")
        self.TheCombo.addItem("One Single URL/Webiste")
        self.TheCombo.addItem("Multible URLs/Webistes")
        # self.TheCombo.setCurrentIndex(0)
        #--ad to layout--
        self.comboLayout.addWidget(self.comboMainLabel)
        self.comboLayout.addWidget(self.TheCombo)
        #-Align Top-
        self.comboLayout.setAlignment(Qt.AlignTop)
        #--Form--
        #-Input-
        self.inputForm = QFormLayout()
        self.urlLabel = QLabel()
        self.url = QLineEdit()
        self.urlLabel.setText("Please Paste the URL HERE:- ")
        #-output-
        self.outputForm = QFormLayout()
        self.outputLabel = QLabel()
        self.emails = QTextEdit()
        self.outputLabel.setText("The output: -")
        #-Set The layout-
        self.inputForm.addRow(self.urlLabel, self.url)
        self.outputForm.addRow(self.outputLabel, self.emails)
        #--Submit Button--
        self.submit = QPushButton()
        self.submit.setText("Get Email")
        self.submit.setFixedWidth(300)
        
        #----Grid----
        self.gridLayout = QGridLayout()
        # self.gridLayout.set
        self.gridLayout.addWidget(self.L_header, 1, 6, 1, 11)
        self.gridLayout.addLayout(self.comboLayout, 4, 6, 1, 11)
        self.gridLayout.addLayout(self.inputForm, 5, 6, 1, 11)
        self.gridLayout.addLayout(self.outputForm, 6, 6, 1, 11)
        self.gridLayout.addWidget(self.submit, 7, 6, 11, 11, Qt.AlignCenter)
        self.setLayout(self.gridLayout)
    
        #----Codes----
        #---Widgets Change---
        self.TheCombo.currentIndexChanged.connect(self.cb)
        #---Button---
        self.submit.clicked.connect(self.getemail)


    #--Combo Method--
    def cb(self, i):
        if i == 1 or i == '1':
            #--Making a new instance of all--
            self.M = MultibleEmails(self.parent)
            self.parent.central_widget = QStackedWidget(self.parent)
            #--set the central widget--
            self.parent.setCentralWidget(self.parent.central_widget)
            #--set the widgts--
            self.parent.central_widget.addWidget(self.M)
            self.parent.central_widget.setCurrentWidget(self.M)
            #-set the combo-
            self.TheCombo.setCurrentIndex(i)

    #--Get Email Mehod--
    def getemail(self):
        url = self.url.text()
        emails  = Email_Scrapping.GetEmail().get(url)
        self.emails.setText(str(emails))



#----- Multible Emails Gui---------------------------------------------------
class MultibleEmails(QWidget):
    def __init__(self, parent=None):
        super(MultibleEmails, self).__init__(parent)
        self.parent = parent
        self.xlsxPath = ''
        #---initilizing the user Interface---
        self.initUi()

    #---The user Interfac code---
    def initUi(self):
        #--Header Photo--
        self.L_header = QLabel()
        self.L_header.setPixmap(QPixmap('imgs\Email-Scrap-up.jpg'))
        #-Align Top-
        self.L_header.setAlignment(Qt.AlignTop)
        #--compo container--
        self.comboLayout = QVBoxLayout()
        self.comboMainLabel = QLabel()
        self.TheCombo = QComboBox()
        #-combo prop-
        self.comboMainLabel.setText("Please Chose How many URLs/Websites do you have:- (*)")
        self.TheCombo.addItem("One Single URL/Webiste")
        self.TheCombo.addItem("Multible URLs/Webistes")
        self.TheCombo.setCurrentIndex(1)
        #--ad to layout--
        self.comboLayout.addWidget(self.comboMainLabel)
        self.comboLayout.addWidget(self.TheCombo)
        #-Align Top-
        self.comboLayout.setAlignment(Qt.AlignTop)
        #--Form--
        #-Input-
        self.inputForm = QFormLayout()
        self.urlLabel = QLabel()
        self.urls = QPushButton()
        self.urls.setText("Choose an excel file")
        self.urls.clicked.connect(self.getfile)
        self.urlLabel.setText("Please Paste the URL HERE:- ")
        #-output-
        self.outputForm = QFormLayout()
        self.outputLabel = QLabel()
        self.emails = QTextEdit()
        self.outputLabel.setText("The output: -")
        #-Set The layout-
        self.inputForm.addRow(self.urlLabel, self.urls)
        self.outputForm.addRow(self.outputLabel, self.emails)
        #--Submit Button--
        self.submit = QPushButton()
        self.submit.setText("Get Email")
        self.submit.setFixedWidth(300)
        #--counter--
        self.count = QLabel("0")
        self.count.setAlignment(Qt.AlignCenter)
        
        #---Widgets Change---
        self.TheCombo.currentIndexChanged.connect(self.cb)
        #---Button---
        self.submit.clicked.connect(self.getemail)


        #----Grid----
        self.gridLayout = QGridLayout()
        # self.gridLayout.set
        self.gridLayout.addWidget(self.L_header, 1, 6, 1, 11)
        self.gridLayout.addLayout(self.comboLayout, 4, 6, 1, 11)
        self.gridLayout.addLayout(self.inputForm, 5, 6, 1, 11)
        self.gridLayout.addLayout(self.outputForm, 6, 6, 1, 11)
        self.gridLayout.addWidget(self.count, 7, 6, 1, 11, Qt.AlignCenter)
        self.gridLayout.addWidget(self.submit, 8, 6, 1, 11, Qt.AlignCenter)
        self.setLayout(self.gridLayout)

    
    #--Combo Method--
    def cb(self, i):
        if i == 0 or i == '0':
            #--Making a new instance of all--
            self.S = SingleEmail(self.parent) #--1
            self.parent.central_widget = QStackedWidget(self.parent) #--2
            #--set the central widget--
            self.parent.setCentralWidget(self.parent.central_widget) 
            #--set the widgts--
            self.parent.central_widget.addWidget(self.S)
            self.parent.central_widget.setCurrentWidget(self.S)
            #-set the combo-
            self.TheCombo.setCurrentIndex(i)
    
    #--File Dialog method--
    def getfile(self):
        self.xlsx = QFileDialog.getOpenFileName(self, 'Open file',
        'd:\\',"(*.xlsx *.txt)")
        self.xlsxPath = self.xlsx[0]
        self.urls.setEnabled(False)

    def getemail(self):
        #--approach 01--
        # test = [r'https://doc.qt.io/qt-6/qstackedwidget.html#dtor.QStackedWidget', r'https://stackoverflow.com/questions/24868733/how-to-access-a-module-from-outside-your-file-folder-in-python', r'https://www.grc.nasa.gov/www/k-12/airplane/airplane.html']
        # emails  = Email_Scrapping.GetEmail().gets(test)
        # self.emails.setText("Loading...")
        # self.emails.setText(str(emails))
        
        #--approach 02--
        self.emails.setText("Loading.....")
        # test = [r'https://doc.qt.io/qt-6/qstackedwidget.html#dtor.QStackedWidget', r'https://stackoverflow.com/questions/24868733/how-to-access-a-module-from-outside-your-file-folder-in-python', r'https://www.grc.nasa.gov/www/k-12/airplane/airplane.html', r'https://doc.qt.io/qt-6/qstackedwidget.html#dtor.QStackedWidget', r'https://stackoverflow.com/questions/24868733/how-to-access-a-module-from-outside-your-file-folder-in-python', r'https://www.grc.nasa.gov/www/k-12/airplane/airplane.html', r'https://doc.qt.io/qt-6/qstackedwidget.html#dtor.QStackedWidget', r'https://stackoverflow.com/questions/24868733/how-to-access-a-module-from-outside-your-file-folder-in-python', r'https://www.grc.nasa.gov/www/k-12/airplane/airplane.html', r'https://doc.qt.io/qt-6/qstackedwidget.html#dtor.QStackedWidget', r'https://stackoverflow.com/questions/24868733/how-to-access-a-module-from-outside-your-file-folder-in-python', r'https://www.grc.nasa.gov/www/k-12/airplane/airplane.html', r'https://doc.qt.io/qt-6/qstackedwidget.html#dtor.QStackedWidget', r'https://stackoverflow.com/questions/24868733/how-to-access-a-module-from-outside-your-file-folder-in-python', r'https://www.grc.nasa.gov/www/k-12/airplane/airplane.html']
        data = Email_Scrapping.GetEmail().readData(self.xlsxPath)
        #--exception--
        if data == "":
            self.emails.setText("Wrong File, Please choose an .xlsx file")
            return
        #--Data Handling--
        self.emailsListofLists = []
        for id, url in enumerate(data.values):
            self.count.setText(str(id))
            emailss = Email_Scrapping.GetEmail().get(url[0])
            emails = emailss[0] 
            self.emailsListofLists.append(emailss[1])
        #--write in a file--list of lists--
        Wrote = Email_Scrapping.GetEmail().writeData(self.emailsListofLists, self.xlsxPath)
        
        if Wrote == "":
            self.emails.setText("Error happened while creating a new excel file")
        elif Wrote == None:
            self.emails.setText("Error happened while Writing or saving the file")
        else:
            temp = str()
            Id = int()
            for id, char in enumerate(self.xlsxPath):
                if char == "\\":
                    Id = id
            self.xlsxPath = self.xlsxPath[:Id]
            self.emails.setText(f"Done\n {self.xlsxPath}")


            

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     # Main = MainWindow() 
#     # S = SingleEmail(Main)
#     # M = MultibleEmails(Main)
#     Main.central_widget.addWidget(S)
#     Main.central_widget.setCurrentWidget(S)
#     # Main.central_widget.addWidget(M)
#     # Main.central_widget.setCurrentWidget(M)
#     Main.show()
#     app.exec_()


