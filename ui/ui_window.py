# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QRadioButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(451, 611)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"#centralwidget {\n"
"	background-color: #3b3a3a\n"
"}\n"
"\n"
"QFrame {\n"
"	background-color: #575757;\n"
"	padding: 5px;\n"
"	border: 5px solid #575757;\n"
"	border-radius: 10px\n"
"}\n"
"\n"
"QLabel, QRadioButton {\n"
"	color: #fff\n"
"}\n"
"\n"
"QLineEdit, QPushButton {\n"
"	padding: 6px\n"
"}\n"
"\n"
"QLineEdit {\n"
"	border: 1px solid #fff;\n"
"	border-radius: 2px;\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"	background-color: #3b3a3a;\n"
"	border: 1px solid #3b3a3a;\n"
"}\n"
"\n"
"QPushButton {\n"
"	background-color: #f59b42;\n"
"	border: 1px solid #f59b42;\n"
"	border-radius: 2px;\n"
"	color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: orange;\n"
"	border: 1px solid orange;\n"
"}\n"
"\n"
"#pushButtonTest {\n"
"	margin-top: 5px\n"
"}\n"
"\n"
"")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(800, 16777215))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame)
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 60))
        self.label.setMaximumSize(QSize(16777215, 60))
        font = QFont()
        font.setPointSize(28)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.label)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(0, 50))
        self.label_8.setMaximumSize(QSize(16777215, 50))
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        self.label_8.setFont(font1)
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_8.setMargin(0)

        self.verticalLayout_3.addWidget(self.label_8)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(100, 36))
        self.label_2.setMaximumSize(QSize(16777215, 36))

        self.horizontalLayout.addWidget(self.label_2)

        self.lineEditUser = QLineEdit(self.frame)
        self.lineEditUser.setObjectName(u"lineEditUser")
        self.lineEditUser.setMinimumSize(QSize(0, 32))
        self.lineEditUser.setMaximumSize(QSize(16777215, 32))

        self.horizontalLayout.addWidget(self.lineEditUser)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(100, 36))
        self.label_3.setMaximumSize(QSize(16777215, 36))

        self.horizontalLayout_2.addWidget(self.label_3)

        self.lineEditPwd = QLineEdit(self.frame)
        self.lineEditPwd.setObjectName(u"lineEditPwd")
        self.lineEditPwd.setMinimumSize(QSize(0, 32))
        self.lineEditPwd.setMaximumSize(QSize(16777215, 32))

        self.horizontalLayout_2.addWidget(self.lineEditPwd)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(100, 36))
        self.label_4.setMaximumSize(QSize(16777215, 36))

        self.horizontalLayout_3.addWidget(self.label_4)

        self.lineEditHost = QLineEdit(self.frame)
        self.lineEditHost.setObjectName(u"lineEditHost")
        self.lineEditHost.setMinimumSize(QSize(0, 32))
        self.lineEditHost.setMaximumSize(QSize(16777215, 32))

        self.horizontalLayout_3.addWidget(self.lineEditHost)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(100, 36))
        self.label_5.setMaximumSize(QSize(16777215, 36))

        self.horizontalLayout_4.addWidget(self.label_5)

        self.lineEditPort = QLineEdit(self.frame)
        self.lineEditPort.setObjectName(u"lineEditPort")
        self.lineEditPort.setMinimumSize(QSize(0, 32))
        self.lineEditPort.setMaximumSize(QSize(16777215, 32))

        self.horizontalLayout_4.addWidget(self.lineEditPort)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.radioButtonSID = QRadioButton(self.frame)
        self.radioButtonSID.setObjectName(u"radioButtonSID")
        self.radioButtonSID.setMinimumSize(QSize(100, 36))
        self.radioButtonSID.setMaximumSize(QSize(16777215, 36))

        self.horizontalLayout_5.addWidget(self.radioButtonSID)

        self.lineEditSID = QLineEdit(self.frame)
        self.lineEditSID.setObjectName(u"lineEditSID")
        self.lineEditSID.setEnabled(False)
        self.lineEditSID.setMinimumSize(QSize(0, 32))
        self.lineEditSID.setMaximumSize(QSize(16777215, 32))

        self.horizontalLayout_5.addWidget(self.lineEditSID)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.radioButtonSerName = QRadioButton(self.frame)
        self.radioButtonSerName.setObjectName(u"radioButtonSerName")
        self.radioButtonSerName.setMinimumSize(QSize(100, 36))
        self.radioButtonSerName.setMaximumSize(QSize(16777215, 36))
        self.radioButtonSerName.setChecked(True)

        self.horizontalLayout_6.addWidget(self.radioButtonSerName)

        self.lineEditSerName = QLineEdit(self.frame)
        self.lineEditSerName.setObjectName(u"lineEditSerName")
        self.lineEditSerName.setEnabled(True)
        self.lineEditSerName.setMinimumSize(QSize(0, 32))
        self.lineEditSerName.setMaximumSize(QSize(16777215, 32))

        self.horizontalLayout_6.addWidget(self.lineEditSerName)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.pushButtonTest = QPushButton(self.frame)
        self.pushButtonTest.setObjectName(u"pushButtonTest")

        self.verticalLayout_3.addWidget(self.pushButtonTest)


        self.verticalLayout_6.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_9 = QLabel(self.frame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(0, 50))
        self.label_9.setMaximumSize(QSize(16777215, 50))
        self.label_9.setFont(font1)
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_9)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(100, 36))
        self.label_6.setMaximumSize(QSize(16777215, 36))

        self.horizontalLayout_7.addWidget(self.label_6)

        self.lineEditScript = QLineEdit(self.frame)
        self.lineEditScript.setObjectName(u"lineEditScript")
        self.lineEditScript.setMinimumSize(QSize(0, 32))
        self.lineEditScript.setMaximumSize(QSize(16777215, 32))
        self.lineEditScript.setReadOnly(True)

        self.horizontalLayout_7.addWidget(self.lineEditScript)

        self.pushButtonScript = QPushButton(self.frame)
        self.pushButtonScript.setObjectName(u"pushButtonScript")

        self.horizontalLayout_7.addWidget(self.pushButtonScript)


        self.verticalLayout.addLayout(self.horizontalLayout_7)


        self.verticalLayout_4.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(100, 36))
        self.label_7.setMaximumSize(QSize(16777215, 36))

        self.horizontalLayout_8.addWidget(self.label_7)

        self.lineEditKey = QLineEdit(self.frame)
        self.lineEditKey.setObjectName(u"lineEditKey")
        self.lineEditKey.setMinimumSize(QSize(0, 32))
        self.lineEditKey.setMaximumSize(QSize(16777215, 32))
        self.lineEditKey.setReadOnly(True)

        self.horizontalLayout_8.addWidget(self.lineEditKey)

        self.pushButtonKey = QPushButton(self.frame)
        self.pushButtonKey.setObjectName(u"pushButtonKey")
        self.pushButtonKey.setMinimumSize(QSize(0, 30))
        self.pushButtonKey.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_8.addWidget(self.pushButtonKey)


        self.verticalLayout_2.addLayout(self.horizontalLayout_8)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)


        self.verticalLayout_6.addLayout(self.verticalLayout_4)

        self.pushButton_4 = QPushButton(self.frame)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.verticalLayout_6.addWidget(self.pushButton_4)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.radioButtonSID.toggled.connect(self.lineEditSID.setEnabled)
        self.radioButtonSerName.toggled.connect(self.lineEditSerName.setEnabled)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Executador de Scripts", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Conex\u00e3o Oracle Database", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"User:", None))
        self.lineEditUser.setPlaceholderText(QCoreApplication.translate("MainWindow", u"User...", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Password:", None))
        self.lineEditPwd.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password...", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Hostname:", None))
        self.lineEditHost.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Hostname", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Port:", None))
        self.lineEditPort.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Port...", None))
        self.radioButtonSID.setText(QCoreApplication.translate("MainWindow", u"SID:", None))
        self.radioButtonSerName.setText(QCoreApplication.translate("MainWindow", u"Service Name:", None))
        self.pushButtonTest.setText(QCoreApplication.translate("MainWindow", u"Testar conex\u00e3o", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Selecionar Script", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Script:", None))
        self.lineEditScript.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Selecione um Script...", None))
        self.pushButtonScript.setText(QCoreApplication.translate("MainWindow", u"Selecionar Arquivo", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Key:", None))
        self.lineEditKey.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Selecione uma Chave...", None))
        self.pushButtonKey.setText(QCoreApplication.translate("MainWindow", u"Selecionar Arquivo", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Run", None))
    # retranslateUi

