# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'task.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDialog,
    QFrame, QLabel, QPlainTextEdit, QPushButton,
    QSizePolicy, QWidget)
import res_rc

class Ui_Add_Task(object):
    def setupUi(self, Add_Task):
        if not Add_Task.objectName():
            Add_Task.setObjectName(u"Add_Task")
        Add_Task.resize(400, 409)
        Add_Task.setStyleSheet(u"background-color:qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));\n"
"font-family: Segoe UI")
        self.frame_task = QFrame(Add_Task)
        self.frame_task.setObjectName(u"frame_task")
        self.frame_task.setGeometry(QRect(10, 10, 381, 391))
        self.frame_task.setStyleSheet(u"background-color:rgba(255,255,255,30);\n"
"border:1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;")
        self.frame_task.setFrameShape(QFrame.StyledPanel)
        self.frame_task.setFrameShadow(QFrame.Raised)
        self.lbl_new_task = QLabel(self.frame_task)
        self.lbl_new_task.setObjectName(u"lbl_new_task")
        self.lbl_new_task.setGeometry(QRect(170, 0, 41, 41))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(15)
        font.setBold(True)
        self.lbl_new_task.setFont(font)
        self.lbl_new_task.setStyleSheet(u"background-color: transparent;\n"
"border: none;\n"
"color: white;")
        self.lbl_name = QLabel(self.frame_task)
        self.lbl_name.setObjectName(u"lbl_name")
        self.lbl_name.setGeometry(QRect(20, 30, 61, 41))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(15)
        font1.setBold(False)
        self.lbl_name.setFont(font1)
        self.lbl_name.setStyleSheet(u"background-color: transparent;\n"
"border: none;\n"
"color: white;")
        self.lbl_description = QLabel(self.frame_task)
        self.lbl_description.setObjectName(u"lbl_description")
        self.lbl_description.setGeometry(QRect(20, 190, 111, 41))
        self.lbl_description.setFont(font1)
        self.lbl_description.setStyleSheet(u"background-color: transparent;\n"
"border: none;\n"
"color: white;")
        self.description_value = QPlainTextEdit(self.frame_task)
        self.description_value.setObjectName(u"description_value")
        self.description_value.setGeometry(QRect(20, 230, 351, 101))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(14)
        self.description_value.setFont(font2)
        self.description_value.setStyleSheet(u"color: white;")
        self.name_value = QPlainTextEdit(self.frame_task)
        self.name_value.setObjectName(u"name_value")
        self.name_value.setGeometry(QRect(20, 70, 351, 41))
        self.name_value.setFont(font2)
        self.name_value.setStyleSheet(u"color: white;")
        self.lbl_status = QLabel(self.frame_task)
        self.lbl_status.setObjectName(u"lbl_status")
        self.lbl_status.setGeometry(QRect(20, 120, 61, 41))
        self.lbl_status.setFont(font1)
        self.lbl_status.setStyleSheet(u"background-color: transparent;\n"
"border: none;\n"
"color: white;")
        self.status_value = QComboBox(self.frame_task)
        self.status_value.addItem(u"New")
        self.status_value.addItem("")
        self.status_value.addItem("")
        self.status_value.addItem("")
        self.status_value.setObjectName(u"status_value")
        self.status_value.setGeometry(QRect(20, 160, 171, 31))
        self.status_value.setFont(font2)
        self.status_value.setStyleSheet(u"QComboBox {\n"
"color: white;\n"
"}\n"
"\n"
"QComboBox:item {\n"
"\n"
"}")
        self.btn_save = QPushButton(self.frame_task)
        self.btn_save.setObjectName(u"btn_save")
        self.btn_save.setGeometry(QRect(100, 350, 91, 31))
        self.btn_save.setFont(font2)
        self.btn_save.setStyleSheet(u"QPushButton{\n"
"color: white;\n"
"background-color:rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,30);\n"
"border-radius: 7px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255,255,255,40);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255,255,255,70);\n"
"}")
        self.btn_cancel = QPushButton(self.frame_task)
        self.btn_cancel.setObjectName(u"btn_cancel")
        self.btn_cancel.setGeometry(QRect(200, 350, 91, 31))
        self.btn_cancel.setFont(font2)
        self.btn_cancel.setStyleSheet(u"QPushButton{\n"
"color: white;\n"
"background-color:rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,30);\n"
"border-radius: 7px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255,255,255,40);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255,255,255,70);\n"
"}")
        self.lbl_deadline = QLabel(self.frame_task)
        self.lbl_deadline.setObjectName(u"lbl_deadline")
        self.lbl_deadline.setGeometry(QRect(210, 120, 81, 41))
        self.lbl_deadline.setFont(font1)
        self.lbl_deadline.setStyleSheet(u"background-color: transparent;\n"
"border: none;\n"
"color: white;")
        self.deadline_value = QDateEdit(self.frame_task)
        self.deadline_value.setObjectName(u"deadline_value")
        self.deadline_value.setGeometry(QRect(210, 161, 151, 31))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(12)
        self.deadline_value.setFont(font3)
        self.deadline_value.setStyleSheet(u"color: white;")
        self.deadline_value.setDate(QDate(2023, 1, 1))

        self.retranslateUi(Add_Task)

        self.status_value.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(Add_Task)
    # setupUi

    def retranslateUi(self, Add_Task):
        Add_Task.setWindowTitle(QCoreApplication.translate("Add_Task", u"Add task", None))
        self.lbl_new_task.setText(QCoreApplication.translate("Add_Task", u"Task", None))
        self.lbl_name.setText(QCoreApplication.translate("Add_Task", u"Name", None))
        self.lbl_description.setText(QCoreApplication.translate("Add_Task", u"Description", None))
        self.lbl_status.setText(QCoreApplication.translate("Add_Task", u"Status", None))
        self.status_value.setItemText(1, QCoreApplication.translate("Add_Task", u"In progress", None))
        self.status_value.setItemText(2, QCoreApplication.translate("Add_Task", u"Completed", None))
        self.status_value.setItemText(3, QCoreApplication.translate("Add_Task", u"Canceled", None))

        self.btn_save.setText(QCoreApplication.translate("Add_Task", u"Save", None))
        self.btn_cancel.setText(QCoreApplication.translate("Add_Task", u"Cancel", None))
        self.lbl_deadline.setText(QCoreApplication.translate("Add_Task", u"Deadline", None))
    # retranslateUi

