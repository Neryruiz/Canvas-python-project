# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'professor_view.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication, QLabel, QDialog
from PyQt5.QtWidgets import QMessageBox as mb
import random
from DataBase import DataBase as db
from encrypt import encrypt

class Ui_professor_view(QDialog):
    def __init__(self, par, use):
        super(Ui_professor_view, self).__init__()
        self.users = db()
        self.enc = encrypt()
        self.messbox = mb()
        self.username = use
        
    def setupUi(self, Professor_window):
        Professor_window.setObjectName("Professor_window")
        Professor_window.resize(800, 500)
        Professor_window.setMinimumSize(QtCore.QSize(800, 500))

        #menu frame
        self.frame = QtWidgets.QFrame(Professor_window)
        self.frame.setGeometry(QtCore.QRect(0, 0, 171, 511))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayoutWidget = QtWidgets.QWidget(self.frame)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, -1, 171, 170))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.grade_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.grade_button.setObjectName("grade_button")
        self.grade_button.clicked.connect(self.show_grade)
        self.gridLayout.addWidget(self.grade_button, 4, 0, 1, 1)
        self.people_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.people_button.setObjectName("people_button")
        self.people_button.clicked.connect(self.show_people)
        self.gridLayout.addWidget(self.people_button, 2, 0, 1, 1)
        self.assignment_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.assignment_button.setObjectName("assignment_button")
        self.assignment_button.clicked.connect(self.show_assignment)
        self.gridLayout.addWidget(self.assignment_button, 3, 0, 1, 1)
        self.dash_board_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.dash_board_button.setObjectName("dash_board_button")
        self.dash_board_button.clicked.connect(self.show_dash)
        self.gridLayout.addWidget(self.dash_board_button, 0, 0, 1, 1)
        self.file_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.file_button.setObjectName("file_button")
        self.file_button.clicked.connect(self.show_file)
        self.gridLayout.addWidget(self.file_button, 1, 0, 1, 1)
        self.announcements_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.announcements_button.setObjectName("announcements_button")
        self.announcements_button.clicked.connect(self.show_announcement)
        self.gridLayout.addWidget(self.announcements_button, 5, 0, 1, 1)
        self.change_password_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.change_password_button.setObjectName("change_pass_button")
        self.change_password_button.setText("Change Password")
        self.change_password_button.clicked.connect(self.show_change_pass)
        self.gridLayout.addWidget(self.change_password_button, 6, 0, 1, 1)

        #dash Frame
        self.dash_frame = QtWidgets.QFrame(Professor_window)
        self.dash_frame.setGeometry(QtCore.QRect(170, 0, 551, 141))
        self.dash_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.dash_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.dash_frame.setObjectName("dash_frame")
        self.dash_frame.setVisible(False)
        
        self.dash_scrollArea = QtWidgets.QScrollArea(self.dash_frame)
        self.dash_scrollArea.setGeometry(QtCore.QRect(20, 30, 521, 91))
        self.dash_scrollArea.setWidgetResizable(True)
        self.dash_scrollArea.setObjectName("dash_scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 519, 89))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.dash_scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.label = QtWidgets.QLabel(self.dash_frame)
        self.label.setGeometry(QtCore.QRect(20, 10, 61, 16))
        self.label.setObjectName("label")

        #file frame
        self.file_frame = QtWidgets.QFrame(Professor_window)
        self.file_frame.setGeometry(QtCore.QRect(170, 0, 571, 161))
        self.file_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.file_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.file_frame.setObjectName("file_frame")
        self.file_frame.setVisible(False)
        
        self.label_2 = QtWidgets.QLabel(self.file_frame)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 47, 13))
        self.label_2.setObjectName("label_2")
        self.file_scrollArea = QtWidgets.QScrollArea(self.file_frame)
        self.file_scrollArea.setGeometry(QtCore.QRect(20, 40, 521, 71))
        self.file_scrollArea.setWidgetResizable(True)
        self.file_scrollArea.setObjectName("file_scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 519, 69))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.file_scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.label_3 = QtWidgets.QLabel(self.file_frame)
        self.label_3.setGeometry(QtCore.QRect(20, 120, 47, 13))
        self.label_3.setObjectName("label_3")
        self.file_lineEdit = QtWidgets.QLineEdit(self.file_frame)
        self.file_lineEdit.setGeometry(QtCore.QRect(70, 120, 221, 20))
        self.file_lineEdit.setObjectName("file_lineEdit")
        self.post_button = QtWidgets.QPushButton(self.file_frame)
        self.post_button.setGeometry(QtCore.QRect(310, 120, 75, 23))
        self.post_button.setObjectName("post_button")

        #people frame
        self.people_frame = QtWidgets.QFrame(Professor_window)
        self.people_frame.setGeometry(QtCore.QRect(170, 0, 591, 161))
        self.people_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.people_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.people_frame.setObjectName("people_frame")
        self.people_frame.setVisible(False)
        
        self.label_4 = QtWidgets.QLabel(self.people_frame)
        self.label_4.setGeometry(QtCore.QRect(20, 20, 47, 13))
        self.label_4.setObjectName("label_4")
        self.people_scrollArea = QtWidgets.QScrollArea(self.people_frame)
        self.people_scrollArea.setGeometry(QtCore.QRect(20, 40, 521, 101))
        self.people_scrollArea.setWidgetResizable(True)
        self.people_scrollArea.setObjectName("people_scrollArea")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 519, 99))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.people_scrollArea.setWidget(self.scrollAreaWidgetContents_3)

        #assigment frame
        self.assignment_frame = QtWidgets.QFrame(Professor_window)
        self.assignment_frame.setGeometry(QtCore.QRect(170, 0, 551, 271))
        self.assignment_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.assignment_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.assignment_frame.setObjectName("assignment_frame")
        self.assignment_frame.setVisible(False)
        
        self.label_5 = QtWidgets.QLabel(self.assignment_frame)
        self.label_5.setGeometry(QtCore.QRect(20, 20, 61, 16))
        self.label_5.setObjectName("label_5")
        self.assignment_scrollArea = QtWidgets.QScrollArea(self.assignment_frame)
        self.assignment_scrollArea.setGeometry(QtCore.QRect(20, 40, 521, 141))
        self.assignment_scrollArea.setWidgetResizable(True)
        self.assignment_scrollArea.setObjectName("assignment_scrollArea")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 519, 139))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.assignment_scrollArea.setWidget(self.scrollAreaWidgetContents_4)
        self.add_assign_button = QtWidgets.QPushButton(self.assignment_frame)
        self.add_assign_button.setGeometry(QtCore.QRect(360, 200, 101, 23))
        self.add_assign_button.setObjectName("add_assign_button")

        #grade frame
        self.grade_frame = QtWidgets.QFrame(Professor_window)
        self.grade_frame.setGeometry(QtCore.QRect(170, 0, 571, 241))
        self.grade_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.grade_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.grade_frame.setObjectName("grade_frame")
        self.grade_frame.setVisible(False)
        
        self.label_6 = QtWidgets.QLabel(self.grade_frame)
        self.label_6.setGeometry(QtCore.QRect(20, 20, 47, 13))
        self.label_6.setObjectName("label_6")
        self.grade_scrollArea = QtWidgets.QScrollArea(self.grade_frame)
        self.grade_scrollArea.setGeometry(QtCore.QRect(20, 40, 521, 141))
        self.grade_scrollArea.setWidgetResizable(True)
        self.grade_scrollArea.setObjectName("grade_scrollArea")
        self.scrollAreaWidgetContents_5 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_5.setGeometry(QtCore.QRect(0, 0, 519, 139))
        self.scrollAreaWidgetContents_5.setObjectName("scrollAreaWidgetContents_5")
        self.grade_scrollArea.setWidget(self.scrollAreaWidgetContents_5)

        #announcement frame
        self.announcement_frame = QtWidgets.QFrame(Professor_window)
        self.announcement_frame.setGeometry(QtCore.QRect(170, 0, 581, 271))
        self.announcement_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.announcement_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.announcement_frame.setObjectName("announcement_frame")
        self.announcement_frame.setVisible(False)
        
        self.label_7 = QtWidgets.QLabel(self.announcement_frame)
        self.label_7.setGeometry(QtCore.QRect(20, 20, 141, 16))
        self.label_7.setObjectName("label_7")
        self.annountment_scrollArea = QtWidgets.QScrollArea(self.announcement_frame)
        self.annountment_scrollArea.setGeometry(QtCore.QRect(20, 40, 511, 101))
        self.annountment_scrollArea.setWidgetResizable(True)
        self.annountment_scrollArea.setObjectName("annountment_scrollArea")
        self.scrollAreaWidgetContents_6 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_6.setGeometry(QtCore.QRect(0, 0, 509, 99))
        self.scrollAreaWidgetContents_6.setObjectName("scrollAreaWidgetContents_6")
        self.annountment_scrollArea.setWidget(self.scrollAreaWidgetContents_6)
        self.label_8 = QtWidgets.QLabel(self.announcement_frame)
        self.label_8.setGeometry(QtCore.QRect(20, 150, 131, 16))
        self.label_8.setObjectName("label_8")
        self.announcement_lineEdit = QtWidgets.QLineEdit(self.announcement_frame)
        self.announcement_lineEdit.setGeometry(QtCore.QRect(150, 150, 201, 20))
        self.announcement_lineEdit.setObjectName("announcement_lineEdit")
        self.post_announce_button = QtWidgets.QPushButton(self.announcement_frame)
        self.post_announce_button.setGeometry(QtCore.QRect(360, 150, 75, 23))
        self.post_announce_button.clicked.connect(self.post_ann)
        self.post_announce_button.setObjectName("post_announce_button")

        #change password
        self.change_pass_frame = QtWidgets.QFrame(Professor_window)
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

        self.retranslateUi(Professor_window)
        QtCore.QMetaObject.connectSlotsByName(Professor_window)

    def retranslateUi(self, Professor_window):
        _translate = QtCore.QCoreApplication.translate
        Professor_window.setWindowTitle(_translate("Professor_window", "Professor"))
        self.grade_button.setText(_translate("Professor_window", "Grades"))
        self.people_button.setText(_translate("Professor_window", "People"))
        self.assignment_button.setText(_translate("Professor_window", "Assigment"))
        self.dash_board_button.setText(_translate("Professor_window", "Dash Board"))
        self.file_button.setText(_translate("Professor_window", "Files"))
        self.announcements_button.setText(_translate("Professor_window", "Announcements"))
        self.label.setText(_translate("Professor_window", "Dash Board"))
        self.label_2.setText(_translate("Professor_window", "Files"))
        self.label_3.setText(_translate("Professor_window", "Add file:"))
        self.post_button.setText(_translate("Professor_window", "Post"))
        self.label_4.setText(_translate("Professor_window", "People"))
        self.label_5.setText(_translate("Professor_window", "Assignemts"))
        self.add_assign_button.setText(_translate("Professor_window", "Add assignment"))
        self.label_6.setText(_translate("Professor_window", "Grades"))
        self.label_7.setText(_translate("Professor_window", "Announcements"))
        self.label_8.setText(_translate("Professor_window", "post new announcement:"))
        self.post_announce_button.setText(_translate("Professor_window", "Post"))

    def show_dash(self):
        self.dash_frame.setVisible(True)
        self.file_frame.setVisible(False)
        self.people_frame.setVisible(False)
        self.assignment_frame.setVisible(False)
        self.grade_frame.setVisible(False)
        self.announcement_frame.setVisible(False)
        self.change_pass_frame.setVisible(False)
        self.update_dash_scroll()

    def update_dash_scroll(self):
        try:
            outline = 'Classes\n'
            text = QtWidgets.QLabel(self.dash_frame)
            text.setText(outline+'\n'.join(self.users.get_professor_classes(self.username)))
            self.dash_scrollArea.setWidget(text)
        except Exception as err:
            self.messbox.about(self.messbox, "Error",str(err))

    def show_file(self):
        self.dash_frame.setVisible(False)
        self.file_frame.setVisible(True)
        self.people_frame.setVisible(False)
        self.assignment_frame.setVisible(False)
        self.grade_frame.setVisible(False)
        self.announcement_frame.setVisible(False)
        self.change_pass_frame.setVisible(False)

    def show_people(self):
        self.dash_frame.setVisible(False)
        self.file_frame.setVisible(False)
        self.people_frame.setVisible(True)
        self.assignment_frame.setVisible(False)
        self.grade_frame.setVisible(False)
        self.announcement_frame.setVisible(False)
        self.change_pass_frame.setVisible(False)
        self.update_people_scroll()

    def update_people_scroll(self):
        try:
            cls = self.users.get_professor_classes(self.username)
            people = []
            for i in cls:
                lst = self.users.get_class_list(i)
                for e in lst:
                    people.append(" --- ".join(e))
                people.append('\n')
            #print(people)
            text='Class --- student\n'
            for i in people:
                text+=str(i)+'\n'
            out = QtWidgets.QLabel(self.people_frame)
            out.setText(text)
            self.people_scrollArea.setWidget(out)
        except Exception as err:
            self.messbox.about(self.messbox, "Error",str(err))

    def show_assignment(self):
        self.dash_frame.setVisible(False)
        self.file_frame.setVisible(False)
        self.people_frame.setVisible(False)
        self.assignment_frame.setVisible(True)
        self.grade_frame.setVisible(False)
        self.announcement_frame.setVisible(False)
        self.change_pass_frame.setVisible(False)
        

    def update_announcement(self):
        try:
            text = self.users.view_announcement(self.username)
            out =  QtWidgets.QLabel(self.announcement_frame)
            out.setText(str(text))
            self.annountment_scrollArea.setWidget(out)
        except Exception as err:
            self.messbox.about(self.messbox, "Error",str(err))

    def show_grade(self):
        self.dash_frame.setVisible(False)
        self.file_frame.setVisible(False)
        self.people_frame.setVisible(False)
        self.assignment_frame.setVisible(False)
        self.grade_frame.setVisible(True)
        self.announcement_frame.setVisible(False)
        self.change_pass_frame.setVisible(False)

    def show_announcement(self):
        self.dash_frame.setVisible(False)
        self.file_frame.setVisible(False)
        self.people_frame.setVisible(False)
        self.assignment_frame.setVisible(False)
        self.grade_frame.setVisible(False)
        self.announcement_frame.setVisible(True)
        self.change_pass_frame.setVisible(False)
        self.update_announcement()
        #self.users.add_announcement(self.username, '', '')

    def show_change_pass(self):
        self.dash_frame.setVisible(False)
        self.file_frame.setVisible(False)
        self.people_frame.setVisible(False)
        self.assignment_frame.setVisible(False)
        self.grade_frame.setVisible(False)
        self.announcement_frame.setVisible(False)
        self.change_pass_frame.setVisible(True)

    def save_pass(self):
        print("Changing password")
        try:
            new = self.new_pass_entry.text()
            self.new_pass_entry.clear()
            new_enc = self.enc.encrypt_mess(new)
            self.users.update_professor_pass(self.username, new_enc)
        except Exception as err:
            print("Error saving password", err)
            self.messbox.about(self.messbox, "Error",str(err))

    def post_ann(self):
        mess = self.announcement_lineEdit.text().split(',',1)
        who = mess[0]
        message = mess[1]
        self.users.add_announcement(self.username, who, message)
        self.announcement_lineEdit.clear()
        self.update_announcement()


















