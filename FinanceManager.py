# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from assets.user import *
from assets.balance import *
from assets.encryption import *
from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem
import os








class Ui_MainWindow():
    def __init__(self):
        Ui_MainWindow.window_id = 1
        self.balance = 0
        self.value = "0"
        self.description = ""
        self.to_display = ""
        if(os.path.isdir("accounts")):
            if(not(os.path.isfile('accounts/user_accounts.txt'))):
                new_file = open("accounts/user_accounts.txt", 'w')
                new_file.close()
            elif(not(os.path.isfile('accounts/balance.txt'))):
                new_file = open('accounts/balance.txt', 'w')
                new_file.close()
        elif(not(os.path.isdir("accounts"))):
            os.mkdir("accounts")
            new_file = open("accounts/user_accounts.txt", 'w')
            new_file.close()
            new_file = open('accounts/balance.txt', 'w')
            new_file.close()

    def getUi(self):
        if(Ui_MainWindow.window_id == 1 ):
            return self.LoginUi(MainWindow)
        elif(Ui_MainWindow.window_id == 2):
            return self.RegisterUi(MainWindow)
        elif(Ui_MainWindow.window_id == 3):
            return self.DashboardUi(MainWindow)


    # Custom Function:

    def VerifyLogin(self):
        self.username = self.username_input.text()
        self.password = self.password_input.text()
        user_login = Login(self.username, self.password)
        if(user_login.verify()):
            self.getTotal()
            Ui_MainWindow.window_id = 3
            self.DisplayRecords()
        self.getUi()

    def OpenRegistration(self):
        Ui_MainWindow.window_id = 2
        self.getUi()

    def goBack(self):
        Ui_MainWindow.window_id = 1
        self.getUi()

    def getTotal(self):
        print(self.username)
        self.bal = Balance(self.username)
        self.balance = self.bal.getBalance()
        self.balance = str(self.balance)

    def createNewRecord(self):
        self.value = self.new_value_input.text()
        self.description = self.description_input.text()
        new_record = Balance(self.username)
        new_record.addValue(self.value, self.description)
        user_login = Login(self.username, self.password)
        if (user_login.verify()):
            self.getTotal()
            Ui_MainWindow.window_id = 3
        self.getUi()


    def DisplayRecords(self):
        records = Balance(self.username)
        allRecords = records.getRecords()
        self.to_display = ""
        for i in range(len(allRecords)-1, -1, -1):
            if(allRecords[i][1] == self.username):
                self.to_display += "id: " + allRecords[i][0] + "\nvalue: " + allRecords[i][2] + "\nDate: " + allRecords[i][3] + "\nDescription: " + allRecords[i][4]  + "\n--------------------------------------\n"


    def createAccount(self):
        username = self.new_username_input.text()
        password = self.new_password_input.text()

        print(username, password)
        newUser = User()
        newUser.CreateNew(username, password)
        Ui_MainWindow.window_id= 1
        self.getUi()






    #------------------------------------




    # Login Window:
    def LoginUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(480, 370, 214, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.registerButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.registerButton.setObjectName("registerButton")
        self.horizontalLayout.addWidget(self.registerButton)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(spacerItem)
        self.loginButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.loginButton.setObjectName("loginButton")
        self.horizontalLayout.addWidget(self.loginButton)
        self.headTitle = QtWidgets.QLabel(self.centralwidget)
        self.headTitle.setGeometry(QtCore.QRect(210, 120, 371, 71))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.headTitle.setFont(font)
        self.headTitle.setObjectName("headTitle")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(130, 290, 511, 71))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.password_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.password_label.setObjectName("password_label")
        self.verticalLayout_2.addWidget(self.password_label)
        self.password_input = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_input.setObjectName("password_input")
        self.verticalLayout_2.addWidget(self.password_input)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(130, 210, 511, 71))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.username_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.username_label.setObjectName("username_label")
        self.verticalLayout.addWidget(self.username_label)
        self.username_input = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.username_input.setObjectName("username_input")
        self.verticalLayout.addWidget(self.username_input)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)



        # Connectins:
        self.loginButton.clicked.connect(lambda: self.VerifyLogin())
        self.registerButton.clicked.connect(lambda: self.OpenRegistration())

        self.retranslateLoginUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateLoginUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.registerButton.setText(_translate("MainWindow", "Create new account"))
        self.loginButton.setText(_translate("MainWindow", "Login"))
        self.headTitle.setText(_translate("MainWindow", "Finance Manager"))
        self.password_label.setText(_translate("MainWindow", "Password:"))
        self.username_label.setText(_translate("MainWindow", "Username:"))






    # Dashboard Window:
    def DashboardUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(802, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 10, 281, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.usernameLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.usernameLabel.setFont(font)
        self.usernameLabel.setObjectName("usernameLabel")
        self.horizontalLayout.addWidget(self.usernameLabel)
        self.exitButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.exitButton.setObjectName("exitButton")
        self.horizontalLayout.addWidget(self.exitButton)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(20, 150, 551, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.new_value_input = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.new_value_input.setObjectName("new_value_input")
        self.horizontalLayout_2.addWidget(self.new_value_input)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.description_input = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.description_input.setObjectName("description_input")
        self.horizontalLayout_2.addWidget(self.description_input)
        self.submitButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.submitButton.setObjectName("submitButton")
        self.horizontalLayout_2.addWidget(self.submitButton)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 120, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(600, 10, 171, 41))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.balanceLabel = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.balanceLabel.setFont(font)
        self.balanceLabel.setObjectName("balanceLabel")
        self.horizontalLayout_3.addWidget(self.balanceLabel)
        self.balanceValue = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.balanceValue.setObjectName("balanceValue")
        self.horizontalLayout_3.addWidget(self.balanceValue)
        self.recordLabel = QtWidgets.QLabel(self.centralwidget)
        self.recordLabel.setGeometry(QtCore.QRect(20, 260, 221, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.recordLabel.setFont(font)
        self.recordLabel.setObjectName("recordLabel")
        self.recordView = QtWidgets.QTextBrowser(self.centralwidget)
        self.recordView.setGeometry(QtCore.QRect(20, 290, 771, 251))
        self.recordView.setObjectName("recordView")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 802, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)


        # Connections:
        self.submitButton.clicked.connect(lambda: self.createNewRecord())
        self.exitButton.clicked.connect(lambda: self.goBack())


        self.DisplayRecords()
        self.retranslateDashboardUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateDashboardUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.usernameLabel.setText(_translate("MainWindow", self.username))
        self.exitButton.setText(_translate("MainWindow", "Exit Finance Manager"))
        self.label_2.setText(_translate("MainWindow", "Value:"))
        self.label_3.setText(_translate("MainWindow", "Description:"))
        self.submitButton.setText(_translate("MainWindow", "Submit"))
        self.label_4.setText(_translate("MainWindow", "Create new record:"))
        self.balanceLabel.setText(_translate("MainWindow", "Balance:"))
        self.balanceValue.setText(_translate("MainWindow", self.balance))
        self.recordLabel.setText(_translate("MainWindow", "Record History:"))
        self.recordView.setPlainText(_translate("MainWindow",self.to_display))


        #----------------------------------------------------------------------------------------




    # Registration Window:
    def RegisterUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.headTitle = QtWidgets.QLabel(self.centralwidget)
        self.headTitle.setGeometry(QtCore.QRect(210, 70, 371, 71))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.headTitle.setFont(font)
        self.headTitle.setObjectName("headTitle")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(140, 170, 511, 71))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.new_username_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.new_username_label.setObjectName("new_username_label")
        self.verticalLayout.addWidget(self.new_username_label)
        self.new_username_input = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.new_username_input.setText("")
        self.new_username_input.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.new_username_input.setObjectName("new_username_input")
        self.verticalLayout.addWidget(self.new_username_input)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(140, 260, 511, 71))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.new_password_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.new_password_label.setObjectName("new_password_label")
        self.verticalLayout_2.addWidget(self.new_password_label)
        self.new_password_input = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.new_password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.new_password_input.setObjectName("new_password_input")
        self.verticalLayout_2.addWidget(self.new_password_input)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(140, 340, 511, 71))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.new_password_label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.new_password_label_2.setObjectName("new_password_label_2")
        self.verticalLayout_3.addWidget(self.new_password_label_2)
        self.new_password_confirmation = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.new_password_confirmation.setEchoMode(QtWidgets.QLineEdit.Password)
        self.new_password_confirmation.setObjectName("new_password_confirmation")
        self.verticalLayout_3.addWidget(self.new_password_confirmation)
        self.registerButton = QtWidgets.QPushButton(self.centralwidget)
        self.registerButton.setGeometry(QtCore.QRect(520, 430, 131, 41))
        self.registerButton.setObjectName("registerButton")
        self.go_back = QtWidgets.QPushButton(self.centralwidget)
        self.go_back.setGeometry(QtCore.QRect(20, 20, 131, 41))
        self.go_back.setObjectName("go_back")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # Connections:
        self.go_back.clicked.connect(lambda: self.goBack())

        self.retranslateRegisterUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.registerButton.clicked.connect(lambda: self.createAccount())

    def retranslateRegisterUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Finance Manager | Create new account"))
        MainWindow.setProperty("echoMode", _translate("MainWindow", "Password"))
        self.headTitle.setText(_translate("MainWindow", "Finance Manager"))
        self.new_username_label.setText(_translate("MainWindow", "Enter your new username:"))
        self.new_password_label.setText(_translate("MainWindow", "Enter your password:"))
        self.new_password_label_2.setText(_translate("MainWindow", "Confirm your password:"))
        self.registerButton.setText(_translate("MainWindow", "Create account"))
        self.go_back.setText(_translate("MainWindow", "Go back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    setUi = ui.getUi()

    MainWindow.show()
    sys.exit(app.exec_())

