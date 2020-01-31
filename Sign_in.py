#by Nery Ruiz
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Sign_in_window.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
from DataBase import DataBase as db
from encrypt import encrypt
from PyQt5.QtWidgets import QMessageBox as mb
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDialog
from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel
from Admin_Dialog import Ui_admin_window
from Professor_view import Ui_professor_view
from Student_view import Ui_student_view

class Ui_Dialog(object):
    def __init__(self):
        self.users = db()
        self.enc = encrypt()
        self.messbox = mb()
        self.username_pass = ''
        #self.open_ad()
            
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(130, 50, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.user_name_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.user_name_lineEdit.setGeometry(QtCore.QRect(90, 130, 211, 20))
        self.user_name_lineEdit.setObjectName("user_name_lineEdit")
        self.password_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.password_lineEdit.setGeometry(QtCore.QRect(90, 180, 211, 20))
        self.password_lineEdit.setObjectName("password_lineEdit")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(100, 110, 61, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(100, 160, 47, 13))
        self.label_3.setObjectName("label_3")
        self.enter_button = QtWidgets.QPushButton(Dialog)
        self.enter_button.setGeometry(QtCore.QRect(240, 220, 75, 23))
        self.enter_button.setObjectName("enter_button")
        self.enter_button.clicked.connect(self.sign_in)
        self.error_label = QtWidgets.QLabel(Dialog)
        self.error_label.setGeometry(QtCore.QRect(90, 220, 47, 13))
        self.error_label.setText("")
        self.error_label.setObjectName("error_label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        #self.sign_in()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Sign In"))
        self.label.setText(_translate("Dialog", "Welcome"))
        self.label_2.setText(_translate("Dialog", "User Name"))
        self.label_3.setText(_translate("Dialog", "Password"))
        self.enter_button.setText(_translate("Dialog", "Enter"))

    def sign_in(self):
        print('signing in')
        username = self.user_name_lineEdit.text()
        password = self.password_lineEdit.text()
        self.username_pass = username
        self.user_name_lineEdit.clear()
        self.password_lineEdit.clear()
        students = self.users.get_students()
        professors = self.users.get_professors()
        self.test = self.enc.decrypt_mess(self.users.get_ad_pass())
        if(username == "ADMIN" and password == self.test):
            print("ADMIN window")
            try:
                self.open_ad()
                #self.close()
                #sys.exit(app.exec_())
            except Exception as err:
                print("sign in:", err)
                
        elif(self.users.is_in_student(username)):
            print('student')
            i = self.users.find_student(username)
            if(i != None):
                p = self.enc.decrypt_mess(students[i][1])
                if(p == password):
                    print('pass')
                    try:
                        self.open_student()
                    except Exception as err:
                        print("open student",err)
                else:
                    self.messbox.about(self.messbox, "Error", "The username or password you entered were incorrect.")
            else:
                self.messbox.about(self.messbox, "Error", "The username or password you entered were incorrect.")
        elif(self.users.is_in_professor(username)):
            print('professor')
            i = self.users.find_professor(username)
            if(i != None):
                p = self.enc.decrypt_mess(professors[i][1])
                if(p == password):
                    print('pass')
                    try:
                        self.open_professor()
                    except Exception as err:
                        print("open professor",err)
                else:
                    self.messbox.about(self.messbox, "Error", "The username or password you entered were incorrect.")
            else:
                self.messbox.about(self.messbox, "Error", "The username or password you entered were incorrect.")
        else:
            print("error")
            self.messbox.about(self.messbox, "Error", "The username or password you entered were incorrect.")

    def open_ad(self):
        print("open Admin")
        #app = QApplication(sys.argv)
        nex = QDialog()
        ui = Ui_admin_window(self)
        ui.setupUi(nex, )
        nex.show()
        nex.exec_()
        #ui.hide()
        #self.close()
        #app.exec_()

    def open_student(self):
        nex = QDialog()
        ui = Ui_student_view(self, self.username_pass)
        ui.setupUi(nex)
        nex.show()
        nex.exec_()

    def open_professor(self):
        nex = QDialog()
        ui = Ui_professor_view(self, self.username_pass)
        ui.setupUi(nex)
        nex.show()
        nex.exec_()

    
