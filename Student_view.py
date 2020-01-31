# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'student_view.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from DataBase import DataBase as db
from encrypt import encrypt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication, QLabel, QDialog
from PyQt5.QtWidgets import QMessageBox as mb

class Ui_student_view(QDialog):
    def __init__(self, par, use):
        super(Ui_student_view, self).__init__()
        self.users = db()
        self.enc = encrypt()
        self.messbox = mb()
        self.username = use
        
    def setupUi(self, student_view):
        student_view.setObjectName("student_view")
        student_view.resize(800, 500)
        student_view.setMinimumSize(QtCore.QSize(800, 500))

        #menu
        self.gridLayoutWidget = QtWidgets.QWidget(student_view)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 160, 162))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.dash_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.dash_button.setObjectName("dash_button")
        self.dash_button.clicked.connect(self.show_dash)
        self.gridLayout.addWidget(self.dash_button, 0, 0, 1, 1)
        self.files_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.files_button.setObjectName("files_button")
        self.files_button.clicked.connect(self.show_file)
        self.gridLayout.addWidget(self.files_button, 1, 0, 1, 1)
        self.grades_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.grades_button.setObjectName("grades_button")
        self.grades_button.clicked.connect(self.show_grade)
        self.gridLayout.addWidget(self.grades_button, 2, 0, 1, 1)
        self.announcement_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.announcement_button.setObjectName("announcement_button")
        self.announcement_button.clicked.connect(self.show_announcement)
        self.gridLayout.addWidget(self.announcement_button, 3, 0, 1, 1)
        self.change_password_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.change_password_button.setObjectName("change_pass_button")
        self.change_password_button.setText("Change Password")
        self.change_password_button.clicked.connect(self.show_change_pass)
        self.gridLayout.addWidget(self.change_password_button, 4, 0, 1, 1)

        #dash Frame
        self.dash_frame = QtWidgets.QFrame(student_view)
        self.dash_frame.setGeometry(QtCore.QRect(160, 0, 481, 111))
        self.dash_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.dash_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.dash_frame.setObjectName("dash_frame")
        self.dash_frame.setVisible(False)
        
        self.label = QtWidgets.QLabel(self.dash_frame)
        self.label.setGeometry(QtCore.QRect(20, 20, 61, 16))
        self.label.setObjectName("label")
        self.dash_scrollArea = QtWidgets.QScrollArea(self.dash_frame)
        self.dash_scrollArea.setGeometry(QtCore.QRect(20, 40, 441, 61))
        self.dash_scrollArea.setWidgetResizable(True)
        self.dash_scrollArea.setObjectName("dash_scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 439, 59))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.dash_scrollArea.setWidget(self.scrollAreaWidgetContents)

        #file Frame
        self.file_frame = QtWidgets.QFrame(student_view)
        self.file_frame.setGeometry(QtCore.QRect(160, 0, 501, 111))
        self.file_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.file_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.file_frame.setObjectName("file_frame")
        self.file_frame.setVisible(False)
        
        self.label_2 = QtWidgets.QLabel(self.file_frame)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 47, 13))
        self.label_2.setObjectName("label_2")
        self.file_scrollArea = QtWidgets.QScrollArea(self.file_frame)
        self.file_scrollArea.setGeometry(QtCore.QRect(20, 40, 441, 61))
        self.file_scrollArea.setWidgetResizable(True)
        self.file_scrollArea.setObjectName("file_scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 439, 59))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.file_scrollArea.setWidget(self.scrollAreaWidgetContents_2)

        #grade_frame
        self.grade_frame = QtWidgets.QFrame(student_view)
        self.grade_frame.setGeometry(QtCore.QRect(160, 0, 481, 151))
        self.grade_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.grade_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.grade_frame.setObjectName("grade_frame")
        self.grade_frame.setVisible(False)
        
        self.label_3 = QtWidgets.QLabel(self.grade_frame)
        self.label_3.setGeometry(QtCore.QRect(20, 20, 47, 13))
        self.label_3.setObjectName("label_3")
        self.grade_scrollArea = QtWidgets.QScrollArea(self.grade_frame)
        self.grade_scrollArea.setGeometry(QtCore.QRect(20, 40, 441, 80))
        self.grade_scrollArea.setWidgetResizable(True)
        self.grade_scrollArea.setObjectName("grade_scrollArea")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 439, 78))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.grade_scrollArea.setWidget(self.scrollAreaWidgetContents_3)

        #announcemen frame
        self.announcement_frame = QtWidgets.QFrame(student_view)
        self.announcement_frame.setGeometry(QtCore.QRect(160, 0, 521, 161))
        self.announcement_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.announcement_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.announcement_frame.setObjectName("announcement_frame")
        self.announcement_frame.setVisible(False)
        
        self.label_4 = QtWidgets.QLabel(self.announcement_frame)
        self.label_4.setGeometry(QtCore.QRect(20, 20, 81, 16))
        self.label_4.setObjectName("label_4")
        self.announcement_scrollArea = QtWidgets.QScrollArea(self.announcement_frame)
        self.announcement_scrollArea.setGeometry(QtCore.QRect(20, 40, 441, 101))
        self.announcement_scrollArea.setWidgetResizable(True)
        self.announcement_scrollArea.setObjectName("announcement_scrollArea")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 439, 99))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.announcement_scrollArea.setWidget(self.scrollAreaWidgetContents_4)

        #change password
        self.change_pass_frame = QtWidgets.QFrame(student_view)
        self.change_pass_frame.setGeometry(QtCore.QRect(160, 0, 521, 161))
        self.change_pass_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.change_pass_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.change_pass_frame.setObjectName("change_pass_frame")
        self.change_pass_frame.setVisible(False)

        self.change_label = QtWidgets.QLabel(self.change_pass_frame)
        self.change_label.setGeometry(QtCore.QRect(20, 20, 101, 16))
        self.change_label.setObjectName("change_label")
        self.change_label.setText("Change password")
        self.label_name = QtWidgets.QLabel(self.change_pass_frame)
        self.label_name.setGeometry(QtCore.QRect(20, 40, 101, 16))
        self.label_name.setObjectName("label_pass")
        self.label_name.setText("New password:")
        self.new_pass_entry = QtWidgets.QLineEdit(self.change_pass_frame)
        self.new_pass_entry.setGeometry(QtCore.QRect(110, 40, 200, 16))
        self.new_pass_entry.setObjectName("new_pass_entry")
        self.enter_new_pass_button = QtWidgets.QPushButton(self.change_pass_frame)
        self.enter_new_pass_button.setObjectName("grades_button")
        self.enter_new_pass_button.setGeometry(QtCore.QRect(110, 60, 80, 20))
        self.enter_new_pass_button.setText("Enter")
        self.enter_new_pass_button.clicked.connect(self.save_pass)

        self.retranslateUi(student_view)
        QtCore.QMetaObject.connectSlotsByName(student_view)

    def retranslateUi(self, student_view):
        _translate = QtCore.QCoreApplication.translate
        student_view.setWindowTitle(_translate("student_view", "Student"))
        self.dash_button.setText(_translate("student_view", "DashBoard"))
        self.files_button.setText(_translate("student_view", "Files"))
        self.grades_button.setText(_translate("student_view", "Grades"))
        self.announcement_button.setText(_translate("student_view", "Announcements"))
        self.label.setText(_translate("student_view", "DashBoard"))
        self.label_2.setText(_translate("student_view", "Files"))
        self.label_3.setText(_translate("student_view", "Grades"))
        self.label_4.setText(_translate("student_view", "Announcements"))

    def show_dash(self):
        self.dash_frame.setVisible(True)
        self.file_frame.setVisible(False)
        self.grade_frame.setVisible(False)
        self.announcement_frame.setVisible(False)
        self.change_pass_frame.setVisible(False)
        self.update_dash()

    def update_dash(self):
        try:
            outline = 'Class\n'
            text = QtWidgets.QLabel(self.dash_frame)
            text.setText(outline+'\n'.join(self.users.get_student_classes(self.username)))
            self.dash_scrollArea.setWidget(text)
        except Exception as err:
            self.messbox.about(self.messbox, "Error",err)
            
    def show_file(self):
        self.dash_frame.setVisible(False)
        self.file_frame.setVisible(True)
        self.grade_frame.setVisible(False)
        self.announcement_frame.setVisible(False)
        self.change_pass_frame.setVisible(False)

    def show_grade(self):
        self.dash_frame.setVisible(False)
        self.file_frame.setVisible(False)
        self.grade_frame.setVisible(True)
        self.announcement_frame.setVisible(False)
        self.change_pass_frame.setVisible(False)

    def show_announcement(self):
        self.dash_frame.setVisible(False)
        self.file_frame.setVisible(False)
        self.grade_frame.setVisible(False)
        self.announcement_frame.setVisible(True)
        self.change_pass_frame.setVisible(False)

    def update_announcement(self):
        try:
            cls = self.users.get_student_classes(self.username)
            text = "time || class || announcement\n"
            for i in cls:
                text += '\n'.join(self.users.view_announcement(self.username, i))
            out = QtWidgets.QLabel(self.announcement_frame)
            out.setText(text)
            self.announcement_scrollArea.setWidget(out)
        except Exception as err:
            self.messbox.about(self.messbox, "Error",err)

    def show_change_pass(self):
        self.dash_frame.setVisible(False)
        self.file_frame.setVisible(False)
        self.grade_frame.setVisible(False)
        self.announcement_frame.setVisible(False)
        self.change_pass_frame.setVisible(True)

    def save_pass(self):
        print("Changing password")
        try:
            new = self.new_pass_entry.text()
            self.new_pass_entry.clear()
            new_enc = self.enc.encrypt_mess(new)
            self.users.update_student_pass(self.username, new_enc)
        except Exception as err:
            print("Error saving password", err)
            self.messbox.about(self.messbox, "Error",err)








    
