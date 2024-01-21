from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(600, 448)
        mainWindow.setMinimumSize(QtCore.QSize(600, 448))
        mainWindow.setMaximumSize(QtCore.QSize(600, 448))
        mainWindow.setMouseTracking(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:\\Users\Home\\Desktop\\Personal voice assistant\\gif\\logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mainWindow.setWindowIcon(icon)
        mainWindow.setAutoFillBackground(True)
        mainWindow.setIconSize(QtCore.QSize(30, 30))
        mainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(600, 449))
        self.centralwidget.setMaximumSize(QtCore.QSize(600, 449))
        self.centralwidget.setObjectName("centralwidget")
        self.mic_button = QtWidgets.QPushButton(self.centralwidget)
        self.mic_button.setGeometry(QtCore.QRect(30, 360, 60, 60))
        self.mic_button.setMinimumSize(QtCore.QSize(60, 60))
        self.mic_button.setMaximumSize(QtCore.QSize(60, 60))
        self.mic_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.mic_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:\\Users\Home\\Desktop\\Personal voice assistant\\gif\\mic.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mic_button.setIcon(icon1)
        self.mic_button.setIconSize(QtCore.QSize(60, 60))
        self.mic_button.setObjectName("mic_button")
        self.wave_label = QtWidgets.QLabel(self.centralwidget)
        self.wave_label.setGeometry(QtCore.QRect(90, 370, 375, 60))
        self.wave_label.setMinimumSize(QtCore.QSize(375, 60))
        self.wave_label.setMaximumSize(QtCore.QSize(375, 60))
        self.wave_label.setText("")
        self.wave_label.setPixmap(QtGui.QPixmap("C:\\Users\Home\\Desktop\\Personal voice assistant\\gif\\wave.g if"))
        self.wave_label.setScaledContents(True)
        self.wave_label.setObjectName("wave_label")
        self.ball_label = QtWidgets.QLabel(self.centralwidget)
        self.ball_label.setGeometry(QtCore.QRect(-100, -160, 800, 671))
        self.ball_label.setMinimumSize(QtCore.QSize(800, 671))
        self.ball_label.setMaximumSize(QtCore.QSize(800, 671))
        self.ball_label.setText("")
        self.ball_label.setPixmap(QtGui.QPixmap("C:\\Users\Home\\Desktop\\Personal voice assistant\\gif\\ball.gif"))
        self.ball_label.setScaledContents(True)
        self.ball_label.setObjectName("ball_label")
        self.quit_button = QtWidgets.QPushButton(self.centralwidget)
        self.quit_button.setGeometry(QtCore.QRect(490, 400, 93, 28))
        self.quit_button.setMinimumSize(QtCore.QSize(93, 28))
        self.quit_button.setMaximumSize(QtCore.QSize(93, 28))
        self.quit_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.quit_button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("C:\\Users\Home\\Desktop\\Personal voice assistant\\gif\\Quit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.quit_button.setIcon(icon2)
        self.quit_button.setIconSize(QtCore.QSize(93, 60))
        self.quit_button.setObjectName("quit_button")
        self.start_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_button.setGeometry(QtCore.QRect(490, 360, 93, 28))
        self.start_button.setMinimumSize(QtCore.QSize(93, 28))
        self.start_button.setMaximumSize(QtCore.QSize(93, 28))
        self.start_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.start_button.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("C:\\Users\Home\\Desktop\\Personal voice assistant\\gif\\Start.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.start_button.setIcon(icon3)
        self.start_button.setIconSize(QtCore.QSize(93, 60))
        self.start_button.setObjectName("start_button")
        self.ball_label.raise_()
        self.mic_button.raise_()
        self.quit_button.raise_()
        self.wave_label.raise_()
        self.start_button.raise_()
        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)
        self.actionChange_Name = QtWidgets.QAction(mainWindow)
        self.actionChange_Name.setObjectName("actionChange_Name")
        self.actionDate = QtWidgets.QAction(mainWindow)
        self.actionDate.setObjectName("actionDate")
        self.actionTime = QtWidgets.QAction(mainWindow)
        self.actionTime.setObjectName("actionTime")

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "UKNOW"))
        self.actionChange_Name.setText(_translate("mainWindow", "Change Name"))
        self.actionDate.setText(_translate("mainWindow", "Date"))
        self.actionTime.setText(_translate("mainWindow", "Time"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())