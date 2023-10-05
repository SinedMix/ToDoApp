# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main2.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QTableView, QWidget)
import res_rc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(716, 653)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(716, 653))
        MainWindow.setMaximumSize(QSize(716, 653))
        icon = QIcon()
        icon.addFile(u":/icon/icons/main_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color:qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));\n"
"font-family: Segoe UI")
        MainWindow.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.centralwidget.setMinimumSize(QSize(716, 653))
        self.centralwidget.setMaximumSize(QSize(716, 653))
        self.centralwidget.setSizeIncrement(QSize(716, 653))
        self.centralwidget.setBaseSize(QSize(716, 653))
        self.lbl_name_tasklist = QLabel(self.centralwidget)
        self.lbl_name_tasklist.setObjectName(u"lbl_name_tasklist")
        self.lbl_name_tasklist.setEnabled(True)
        self.lbl_name_tasklist.setGeometry(QRect(20, 10, 161, 61))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(32)
        self.lbl_name_tasklist.setFont(font)
        self.lbl_name_tasklist.setStyleSheet(u"background-color: transparent;\n"
"color: white;")
        self.tbl_tasklist = QTableView(self.centralwidget)
        self.tbl_tasklist.setObjectName(u"tbl_tasklist")
        self.tbl_tasklist.setGeometry(QRect(20, 121, 680, 521))
        self.tbl_tasklist.setStyleSheet(u"QTableView {\n"
"border-radius: 7px;\n"
"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"}\n"
"QTableView::section {\n"
"background-color: rgba(53,53,53);\n"
"border: none;\n"
"color:white;\n"
"height: 50px;\n"
"font-size: 14pt\n"
"}\n"
"\n"
"QTableView::item {\n"
"border-style: none;\n"
"border-bottom: rgba(255,255,255,50);\n"
"}\n"
"\n"
"QTableView::item:selected {\n"
"border: none;\n"
"color: rgba(255,255,255);\n"
"background-color: rgba(255,255,255,50);\n"
"}\n"
"")
        self.tbl_tasklist.horizontalHeader().setMinimumSectionSize(50)
        self.tbl_tasklist.horizontalHeader().setDefaultSectionSize(110)
        self.buttons = QFrame(self.centralwidget)
        self.buttons.setObjectName(u"buttons")
        self.buttons.setEnabled(True)
        self.buttons.setGeometry(QRect(20, 70, 681, 47))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setKerning(True)
        self.buttons.setFont(font1)
        self.buttons.setStyleSheet(u"background-color:rgba(255,255,255,30);\n"
"border:1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;")
        self.horizontalLayout = QHBoxLayout(self.buttons)
        self.horizontalLayout.setSpacing(16)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_add_task = QPushButton(self.buttons)
        self.btn_add_task.setObjectName(u"btn_add_task")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(10)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_add_task.sizePolicy().hasHeightForWidth())
        self.btn_add_task.setSizePolicy(sizePolicy2)
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(14)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setStyleStrategy(QFont.PreferDefault)
        self.btn_add_task.setFont(font2)
        self.btn_add_task.setStyleSheet(u"QPushButton{\n"
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
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/icon/icons/add.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_add_task.setIcon(icon1)

        self.horizontalLayout.addWidget(self.btn_add_task)

        self.btn_edit_task = QPushButton(self.buttons)
        self.btn_edit_task.setObjectName(u"btn_edit_task")
        sizePolicy2.setHeightForWidth(self.btn_edit_task.sizePolicy().hasHeightForWidth())
        self.btn_edit_task.setSizePolicy(sizePolicy2)
        self.btn_edit_task.setFont(font2)
        self.btn_edit_task.setStyleSheet(u"QPushButton{\n"
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
        icon2 = QIcon()
        icon2.addFile(u":/icon/icons/edit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_edit_task.setIcon(icon2)

        self.horizontalLayout.addWidget(self.btn_edit_task)

        self.btn_delete_task = QPushButton(self.buttons)
        self.btn_delete_task.setObjectName(u"btn_delete_task")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(10)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.btn_delete_task.sizePolicy().hasHeightForWidth())
        self.btn_delete_task.setSizePolicy(sizePolicy3)
        self.btn_delete_task.setFont(font2)
        self.btn_delete_task.setStyleSheet(u"QPushButton{\n"
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
        icon3 = QIcon()
        icon3.addFile(u":/icon/icons/delete.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_delete_task.setIcon(icon3)

        self.horizontalLayout.addWidget(self.btn_delete_task)

        self.btn_export_xls = QPushButton(self.buttons)
        self.btn_export_xls.setObjectName(u"btn_export_xls")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(12)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.btn_export_xls.sizePolicy().hasHeightForWidth())
        self.btn_export_xls.setSizePolicy(sizePolicy4)
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(255, 255, 255, 30))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.btn_export_xls.setPalette(palette)
        self.btn_export_xls.setFont(font2)
        self.btn_export_xls.setStyleSheet(u"QPushButton{\n"
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
        icon4 = QIcon()
        icon4.addFile(u":/icon/icons/export.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_export_xls.setIcon(icon4)

        self.horizontalLayout.addWidget(self.btn_export_xls)

        MainWindow.setCentralWidget(self.centralwidget)
#if QT_CONFIG(shortcut)
        self.lbl_name_tasklist.setBuddy(self.buttons)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ToDo Application", None))
        self.lbl_name_tasklist.setText(QCoreApplication.translate("MainWindow", u"Task list", None))
        self.btn_add_task.setText(QCoreApplication.translate("MainWindow", u"Add task", None))
        self.btn_edit_task.setText(QCoreApplication.translate("MainWindow", u"Edit task", None))
        self.btn_delete_task.setText(QCoreApplication.translate("MainWindow", u"Delete task", None))
        self.btn_export_xls.setText(QCoreApplication.translate("MainWindow", u"Export to Excel", None))
    # retranslateUi

