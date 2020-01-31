#By Nery Ruiz
#-*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Admin_window.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication, QLabel, QDialog
from PyQt5.QtWidgets import QMessageBox as mb
import random
from DataBase import DataBase as db
from encrypt import encrypt

class Ui_admin_window(QDialog):
    def __init__(self, par):
        super(Ui_admin_window, self).__init__()
        self.name = ''
        self.email = ''
        self.username = ''
        self.default_pass = ''
        self.db = db()
        self.enc = encrypt()
        self.messbox = mb()
        
    def setupUi(self, admin_window):
        admin_window.setObjectName("admin_window")
        admin_window.resize(996, 815)
        admin_window.setMinimumSize(QtCore.QSize(800, 500))

        #menu frame
        self.ad_button_frame = QtWidgets.QFrame(admin_window)
        self.ad_button_frame.setGeometry(QtCore.QRect(0, 0, 171, 501))
        self.ad_button_frame.setAutoFillBackground(True)
        self.ad_button_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ad_button_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ad_button_frame.setObjectName("ad_button_frame")
        
        self.add_student_button = QtWidgets.QPushButton(self.ad_button_frame)
        self.add_student_button.setGeometry(QtCore.QRect(10, 10, 151, 23))
        self.add_student_button.setObjectName("add_student_button")
        self.add_student_button.clicked.connect(self.show_create_student)
        
        self.delete_student_button = QtWidgets.QPushButton(self.ad_button_frame)
        self.delete_student_button.setGeometry(QtCore.QRect(10, 40, 151, 23))
        self.delete_student_button.setObjectName("delete_student_button")
        self.delete_student_button.clicked.connect(self.show_delete_student)
        
        self.add_professor_button = QtWidgets.QPushButton(self.ad_button_frame)
        self.add_professor_button.setGeometry(QtCore.QRect(10, 70, 151, 23))
        self.add_professor_button.setObjectName("add_professor_button")
        self.add_professor_button.clicked.connect(self.show_add_professor)
        
        self.create_class = QtWidgets.QPushButton(self.ad_button_frame)
        self.create_class.setGeometry(QtCore.QRect(10, 130, 151, 23))
        self.create_class.setObjectName("create_class")
        self.create_class.clicked.connect(self.show_create_class)
        
        self.delete_class = QtWidgets.QPushButton(self.ad_button_frame)
        self.delete_class.setGeometry(QtCore.QRect(10, 160, 151, 23))
        self.delete_class.setObjectName("delete_class")
        self.delete_class.clicked.connect(self.show_delete_class)
        
        self.add_student_class_button = QtWidgets.QPushButton(self.ad_button_frame)
        self.add_student_class_button.setGeometry(QtCore.QRect(10, 190, 151, 23))
        self.add_student_class_button.setObjectName("add_student_class_button")
        self.add_student_class_button.clicked.connect(self.show_add_student_class)
        
        self.remove_student_frame_button = QtWidgets.QPushButton(self.ad_button_frame)
        self.remove_student_frame_button.setGeometry(QtCore.QRect(10, 220, 151, 23))
        self.remove_student_frame_button.setObjectName("pushButton")
        self.remove_student_frame_button.clicked.connect(self.show_remove_student)
        
        self.delete_professor_button = QtWidgets.QPushButton(self.ad_button_frame)
        self.delete_professor_button.setGeometry(QtCore.QRect(10, 100, 151, 23))
        self.delete_professor_button.setObjectName("delete_professor_button")
        self.delete_professor_button.clicked.connect(self.show_delete_professor)

        #create student account frame
        self.ad_add_frame = QtWidgets.QFrame(admin_window)
        self.ad_add_frame.setGeometry(QtCore.QRect(170, 0, 411, 171))
        self.ad_add_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ad_add_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ad_add_frame.setObjectName("ad_add_frame")
        self.ad_add_frame.setVisible(False)
        
        self.gridLayoutWidget = QtWidgets.QWidget(self.ad_add_frame)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 40, 391, 125))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.Genarated_username = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Genarated_username.setText("")#gerated username
        self.Genarated_username.setObjectName("Genarated_username")
        self.gridLayout.addWidget(self.Genarated_username, 4, 1, 1, 1, QtCore.Qt.AlignVCenter)
        
        self.add_student_db_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.add_student_db_button.setObjectName("add_student_db_button")
        self.add_student_db_button.clicked.connect(self.add_student_db)#add student db
        self.gridLayout.addWidget(self.add_student_db_button, 6, 2, 1, 1)
        
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)
        
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        
        self.Genarated_password = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Genarated_password.setText("")#genrated pass
        self.Genarated_password.setObjectName("Genarated_password")
        self.gridLayout.addWidget(self.Genarated_password, 5, 1, 1, 1, QtCore.Qt.AlignVCenter)
        
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1, QtCore.Qt.AlignVCenter)
        
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)
        
        self.add_student_cancel_db_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.add_student_cancel_db_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.add_student_cancel_db_button.setObjectName("add_student_cancel_db_button")
        self.gridLayout.addWidget(self.add_student_cancel_db_button, 6, 3, 1, 1)
        self.add_student_cancel_db_button.clicked.connect(self.close_add_student)#close frame
        
        self.Email_lineEdit_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.Email_lineEdit_2.setObjectName("Email_lineEdit_2")
        self.gridLayout.addWidget(self.Email_lineEdit_2, 2, 1, 1, 3)
        
        self.Name_lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.Name_lineEdit.setObjectName("Name_lineEdit")
        self.gridLayout.addWidget(self.Name_lineEdit, 0, 1, 1, 3)
        
        self.Genarate_user_pass_button = QtWidgets.QPushButton(self.gridLayoutWidget)#genarate username and default password
        self.Genarate_user_pass_button.setObjectName("Genarate_user_pass_button")
        self.Genarate_user_pass_button.clicked.connect(self.gen_user_pass)
        self.gridLayout.addWidget(self.Genarate_user_pass_button, 4, 2, 1, 2)
        
        self.label_6 = QtWidgets.QLabel(self.ad_add_frame)
        self.label_6.setGeometry(QtCore.QRect(10, 20, 121, 16))
        self.label_6.setObjectName("label_6")

        #delete student account frame
        self.ad_delete_frame = QtWidgets.QFrame(admin_window)
        self.ad_delete_frame.setGeometry(QtCore.QRect(170, 0, 621, 211))
        self.ad_delete_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ad_delete_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ad_delete_frame.setObjectName("ad_delete_frame")
        self.ad_delete_frame.setVisible(False)
        
        self.detele_student_scrollArea = QtWidgets.QScrollArea(self.ad_delete_frame)
        self.detele_student_scrollArea.setGeometry(QtCore.QRect(10, 40, 601, 121))
        self.detele_student_scrollArea.setWidgetResizable(True)
        self.detele_student_scrollArea.setObjectName("detele_student_scrollArea")
        
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 599, 119))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.detele_student_scrollArea.setWidget(self.scrollAreaWidgetContents)
        
        self.label_4 = QtWidgets.QLabel(self.ad_delete_frame)
        self.label_4.setGeometry(QtCore.QRect(10, 180, 101, 16))
        self.label_4.setObjectName("label_4")
        self.delete_student_entry = QtWidgets.QLineEdit(self.ad_delete_frame)
        
        self.delete_student_entry.setGeometry(QtCore.QRect(120, 180, 181, 20))
        self.delete_student_entry.setObjectName("delete_student_entry")
        
        self.delete_student_db_button = QtWidgets.QPushButton(self.ad_delete_frame)
        self.delete_student_db_button.clicked.connect(self.delete_student_db)
        self.delete_student_db_button.setGeometry(QtCore.QRect(380, 180, 75, 23))
        
        self.delete_student_db_button.setObjectName("delete_student_db_button")
        self.delete_student_cancel_db_button = QtWidgets.QPushButton(self.ad_delete_frame)
        self.delete_student_cancel_db_button.setGeometry(QtCore.QRect(460, 180, 75, 23))
        self.delete_student_cancel_db_button.clicked.connect(self.close_del_student_db)
        
        self.delete_student_cancel_db_button.setObjectName("delete_student_cancel_db_button")
        self.label_7 = QtWidgets.QLabel(self.ad_delete_frame)
        self.label_7.setGeometry(QtCore.QRect(10, 20, 121, 16))
        self.label_7.setObjectName("label_7")

        #create professor frame
        self.add_professor_frame = QtWidgets.QFrame(admin_window)
        self.add_professor_frame.setGeometry(QtCore.QRect(170, 0, 421, 171))
        self.add_professor_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.add_professor_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.add_professor_frame.setObjectName("add_professor_frame")
        self.add_professor_frame.setVisible(False)
        
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.add_professor_frame)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 40, 401, 125))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        
        self.professor_password_label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.professor_password_label.setText("")
        self.professor_password_label.setObjectName("professor_password_label")
        self.gridLayout_2.addWidget(self.professor_password_label, 3, 1, 1, 1)
        
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 1, 0, 1, 1)
        
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 3, 0, 1, 1)
        
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 2, 0, 1, 1)
        
        self.professor_username_label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.professor_username_label.setText("")
        self.professor_username_label.setObjectName("professor_username_label")
        self.gridLayout_2.addWidget(self.professor_username_label, 2, 1, 1, 1)
        
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 0, 0, 1, 1)
        
        self.add_professor_db_button = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.add_professor_db_button.setObjectName("add_professor_db_button")
        self.add_professor_db_button.clicked.connect(self.add_professor_db)
        self.gridLayout_2.addWidget(self.add_professor_db_button, 4, 2, 1, 1)
        
        self.add_professor_db_cancel_button = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.add_professor_db_cancel_button.setObjectName("add_professor_db_cancel_button")
        self.add_professor_db_cancel_button.clicked.connect(self.close_add_professor)
        self.gridLayout_2.addWidget(self.add_professor_db_cancel_button, 4, 3, 1, 1)
        
        self.lineEdit_3 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_2.addWidget(self.lineEdit_3, 1, 1, 1, 3)
        
        self.lineEdit_2 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_2.addWidget(self.lineEdit_2, 0, 1, 1, 3)
        
        self.Gen_professor_user_pass_button = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.Gen_professor_user_pass_button.setObjectName("Gen_professor_user_pass_button")
        self.Gen_professor_user_pass_button.clicked.connect(self.gen_user_pass_pro)
        self.gridLayout_2.addWidget(self.Gen_professor_user_pass_button, 2, 2, 1, 2)
        
        self.label_12 = QtWidgets.QLabel(self.add_professor_frame)
        self.label_12.setGeometry(QtCore.QRect(10, 20, 131, 16))
        self.label_12.setObjectName("label_12")

        #create class frame
        self.create_class_frame = QtWidgets.QFrame(admin_window)
        self.create_class_frame.setGeometry(QtCore.QRect(170, 0, 661, 151))
        self.create_class_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.create_class_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.create_class_frame.setObjectName("create_class_frame")
        self.create_class_frame.setVisible(False)
        
        self.label_15 = QtWidgets.QLabel(self.create_class_frame)
        self.label_15.setGeometry(QtCore.QRect(10, 20, 81, 16))
        self.label_15.setObjectName("label_15")
        
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.create_class_frame)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(10, 40, 302, 103))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        
        self.label_16 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_16.setObjectName("label_16")
        self.gridLayout_3.addWidget(self.label_16, 0, 0, 1, 1)
        
        self.label_18 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_18.setObjectName("label_18")
        self.gridLayout_3.addWidget(self.label_18, 2, 0, 1, 1)
        
        self.label_17 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_17.setObjectName("label_17")
        self.gridLayout_3.addWidget(self.label_17, 1, 0, 1, 1)
        
        self.add_class_db_buttom = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.add_class_db_buttom.setObjectName("add_class_db_buttom")
        self.add_class_db_buttom.clicked.connect(self.create_course)
        self.gridLayout_3.addWidget(self.add_class_db_buttom, 3, 2, 1, 1)
        
        self.add_class_db_cancel_button = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.add_class_db_cancel_button.setObjectName("add_class_db_cancel_button")
        self.add_class_db_cancel_button.clicked.connect(self.close_create_course)
        self.gridLayout_3.addWidget(self.add_class_db_cancel_button, 3, 3, 1, 1)
        
        self.clas_professor_entry = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.clas_professor_entry.setObjectName("clas_professor_entry")
        self.gridLayout_3.addWidget(self.clas_professor_entry, 2, 1, 1, 3)
        
        self.class_number_entry = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.class_number_entry.setObjectName("class_number_entry")
        self.gridLayout_3.addWidget(self.class_number_entry, 1, 1, 1, 3)
        
        self.class_name_entry = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.class_name_entry.setObjectName("class_name_entry")
        self.gridLayout_3.addWidget(self.class_name_entry, 0, 1, 1, 3)

        #delete class frame
        self.delete_class_frame = QtWidgets.QFrame(admin_window)
        self.delete_class_frame.setGeometry(QtCore.QRect(170, 0, 681, 211))
        self.delete_class_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.delete_class_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.delete_class_frame.setObjectName("delete_class_frame")
        self.delete_class_frame.setVisible(False)
        
        self.delete_class_scrollArea = QtWidgets.QScrollArea(self.delete_class_frame)
        self.delete_class_scrollArea.setGeometry(QtCore.QRect(10, 40, 621, 121))
        self.delete_class_scrollArea.setWidgetResizable(True)
        self.delete_class_scrollArea.setObjectName("delete_class_scrollArea")
        
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 619, 119))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.delete_class_scrollArea.setWidget(self.scrollAreaWidgetContents_3)
        
        self.label_19 = QtWidgets.QLabel(self.delete_class_frame)
        self.label_19.setGeometry(QtCore.QRect(10, 20, 81, 16))
        self.label_19.setObjectName("label_19")
        
        self.label_20 = QtWidgets.QLabel(self.delete_class_frame)
        self.label_20.setGeometry(QtCore.QRect(10, 170, 101, 16))
        self.label_20.setObjectName("label_20")
        
        self.delete_class_entry = QtWidgets.QLineEdit(self.delete_class_frame)
        self.delete_class_entry.setGeometry(QtCore.QRect(120, 170, 171, 20))
        self.delete_class_entry.setObjectName("delete_class_entry")
        
        self.delete_class_db_button = QtWidgets.QPushButton(self.delete_class_frame)
        self.delete_class_db_button.setGeometry(QtCore.QRect(380, 170, 75, 23))
        self.delete_class_db_button.clicked.connect(self.delete_class_act)
        self.delete_class_db_button.setObjectName("delete_class_db_button")
        
        self.delete_class_db_cancel_button = QtWidgets.QPushButton(self.delete_class_frame)
        self.delete_class_db_cancel_button.setGeometry(QtCore.QRect(460, 170, 75, 23))
        self.delete_class_db_cancel_button.clicked.connect(self.close_delete_class)
        self.delete_class_db_cancel_button.setObjectName("delete_class_db_cancel_button")

        #delete professor account frame
        self.delete_professor_frame = QtWidgets.QFrame(admin_window)
        self.delete_professor_frame.setGeometry(QtCore.QRect(170, 0, 641, 211))
        self.delete_professor_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.delete_professor_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.delete_professor_frame.setObjectName("delete_professor_frame")
        self.delete_professor_frame.setVisible(False)
        
        self.label_13 = QtWidgets.QLabel(self.delete_professor_frame)
        self.label_13.setGeometry(QtCore.QRect(10, 20, 121, 16))
        self.label_13.setObjectName("label_13")
        
        self.delete_professor_scrollArea = QtWidgets.QScrollArea(self.delete_professor_frame)
        self.delete_professor_scrollArea.setGeometry(QtCore.QRect(10, 50, 601, 111))
        self.delete_professor_scrollArea.setWidgetResizable(True)
        self.delete_professor_scrollArea.setObjectName("delete_professor_scrollArea")
        
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 599, 109))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.delete_professor_scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        
        self.label_14 = QtWidgets.QLabel(self.delete_professor_frame)
        self.label_14.setGeometry(QtCore.QRect(10, 170, 111, 16))
        self.label_14.setObjectName("label_14")
        
        self.delete_professor_entry = QtWidgets.QLineEdit(self.delete_professor_frame)
        self.delete_professor_entry.setGeometry(QtCore.QRect(120, 170, 181, 20))
        self.delete_professor_entry.setObjectName("delete_professor_entry")
        
        self.professor_delete_db_button = QtWidgets.QPushButton(self.delete_professor_frame)
        self.professor_delete_db_button.setGeometry(QtCore.QRect(380, 170, 75, 23))
        self.professor_delete_db_button.setObjectName("professor_delete_db_button")
        self.professor_delete_db_button.clicked.connect(self.del_professor_db)
        
        self.professor_delete_db_cancel = QtWidgets.QPushButton(self.delete_professor_frame)
        self.professor_delete_db_cancel.setGeometry(QtCore.QRect(460, 170, 75, 23))
        self.professor_delete_db_cancel.setObjectName("professor_delete_db_cancel")
        self.professor_delete_db_cancel.clicked.connect(self.close_del_professor)

        #add student to a class frame
        self.add_student_to_class_frame = QtWidgets.QFrame(admin_window)
        self.add_student_to_class_frame.setGeometry(QtCore.QRect(170, 0, 701, 131))
        self.add_student_to_class_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.add_student_to_class_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.add_student_to_class_frame.setObjectName("add_student_to_class_frame")
        self.add_student_to_class_frame.setVisible(False)
        
        self.label_21 = QtWidgets.QLabel(self.add_student_to_class_frame)
        self.label_21.setGeometry(QtCore.QRect(10, 20, 121, 16))
        self.label_21.setObjectName("label_21")
        
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.add_student_to_class_frame)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(10, 40, 331, 80))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        
        self.label_22 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_22.setObjectName("label_22")
        self.gridLayout_4.addWidget(self.label_22, 0, 0, 1, 1)
        
        self.label_23 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_23.setObjectName("label_23")
        self.gridLayout_4.addWidget(self.label_23, 1, 0, 1, 1)
        
        self.add_student_to_class_button = QtWidgets.QPushButton(self.gridLayoutWidget_4)
        self.add_student_to_class_button.setObjectName("add_student_to_class_button")
        self.add_student_to_class_button.clicked.connect(self.student_to_class)
        self.gridLayout_4.addWidget(self.add_student_to_class_button, 2, 1, 1, 1)
        
        self.add_student_to_class_cancel_button = QtWidgets.QPushButton(self.gridLayoutWidget_4)
        self.add_student_to_class_cancel_button.setObjectName("add_student_to_class_cancel_button")
        self.add_student_to_class_cancel_button.clicked.connect(self.close_student_to_class) 
        self.gridLayout_4.addWidget(self.add_student_to_class_cancel_button, 2, 2, 1, 1)
        
        self.add_student_class_entry = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.add_student_class_entry.setObjectName("add_student_class_entry")
        self.gridLayout_4.addWidget(self.add_student_class_entry, 1, 1, 1, 2)
        
        self.add_student_to_class_entry = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.add_student_to_class_entry.setObjectName("add_student_to_class_entry")
        self.gridLayout_4.addWidget(self.add_student_to_class_entry, 0, 1, 1, 2)

        #remove student from a class frame
        self.remove_student_frame = QtWidgets.QFrame(admin_window)
        self.remove_student_frame.setGeometry(QtCore.QRect(170, 0, 721, 211))
        self.remove_student_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.remove_student_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.remove_student_frame.setObjectName("remove_student_frame")
        self.remove_student_frame.setVisible(False)
        
        self.remove_student_scrollArea = QtWidgets.QScrollArea(self.remove_student_frame)
        self.remove_student_scrollArea.setGeometry(QtCore.QRect(10, 40, 611, 80))
        self.remove_student_scrollArea.setWidgetResizable(True)
        self.remove_student_scrollArea.setObjectName("remove_student_scrollArea")
        
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 609, 78))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.remove_student_scrollArea.setWidget(self.scrollAreaWidgetContents_4)
        
        self.remove_student_entry = QtWidgets.QLineEdit(self.remove_student_frame)
        self.remove_student_entry.setGeometry(QtCore.QRect(60, 130, 211, 20))
        self.remove_student_entry.setObjectName("remove_student_entry")
        
        self.label_24 = QtWidgets.QLabel(self.remove_student_frame)
        self.label_24.setGeometry(QtCore.QRect(10, 20, 161, 16))
        self.label_24.setObjectName("label_24")
        
        self.label_25 = QtWidgets.QLabel(self.remove_student_frame)
        self.label_25.setGeometry(QtCore.QRect(10, 130, 47, 13))
        self.label_25.setObjectName("label_25")
        
        self.label_26 = QtWidgets.QLabel(self.remove_student_frame)
        self.label_26.setGeometry(QtCore.QRect(10, 160, 47, 13))
        self.label_26.setObjectName("label_26")
        
        self.remove_student_class_entry = QtWidgets.QLineEdit(self.remove_student_frame)
        self.remove_student_class_entry.setGeometry(QtCore.QRect(60, 160, 211, 20))
        self.remove_student_class_entry.setObjectName("remove_student_class_entry")
        
        self.remove_student_button = QtWidgets.QPushButton(self.remove_student_frame)
        self.remove_student_button.setGeometry(QtCore.QRect(380, 140, 75, 23))
        self.remove_student_button.clicked.connect(self.remove_student)
        self.remove_student_button.setObjectName("remove_student_button")
        
        self.cancel_remove_student_button = QtWidgets.QPushButton(self.remove_student_frame)
        self.cancel_remove_student_button.setGeometry(QtCore.QRect(460, 140, 75, 23))
        self.cancel_remove_student_button.clicked.connect(self.close_remove_student)
        self.cancel_remove_student_button.setObjectName("cancel_remove_student_button")

        self.retranslateUi(admin_window)
        QtCore.QMetaObject.connectSlotsByName(admin_window)

    def retranslateUi(self, admin_window):
        _translate = QtCore.QCoreApplication.translate
        admin_window.setWindowTitle(_translate("admin_window", "Administrator"))
        self.add_student_button.setText(_translate("admin_window", "Add Student"))
        self.delete_student_button.setText(_translate("admin_window", "Delete Student"))
        self.add_professor_button.setText(_translate("admin_window", "Add Professor"))
        self.create_class.setText(_translate("admin_window", "Create Class"))
        self.delete_class.setText(_translate("admin_window", "Delete Class"))
        self.add_student_class_button.setText(_translate("admin_window", "Add student to class"))
        self.remove_student_frame_button.setText(_translate("admin_window", "Remove student from class"))
        self.delete_professor_button.setText(_translate("admin_window", "Delete Professor"))
        self.add_student_db_button.setText(_translate("admin_window", "Add"))
        self.label_3.setText(_translate("admin_window", "Username:"))
        self.label_2.setText(_translate("admin_window", "Email:"))
        self.label.setText(_translate("admin_window", "Name:"))
        self.label_5.setText(_translate("admin_window", "Password:"))
        self.add_student_cancel_db_button.setText(_translate("admin_window", "Cancel"))
        self.Genarate_user_pass_button.setText(_translate("admin_window", "Genarate User and Password"))
        self.label_6.setText(_translate("admin_window", "Create Student Account"))
        self.label_4.setText(_translate("admin_window", "Enter Student Name:"))
        self.delete_student_db_button.setText(_translate("admin_window", "Delete"))
        self.delete_student_cancel_db_button.setText(_translate("admin_window", "Cancel"))
        self.label_7.setText(_translate("admin_window", "Delete Student account"))
        self.label_9.setText(_translate("admin_window", "Email:"))
        self.label_11.setText(_translate("admin_window", "Password:"))
        self.label_10.setText(_translate("admin_window", "Username:"))
        self.label_8.setText(_translate("admin_window", "Name:"))
        self.add_professor_db_button.setText(_translate("admin_window", "Add"))
        self.add_professor_db_cancel_button.setText(_translate("admin_window", "Cancel"))
        self.Gen_professor_user_pass_button.setText(_translate("admin_window", "Genarate User and Password"))
        self.label_12.setText(_translate("admin_window", "Create Professor Account"))
        self.label_15.setText(_translate("admin_window", "Create Course"))
        self.label_16.setText(_translate("admin_window", "Name:"))
        self.label_18.setText(_translate("admin_window", "Professor:"))
        self.label_17.setText(_translate("admin_window", "Course Number:"))
        self.add_class_db_buttom.setText(_translate("admin_window", "Add"))
        self.add_class_db_cancel_button.setText(_translate("admin_window", "Cancel"))
        self.label_19.setText(_translate("admin_window", "Delete Course"))
        self.label_20.setText(_translate("admin_window", "Enter Course name:"))
        self.delete_class_db_button.setText(_translate("admin_window", "Delete"))
        self.delete_class_db_cancel_button.setText(_translate("admin_window", "Cancel"))
        self.label_13.setText(_translate("admin_window", "Delete Professor Account"))
        self.label_14.setText(_translate("admin_window", "Enter Professor name:"))
        self.professor_delete_db_button.setText(_translate("admin_window", "Delete"))
        self.professor_delete_db_cancel.setText(_translate("admin_window", "Cancel"))
        self.label_21.setText(_translate("admin_window", "Add student to Course"))
        self.label_22.setText(_translate("admin_window", "Student Name:"))
        self.label_23.setText(_translate("admin_window", "Course:"))
        self.add_student_to_class_button.setText(_translate("admin_window", "Add"))
        self.add_student_to_class_cancel_button.setText(_translate("admin_window", "Cancel"))
        self.label_24.setText(_translate("admin_window", "Remove student from Class"))
        self.label_25.setText(_translate("admin_window", "Student:"))
        self.label_26.setText(_translate("admin_window", "Course:"))
        self.remove_student_button.setText(_translate("admin_window", "Remove"))
        self.cancel_remove_student_button.setText(_translate("admin_window", "Cancel"))

    def show_create_student(self):
        #only show the one
        self.ad_add_frame.setVisible(True)
        self.ad_delete_frame.setVisible(False)
        self.add_professor_frame.setVisible(False)
        self.add_student_to_class_frame.setVisible(False)
        self.create_class_frame.setVisible(False)
        self.delete_class_frame.setVisible(False)
        self.delete_professor_frame.setVisible(False)
        self.remove_student_frame.setVisible(False)

    def show_delete_student(self):
        #only show the one
        self.ad_add_frame.setVisible(False)
        self.ad_delete_frame.setVisible(True)
        self.add_professor_frame.setVisible(False)
        self.add_student_to_class_frame.setVisible(False)
        self.create_class_frame.setVisible(False)
        self.delete_class_frame.setVisible(False)
        self.delete_professor_frame.setVisible(False)
        self.remove_student_frame.setVisible(False)
        self.update_delete_scroll()
        
    def update_delete_scroll(self):
        try:#DELETE STUDENT
            #utline = QtWidgets.QLabel(self.ad_delete_frame)
            self.outline='|Username||Pass||name||email||classes|\n'
            #self.detele_student_scrollArea.setWidget(outline)
            text = QtWidgets.QLabel(self.ad_delete_frame)
            text.setText(self.outline+self.show_student_db())
            self.detele_student_scrollArea.setWidget(text)
            #text.append(outline)
            #text.append(self.show_student_db())
            #text.setText('test2')
            #self.detele_student_scrollArea.setWidget(text)
        except Exception as err:
            print("Update scroll student:",err)
            self.messbox.about(self.messbox, "Error", str(err))

    def update_delete_scroll_pro(self):
        try:#delete professor 
            self.outline='|Username||Pass||name||email||classes|\n'
            text = QtWidgets.QLabel(self.ad_delete_frame)
            text.setText(self.outline+self.show_professor_db())
            self.delete_professor_scrollArea.setWidget(text)
        except Exception as err:
            print("Update scroll pro:", err)
            self.messbox.about(self.messbox, "Error", str(err))

    def update_delete_class_scroll(self):
        try:
            self.outline='Course name||Course number|| Professor\n'
            text = QtWidgets.QLabel(self.delete_class_frame)
            text.setText(self.outline+self.show_classes_db())#######################################
            self.delete_class_scrollArea.setWidget(text)
        except Exception as err:
            print('Update scroll class',err)
            self.messbox.about(self.messbox, "Error", str(err))

    def update_remove_student_scroll(self):
        try:
            self.outline="Class || student"
            all_class, cls = self.db.get_all_class_list()
            text = QtWidgets.QLabel(self.remove_student_frame)
            temp = ''
            #print(all_class)
            for i in range(len(cls)):
                temp+="\n--------------"+str(cls[i][0])+"--------------\n"
                temp+=self.outline+'\n'
                for e in all_class[i]:
                    temp+= ' || '.join(list(e)[:2])+'\n'
            text.setText(temp)
            self.remove_student_scrollArea.setWidget(text)
        except Exception as err:
            print("Update scroll class remove student",err)
            self.messbox.about(self.messbox, "Error", str(err))
        
    def show_add_professor(self):
        #only show the one
        self.ad_add_frame.setVisible(False)
        self.ad_delete_frame.setVisible(False)
        self.add_professor_frame.setVisible(True)
        self.add_student_to_class_frame.setVisible(False)
        self.create_class_frame.setVisible(False)
        self.delete_class_frame.setVisible(False)
        self.delete_professor_frame.setVisible(False)
        self.remove_student_frame.setVisible(False)

    def show_add_student_class(self):
        #only show the one
        self.ad_add_frame.setVisible(False)
        self.ad_delete_frame.setVisible(False)
        self.add_professor_frame.setVisible(False)
        self.add_student_to_class_frame.setVisible(True)
        self.create_class_frame.setVisible(False)
        self.delete_class_frame.setVisible(False)
        self.delete_professor_frame.setVisible(False)
        self.remove_student_frame.setVisible(False)

    def show_create_class(self):
        #only show the one
        self.ad_add_frame.setVisible(False)
        self.ad_delete_frame.setVisible(False)
        self.add_professor_frame.setVisible(False)
        self.add_student_to_class_frame.setVisible(False)
        self.create_class_frame.setVisible(True)
        self.delete_class_frame.setVisible(False)
        self.delete_professor_frame.setVisible(False)
        self.remove_student_frame.setVisible(False)

    def show_delete_class(self):
        #only show the one
        self.ad_add_frame.setVisible(False)
        self.ad_delete_frame.setVisible(False)
        self.add_professor_frame.setVisible(False)
        self.add_student_to_class_frame.setVisible(False)
        self.create_class_frame.setVisible(False)
        self.delete_class_frame.setVisible(True)
        self.delete_professor_frame.setVisible(False)
        self.remove_student_frame.setVisible(False)
        self.update_delete_class_scroll()

    def show_delete_professor(self):
        #only show the one
        self.ad_add_frame.setVisible(False)
        self.ad_delete_frame.setVisible(False)
        self.add_professor_frame.setVisible(False)
        self.add_student_to_class_frame.setVisible(False)
        self.create_class_frame.setVisible(False)
        self.delete_class_frame.setVisible(False)
        self.delete_professor_frame.setVisible(True)
        self.remove_student_frame.setVisible(False)
        self.update_delete_scroll_pro()

    def show_remove_student(self):
        #only show the one
        self.ad_add_frame.setVisible(False)
        self.ad_delete_frame.setVisible(False)
        self.add_professor_frame.setVisible(False)
        self.add_student_to_class_frame.setVisible(False)
        self.create_class_frame.setVisible(False)
        self.delete_class_frame.setVisible(False)
        self.delete_professor_frame.setVisible(False)
        self.remove_student_frame.setVisible(True)
        self.update_remove_student_scroll()

    def gen_user_pass(self):
        try:
            self.username = self.Email_lineEdit_2.text().split('@')[0]
            self.Genarated_username.setText(self.username)
            self.default_pass = self.gen_random() #random 8 character pass
            self.Genarated_password.setText(self.default_pass)
        except Exception as err:
            print("gen_user"+str(err))
            self.messbox.about(self.messbox, "Error", str(err))

    def gen_random(self):
        temp = ""
        for i in range(8):
            temp+= str(chr(random.randint(33, 90)))
        return temp

    def close_add_student(self):
        self.ad_add_frame.setVisible(False)
        self.Name_lineEdit.clear()
        self.Email_lineEdit_2.clear()
        self.Genarated_username.setText('')
        self.Genarated_password.setText('')
        pass
        
    def add_student_db(self):
        try:
            name = self.Name_lineEdit.text()
            email = self.Email_lineEdit_2.text()
            if(not self.db.is_in_student(name) and not self.db.is_in_student(self.username)):
                if(not self.db.is_in_student(email)):
                    enc_pas = self.enc.encrypt_mess(self.default_pass)
                    good = self.db.add_student(user=self.username, pas=enc_pas, name=name, email=email)
                    if(good):
                        self.messbox.about(self.messbox, "Success", "Account Created")
                    else:
                        self.messbox.about(self.messbox, "Error", "Creating the account failed.")
                else:
                    self.messbox.about(self.messbox, "Error", "There is an existing account with email")
            elif(self.db.is_in_student(email)):
                self.messbox.about(self.messbox, "Error", "There is an existing account with email")
            else:
                self.messbox.about(self.messbox, "Error", "Username taken")
            self.Name_lineEdit.clear()
            self.Email_lineEdit_2.clear()
            self.Genarated_username.setText('')
            self.Genarated_password.setText('')
        except Exception as err:
            print("add_student "+str(err))
            self.messbox.about(self.messbx, "Error", str(err))

    def show_student_db(self):
        temp = ""
        data = self.db.get_students()
        for d in data:
            for i in d:
                temp += '| '+str(i)+' |'
            temp +='\n'
        return temp
    
    def delete_student_db(self):
        try:
            name = self.delete_student_entry.text()
            if(self.db.is_in_student(name)):
                try:
                    self.db.del_student(name)
                except Exception as err:
                    print("delte"+str(err))
                    self.db.del_student_user(name)
            else:
                print("Error did not found User")
            print("del done")
            self.update_delete_scroll()
        except Exception as err:
            print(str(err))
            print('Error no user found')
            self.messbox.about(self.messbx, "Error", str(err))
                    
    def close_del_student_db(self):
        self.ad_delete_frame.setVisible(False)
        self.delete_student_entry.clear()

    def add_professor_db(self):
        try:
            name = self.lineEdit_2.text()
            email = self.lineEdit_3.text()
            if(not self.db.is_in_professor(name) and not self.db.is_in_professor(self.username)):
                if(not self.db.is_in_professor(email)):
                    enc_pas = self.enc.encrypt_mess(self.default_pass)
                    good = self.db.add_professor(user=self.username, pas=enc_pas, name=name, email=email)
                    if(good):
                        self.messbox.about(self.messbox, "Success", "Account Created")
                    else:
                        self.messbox.about(self.messbox, "Error", "Creating the account failed.")
                else:
                    self.messbox.about(self.messbox, "Error", "There is an existing account with email")
            elif(self.db.is_in_professor(email)):
                self.messbox.about(self.messbox, "Error", "There is an existing account with email")
            else:
                self.messbox.about(self.messbox, "Error", "Username taken")
            self.lineEdit_2.clear()
            self.lineEdit_3.clear()
            self.professor_password_label.setText('')
            self.professor_username_label.setText('')
        except Exception as err:
            print("add_professor "+str(err))
            self.messbox.about(self.messbx, "Error", str(err))

    def gen_user_pass_pro(self):
        try:
            self.username = self.lineEdit_3.text().split('@')[0]
            self.professor_username_label.setText(self.username)
            self.default_pass = self.gen_random() #random 8 character pass
            self.professor_password_label.setText(self.default_pass)
        except Exception as err:
            print("gen_user"+str(err))
            self.messbox.about(self.messbox, "Error", str(err))

    def gen_random(self):
        temp = ""
        for i in range(8):
            temp+= str(chr(random.randint(33, 90)))
        return temp

    def del_professor_db(self):
        try:
            name = self.delete_professor_entry.text()
            if(self.db.is_in_professor(name)):
                try:
                    self.db.del_professor(name)
                except Exception as err:
                    print("delte"+str(err))
                    try:
                        self.db.del_professor_user(name)
                    except Exception as err:
                        print("delete",err)
                        self.messbox.about(self.messbx, "Error", str(err))
            else:
                print("Error did not found User")
                self.messbox.about(self.messbx, "Error", "Error did not found user")
            print("del done")
            self.update_delete_scroll_pro()
        except Exception as err:
            print(str(err))
            print('Error no user found')
            self.messbox.about(self.messbx, "Error", str(err))

    def show_professor_db(self):
        temp = ""
        data = self.db.get_professors()
        for d in data:
            for i in d:
                temp += '| '+str(i)+' |'
            temp +='\n'
        return temp

    def close_add_professor(self):
        self.add_professor_frame.setVisible(False)
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()

    def close_del_professor(self):
        self.delete_professor_frame.setVisible(False)
        self.delete_professor_entry.clear()

    def create_course(self):
        try:
            name = self.class_name_entry.text()
            num = self.class_number_entry.text()
            prof = self.clas_professor_entry.text()
            self.db.create_class(name, num, prof)
            self.db.add_class(prof, name)
            self.class_name_entry.clear()
            self.class_number_entry.clear()
            self.clas_professor_entry.clear()
        except Exception as err:
            print("Err Create class:", err)
            self.messbox.about(self.messbox, "Error", str(err))

    def close_create_course(self):
        self.create_class_frame.setVisible(False)
        self.class_name_entry.clear()
        self.class_number_entry.clear()
        self.clas_professor_entry.clear()

    def delete_class_act(self):
        name = self.delete_class_entry.text()
        try:
            self.db.del_class(name)
            self.delete_class_entry.clear()
        except Exception as err:
            print("Error delete class",err)
            self.messbox.about(self.messbox, "Error", str(err))

    def close_delete_class(self):
        self.delete_class_frame.setVisible(False)
        self.delete_class_entry.clear()

    def show_classes_db(self):
        temp = ''
        data = self.db.get_classes()
        for i in data:
            temp += '||'.join(i)+'\n'
        return temp

    def student_to_class(self):
        clas = self.add_student_class_entry.text()
        name = self.add_student_to_class_entry.text()
        print(name)
        print(clas)
        try:
            self.db.add_class(name, clas)
            self.db.add_student_to_class(name, clas)
            print("Student added to class")
        except Exception as err:
            print("Error adding student to class:",err)
            self.messbox.about(self.messbox, "Error", str(err))
    
    def close_student_to_class(self):
        self.add_student_to_class_frame.setVisible(False)
        self.add_student_to_class_entry.clear()
        self.add_student_class_entry.clear()
        pass

    def remove_student(self):
        name = self.remove_student_entry.text()
        clas = self.remove_student_class_entry.text()
        #try:
        self.db.remove_student_from_class(name, clas)
        #except Exception as err:
            #print("Error remove student:", err)
            #self.messbox.about(self.messbox, "Error", str(err))
        self.remove_student_entry.clear()
        #self.remove_student_class_entry.clear()
        self.update_remove_student_scroll()

    def close_remove_student(self):
        self.remove_student_class_entry.clear()
        self.remove_student_entry.clear()
        self.remove_student_frame.setVisible(False)

    



        
