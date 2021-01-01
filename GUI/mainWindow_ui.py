import requests
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QCursor
from voice_assistant.friday_voice_engine import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 720)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.dropShadowFrame = QtWidgets.QFrame(self.centralwidget)
        self.dropShadowFrame.setMinimumSize(QtCore.QSize(400, 720))
        self.dropShadowFrame.setStyleSheet("#dropShadowFrame {\n"
                                           "background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0.975369, y2:0.0340909, stop:0 rgba(9, 0, 113, 255), stop:0.852217 rgba(89, 0, 108, 255));\n"
                                           "}\n"
                                           "\n"
                                           "")
        self.dropShadowFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.dropShadowFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.dropShadowFrame.setObjectName("dropShadowFrame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.dropShadowFrame)
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_3 = QtWidgets.QFrame(self.dropShadowFrame)
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 75))
        self.frame_3.setStyleSheet("border: 0;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setContentsMargins(0, 10, 0, 5)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Abnes")
        font.setPointSize(44)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("color: white; \n"
                                 "font: \"Abnes\";\n"
                                 "dropShadowFrame")
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setLineWidth(0)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setIndent(0)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Megrim")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: white;n")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.dropShadowFrame)
        font = QtGui.QFont()
        font.setFamily("Earth Orbiter")
        font.setPointSize(18)
        self.frame_4.setFont(font)
        self.frame_4.setStyleSheet("border:0;")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setLineWidth(0)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_2 = QtWidgets.QFrame(self.frame_4)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_4.addWidget(self.frame_2)
        self.frame_5 = QtWidgets.QFrame(self.frame_4)
        self.frame_5.setMinimumSize(QtCore.QSize(0, 233))
        self.frame_5.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.assistant_button = QtWidgets.QPushButton(self.frame_5)
        self.assistant_button.setMinimumSize(QtCore.QSize(180, 180))
        self.assistant_button.setMaximumSize(QtCore.QSize(180, 180))
        self.assistant_button_stylesheet = "\nQPushButton\n{\nborder-radius: 90px;\nbackground: qlineargradient(spread:pad, x1:0, y1:1, x2:0.975369, y2:0.0340909, stop:0 rgba(3, 4, 64, 255), stop:0.852217 rgba(49, 3, 61, 255));\n\n}\n\nQPushButton:hover:!pressed\n{\nbackground: qlineargradient(spread:pad, x1:0, y1:1, x2:0.975369, y2:0.0340909, stop:0 rgba(2, 4, 48, 255), stop:0.852217 rgba(40, 3, 50, 255))\n\n}"
        self.assistant_button.setStyleSheet(self.assistant_button_stylesheet)
        self.assistant_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/white-mic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.assistant_button.setIcon(icon)
        self.assistant_button.setIconSize(QtCore.QSize(140, 140))
        self.assistant_button.setObjectName("assistant_button")
        self.verticalLayout_6.addWidget(self.assistant_button)
        self.assistant_state_label = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setFamily("Earth Orbiter")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.assistant_state_label.setFont(font)
        self.assistant_state_label.setStyleSheet("color: white;\n"
                                                 "font: 20pt \"Earth Orbiter\";")
        self.assistant_state_label.setObjectName("assistant_state_label")
        self.verticalLayout_6.addWidget(self.assistant_state_label, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_4.addWidget(self.frame_5, 0, QtCore.Qt.AlignHCenter)
        self.frame_6 = QtWidgets.QFrame(self.frame_4)
        self.frame_6.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Earth Orbiter")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.frame_6.setFont(font)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_7.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_7.setSpacing(3)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_8 = QtWidgets.QFrame(self.frame_6)
        self.frame_8.setMinimumSize(QtCore.QSize(0, 100))
        self.frame_8.setMaximumSize(QtCore.QSize(16777215, 230))
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.user_input_textedit = QtWidgets.QTextEdit(self.frame_8)
        font = QtGui.QFont()
        font.setFamily("Geneva")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.user_input_textedit.setFont(font)
        self.user_input_textedit.setStyleSheet("background: transparent;\n"
                                               "color: white;\n"
                                               "font: 20pt \"Geneva\";")
        self.user_input_textedit.setReadOnly(True)
        self.user_input_textedit.setObjectName("user_input_textedit")
        self.horizontalLayout_2.addWidget(self.user_input_textedit)
        self.verticalLayout_7.addWidget(self.frame_8)
        self.frame_9 = QtWidgets.QFrame(self.frame_6)
        self.frame_9.setMinimumSize(QtCore.QSize(0, 200))
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_9)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.frame_10 = QtWidgets.QFrame(self.frame_9)
        self.frame_10.setMinimumSize(QtCore.QSize(340, 50))
        self.frame_10.setMaximumSize(QtCore.QSize(16777215, 65))
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.gpio_label = QtWidgets.QLabel(self.frame_10)
        self.gpio_label.setMaximumSize(QtCore.QSize(48, 16777215))
        font = QtGui.QFont()
        font.setFamily("Geneva")
        font.setPointSize(16)
        self.gpio_label.setFont(font)
        self.gpio_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.gpio_label.setObjectName("gpio_label")
        self.horizontalLayout_4.addWidget(self.gpio_label)
        self.channel_selection = QtWidgets.QComboBox(self.frame_10)
        self.channel_selection.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.channel_selection.sizePolicy().hasHeightForWidth())
        self.channel_selection.setSizePolicy(sizePolicy)
        self.channel_selection.setMinimumSize(QtCore.QSize(0, 40))
        self.channel_selection.setMaximumSize(QtCore.QSize(310, 16777215))
        font = QtGui.QFont()
        font.setFamily("Geneva")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.channel_selection.setFont(font)
        self.channel_selection.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.channel_selection.setStyleSheet("QComboBox{\n"
                                             "  border: 2px solid rgb(0, 0, 96);\n"
                                             "  border-radius: 20px;\n"
                                             "  color: #FFF; \n"
                                             "  padding-left: 20px;\n"
                                             "  padding-right: 0px;\n"
                                             "  background-color:rgb(0, 0, 96);\n"
                                             "}\n"
                                             "QComboBox::drop-down{\n"
                                             "  background-color: transparent;\n"
                                             "  width: 40px;\n"
                                             "}\n"
                                             "QComboBox::down-arrow {\n"
                                             "color: white;\n"
                                             "}\n"
                                             "QComboBox QAbstractItemView {\n"
                                             "  border: 1px solid white;\n"
                                             "  border-radius: 5px;\n"
                                             "  selection-background-color: rgb(0, 0, 96);\n"
                                             "  font: 15pt \"Geneva\";\n"
                                             "  color: rgb(0, 0, 96);\n"
                                             "  selection-color: white;\n"
                                             "}\n"
                                             "QComboBox QAbstractItemView::item {\n"
                                             "  min-height: 50px;\n"
                                             "  border: 5px solid white;\n"
                                             "}\n"
                                             "\n"
                                             "QComboBox:disabled {\n"
                                             "    background-color: rgb(108, 135, 158);\n"
                                             "    border: 2px solid rgb(108, 135, 158);\n"
                                             "}\n"
                                             "\n"
                                             "QComboBox:editable {\n"
                                             "    background-color: rgb(0,0,96);\n"
                                             "    padding-right: 15px;\n"
                                             "    font: 15pt \"Geneva\";\n"
                                             "    color:white;\n"
                                             "}\n"
                                             "")
        self.channel_selection.setEditable(True)
        self.channel_selection.setObjectName("channel_selection")
        self.channel_selection.addItem(" ")
        for channel_id in range(1, 28):
            if channel_id not in [1, 14, 15]:
                self.channel_selection.addItem("CHANNEL: {}".format(channel_id))

        self.horizontalLayout_4.addWidget(self.channel_selection)
        self.verticalLayout_8.addWidget(self.frame_10)
        self.frame_11 = QtWidgets.QFrame(self.frame_9)
        self.frame_11.setMinimumSize(QtCore.QSize(0, 145))
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_11)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.radio_digital = QtWidgets.QFrame(self.frame_11)
        self.radio_digital.setMaximumSize(QtCore.QSize(16777215, 25))
        self.radio_digital.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.radio_digital.setFrameShadow(QtWidgets.QFrame.Raised)
        self.radio_digital.setObjectName("radio_digital")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.radio_digital)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.radioButton = QtWidgets.QRadioButton(self.radio_digital)
        self.radioButton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.radioButton.setStyleSheet("color: white")
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout_3.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.radio_digital)
        self.radioButton_2.setMaximumSize(QtCore.QSize(90, 35))
        self.radioButton_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout_3.addWidget(self.radioButton_2)
        self.verticalLayout_9.addWidget(self.radio_digital)
        self.frame_13 = QtWidgets.QFrame(self.frame_11)
        self.frame_13.setMaximumSize(QtCore.QSize(16777215, 59))
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_13)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.value_label = QtWidgets.QLabel(self.frame_13)
        self.value_label.setMinimumSize(QtCore.QSize(0, 0))
        self.value_label.setMaximumSize(QtCore.QSize(63, 16777215))
        font = QtGui.QFont()
        font.setFamily("Geneva")
        font.setPointSize(16)
        self.value_label.setFont(font)
        self.value_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.value_label.setObjectName("value_label")
        self.horizontalLayout_5.addWidget(self.value_label)
        self.value_line_edit = QtWidgets.QLineEdit(self.frame_13)
        self.value_line_edit.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.value_line_edit.sizePolicy().hasHeightForWidth())
        self.value_line_edit.setSizePolicy(sizePolicy)
        self.value_line_edit.setMinimumSize(QtCore.QSize(0, 40))
        self.value_line_edit.setMaximumSize(QtCore.QSize(280, 40))
        font = QtGui.QFont()
        font.setFamily("Geneva")
        font.setPointSize(11)
        self.value_line_edit.setFont(font)
        self.value_line_edit.setStyleSheet("QLineEdit {\n"
                                           "border: 2px solid rgb(0, 0, 96);\n"
                                           "border-radius: 20px;\n"
                                           "color: #FFF; \n"
                                           "padding-left: 20px;\n"
                                           "padding-right: 20px;\n"
                                           "background-color:rgb(0, 0, 96);\n"
                                           "} \n"
                                           "\n"
                                           "QLineEdit:enabled {\n"
                                           "border: 2px solid rgb(0, 0, 96);\n"
                                           "border-radius: 20px;\n"
                                           "color: #FFF; \n"
                                           "padding-left: 20px;\n"
                                           "padding-right: 20px;\n"
                                           "background-color:rgb(0, 0, 96);\n"
                                           "} \n"
                                           "\n"
                                           "\n"
                                           "QLineEdit:disabled {\n"
                                           "    background-color: rgb(108, 135, 158);\n"
                                           "    border: 2px solid rgb(108, 135, 158);\n"
                                           "}\n"
                                           "\n"
                                           "QLineEdit:hover { \n"
                                           "border: 2px solid rgb(15, 102, 255); \n"
                                           "}\n"
                                           "\n"
                                           "QLineEdit:focus {\n"
                                           " border: 2px solid rgb(85, 170, 255);\n"
                                           " background-color: rgb(0, 0, 96);\n"
                                           "}")
        self.value_line_edit.setObjectName("value_line_edit")
        self.horizontalLayout_5.addWidget(self.value_line_edit)
        self.send_button = QtWidgets.QPushButton(self.frame_13)
        self.send_button.setMinimumSize(QtCore.QSize(35, 35))
        self.send_button.setMaximumSize(QtCore.QSize(35, 35))
        self.send_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("assets/send.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.send_button.setIcon(icon1)
        self.send_button.setIconSize(QtCore.QSize(35, 35))
        self.send_button.setObjectName("send_button")
        self.horizontalLayout_5.addWidget(self.send_button)
        self.verticalLayout_9.addWidget(self.frame_13)
        self.verticalLayout_8.addWidget(self.frame_11)
        self.verticalLayout_7.addWidget(self.frame_9)
        self.verticalLayout_4.addWidget(self.frame_6)
        self.frame_7 = QtWidgets.QFrame(self.frame_4)
        self.frame_7.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_7.setStyleSheet("")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.raspbery_status_toast = QtWidgets.QLabel(self.frame_7)
        font = QtGui.QFont()
        font.setFamily("Futura Bk BT")
        font.setPointSize(23)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.raspbery_status_toast.setFont(font)
        self.raspbery_status_toast.setStyleSheet("font: 23pt \"Futura Bk BT\";\n"
                                                 "color: rgb(34, 255, 61)")
        self.raspbery_status_toast.setAlignment(QtCore.Qt.AlignCenter)
        self.raspbery_status_toast.setObjectName("raspbery_status_toast")
        self.verticalLayout_5.addWidget(self.raspbery_status_toast)
        self.verticalLayout_4.addWidget(self.frame_7)
        self.verticalLayout_2.addWidget(self.frame_4)
        self.frame = QtWidgets.QFrame(self.dropShadowFrame)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.frame.setFont(font)
        self.frame.setStyleSheet("border:0;\n"
                                 "color: white;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setMaximumSize(QtCore.QSize(32, 16777215))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(23)
        font.setItalic(False)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.label_3 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Earth Orbiter")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.verticalLayout_2.addWidget(self.frame)
        self.verticalLayout.addWidget(self.dropShadowFrame)
        MainWindow.setCentralWidget(self.centralwidget)

        # custom code below

        self.isAssistantListening = False
        self.check_connectivity()
        self.send_button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.assistant_button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.radioButton.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.radioButton_2.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.assistant_button.clicked.connect(lambda: self.onVoiceAssistantClickEventHandler())
        self.send_button.clicked.connect(self.sendAPIRequests)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FRIDAY"))
        self.label.setText(_translate("MainWindow", "FRIDAY"))
        self.label_2.setText(_translate("MainWindow", "A HACKABLE IOT ASSISTANT"))
        self.assistant_state_label.setText(_translate("MainWindow", "ACTIVE"))
        self.user_input_textedit.setHtml(_translate("MainWindow",
                                                    "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" "
                                                    "\"http://www.w3.org/TR/REC-html40/strict.dtd\">\n "
                                                    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style "
                                                    "type=\"text/css\">\n "
                                                    "p, li { white-space: pre-wrap; }\n"
                                                    "</style></head><body style=\" font-family:\'Geneva\'; "
                                                    "font-size:20pt; font-weight:400; font-style:normal;\">\n "
                                                    "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; "
                                                    "margin-left:0px; margin-right:0px; -qt-block-indent:0; "
                                                    "text-indent:0px;\"><span style=\" color:#ffffff;\">"
                                                    "CLICK THE MIC AND START SPEAKING</span></p></body></html>"))
        self.gpio_label.setText(_translate("MainWindow", "GPIO:"))
        self.radioButton.setText(_translate("MainWindow", "DIGITAL"))
        self.radioButton_2.setText(_translate("MainWindow", "ANALOG"))
        self.value_label.setText(_translate("MainWindow", "VALUE:"))
        self.label_4.setText(_translate("MainWindow", "  ©"))
        self.label_3.setText(_translate("MainWindow", " Ansh Patel · All Rights Reserved"))

    def updateUserVoiceInputArea(self, text):
        self.user_input_textedit.setHtml(("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" "
                                          "\"http://www.w3.org/TR/REC-html40/strict.dtd\">\n "
                                          "<html><head><meta name=\"qrichtext\" content=\"1\" /><style "
                                          "type=\"text/css\">\n "
                                          "p, li { white-space: pre-wrap; }\n"
                                          "</style></head><body style=\" font-family:\'Geneva\'; "
                                          "font-size:20pt; font-weight:400; font-style:normal;\">\n "
                                          "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; "
                                          "margin-left:0px; margin-right:0px; -qt-block-indent:0; "
                                          "text-indent:0px;\"><span style=\" color:#ffffff;\">"
                                          "" + text + "</span></p></body></html>"))

    def onVoiceAssistantClickEventHandler(self):
        try:
            run_friday()
        except sr.UnknownValueError:
            pass

    def sendAPIRequests(self):
        if self.channel_selection.currentText() != '':
            MODE = ''
            channel_id = self.channel_selection.currentText()[8:]
            print(channel_id)
            value = self.value_line_edit.text()
            print(value != '')
            if self.radioButton.isChecked():
                MODE = 'D'
            if self.radioButton_2.isChecked():
                MODE = 'A'
            if MODE != '' and self.channel_selection.currentText() != ' ' and value != '':
                if MODE == 'D':
                    digital_set_gpio(int(channel_id), int(value))
                if MODE == 'A':
                    analog_set_gpio(int(channel_id), int(value))

    def check_connectivity(self):
        self.db_state = False
        # Custom code below
        try:
            r = ""
            r = requests.get('https://www.google.com')
            if r != '':
                self.db_state = True
        except:
            pass
        if not self.db_state:
            self.raspbery_status_toast.setText('OFFLINE')
            self.raspbery_status_toast.setStyleSheet("font: 23pt \"Futura Bk BT\";\n"
                                                     "color: rgb(255, 0, 0)")
        else:
            self.raspbery_status_toast.setText('CONNECTED')
            self.raspbery_status_toast.setStyleSheet("font: 23pt \"Futura Bk BT\";\n"
                                                     "color: rgb(34, 255, 61)")


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)
    print(traceback)


if __name__ == "__main__":
    import sys

    sys.excepthook = except_hook
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
