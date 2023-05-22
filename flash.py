# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tablero.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets 
import time


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 442)
        
        screen_geometry = QtWidgets.QDesktopWidget().screenGeometry()
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ka = QtWidgets.QLabel(self.centralwidget)
        self.ka.setGeometry(screen_geometry)
        self.ka.setText("")
        self.ka.setPixmap(QtGui.QPixmap("blanco.png"))
        self.ka.setObjectName("ka")
        self.bo = QtWidgets.QLabel(self.centralwidget)
        self.bo.setGeometry(screen_geometry)
        self.bo.setText("")
        self.bo.setPixmap(QtGui.QPixmap("negro.png"))
        self.bo.setObjectName("bo")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

    def enabled(self):
        current_state = self.bo.isVisible()
        self.bo.setVisible(not current_state)
        print("paso por enabled", current_state)
        '''
        time.sleep(0.1)
        self.ka.setVisible(current_state)
        print("paso por enabled", current_state)
        '''
        
    def start(self):
        self.timerA = QtCore.QTimer()
        self.timerA.timeout.connect(self.enabled)
        self.timerA.start(1000)
        print("entro a start")



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.start()
    sys.exit(app.exec_())