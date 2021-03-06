# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FrontEnd.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QComboBox
from pygame import mixer

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.counter = 0
        self.x = 0
        self.o = 0
        self.tie = 0
        mixer.init()        
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(424, 629)
        MainWindow.setMinimumSize(QtCore.QSize(424, 629))
        MainWindow.setMaximumSize(QtCore.QSize(424, 629))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(130, 90, 20, 371))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.line.setFont(font)
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(3)
        self.line.setMidLineWidth(0)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setObjectName("line")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(270, 90, 20, 371))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.line_3.setFont(font)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_3.setLineWidth(3)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setObjectName("line_3")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(10, 200, 401, 20))
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setLineWidth(3)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setObjectName("line_2")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(10, 330, 401, 20))
        self.line_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_4.setLineWidth(3)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setObjectName("line_4")
        self.button0 = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.eventClicker(self.button0))
        self.button0.setGeometry(QtCore.QRect(10, 90, 121, 111))
        font = QtGui.QFont()
        font.setFamily("Press Start 2P")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.button0.setFont(font)
        self.button0.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.button0.setToolTipDuration(-1)
        self.button0.setStyleSheet("QPushButton {\n"
"background-color:rgb(242, 242, 242);\n"
"}\n"
"\n"
"")
        self.button0.setText("")
        self.button0.setShortcut("")
        self.button0.setAutoDefault(False)
        self.button0.setDefault(False)
        self.button0.setFlat(True)
        self.button0.setObjectName("button0")
        self.button1 = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.eventClicker(self.button1))
        self.button1.setGeometry(QtCore.QRect(150, 90, 121, 111))
        font = QtGui.QFont()
        font.setFamily("Press Start 2P")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.button1.setFont(font)
        self.button1.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.button1.setToolTipDuration(-1)
        self.button1.setStyleSheet("\n"
"background-color:rgb(242, 242, 242);\n"
"\n"
"\n"
"")
        self.button1.setText("")
        self.button1.setShortcut("")
        self.button1.setAutoDefault(False)
        self.button1.setDefault(False)
        self.button1.setFlat(True)
        self.button1.setObjectName("button1")
        self.button2 = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.eventClicker(self.button2))
        self.button2.setGeometry(QtCore.QRect(290, 90, 121, 111))
        font = QtGui.QFont()
        font.setFamily("Press Start 2P")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.button2.setFont(font)
        self.button2.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.button2.setToolTipDuration(-1)
        self.button2.setStyleSheet("QPushButton {\n"
"background-color:rgb(242, 242, 242);\n"
"}\n"
"\n"
"")
        self.button2.setText("")
        self.button2.setShortcut("")
        self.button2.setAutoDefault(False)
        self.button2.setDefault(False)
        self.button2.setFlat(True)
        self.button2.setObjectName("button2")
        self.button3 = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.eventClicker(self.button3))
        self.button3.setGeometry(QtCore.QRect(10, 220, 121, 111))
        font = QtGui.QFont()
        font.setFamily("Press Start 2P")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.button3.setFont(font)
        self.button3.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.button3.setToolTipDuration(-1)
        self.button3.setStyleSheet("\n"
"background-color:rgb(242, 242, 242);\n"
"\n"
"\n"
"")
        self.button3.setText("")
        self.button3.setShortcut("")
        self.button3.setAutoDefault(False)
        self.button3.setDefault(False)
        self.button3.setFlat(True)
        self.button3.setObjectName("button3")
        self.button4 = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.eventClicker(self.button4))
        self.button4.setGeometry(QtCore.QRect(150, 220, 121, 111))
        font = QtGui.QFont()
        font.setFamily("Press Start 2P")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.button4.setFont(font)
        self.button4.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.button4.setToolTipDuration(-1)
        self.button4.setStyleSheet("QPushButton {\n"
"background-color:rgb(242, 242, 242);\n"
"}\n"
"\n"
"")
        self.button4.setText("")
        self.button4.setShortcut("")
        self.button4.setAutoDefault(False)
        self.button4.setDefault(False)
        self.button4.setFlat(True)
        self.button4.setObjectName("button4")
        self.button5 = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.eventClicker(self.button5))
        self.button5.setGeometry(QtCore.QRect(290, 220, 121, 111))
        font = QtGui.QFont()
        font.setFamily("Press Start 2P")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.button5.setFont(font)
        self.button5.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.button5.setToolTipDuration(-1)
        self.button5.setStyleSheet("QPushButton {\n"
"background-color:rgb(242, 242, 242);\n"
"}\n"
"\n"
"")
        self.button5.setText("")
        self.button5.setShortcut("")
        self.button5.setAutoDefault(False)
        self.button5.setDefault(False)
        self.button5.setFlat(True)
        self.button5.setObjectName("button5")
        self.button8 = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.eventClicker(self.button8))
        self.button8.setGeometry(QtCore.QRect(290, 350, 121, 111))
        font = QtGui.QFont()
        font.setFamily("Press Start 2P")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.button8.setFont(font)
        self.button8.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.button8.setToolTipDuration(-1)
        self.button8.setStyleSheet("QPushButton {\n"
"background-color:rgb(242, 242, 242);\n"
"}\n"
"\n"
"")
        self.button8.setText("")
        self.button8.setShortcut("")
        self.button8.setAutoDefault(False)
        self.button8.setDefault(False)
        self.button8.setFlat(True)
        self.button8.setObjectName("button8")
        self.button7 = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.eventClicker(self.button7))
        self.button7.setGeometry(QtCore.QRect(150, 350, 121, 111))
        font = QtGui.QFont()
        font.setFamily("Press Start 2P")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.button7.setFont(font)
        self.button7.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.button7.setToolTipDuration(-1)
        self.button7.setStyleSheet("QPushButton {\n"
"background-color:rgb(242, 242, 242);\n"
"}\n"
"\n"
"")
        self.button7.setText("")
        self.button7.setShortcut("")
        self.button7.setAutoDefault(False)
        self.button7.setDefault(False)
        self.button7.setFlat(True)
        self.button7.setObjectName("button7")
        self.button6 = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.eventClicker(self.button6))
        self.button6.setGeometry(QtCore.QRect(10, 350, 121, 111))
        font = QtGui.QFont()
        font.setFamily("Press Start 2P")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.button6.setFont(font)
        self.button6.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.button6.setToolTipDuration(-1)
        self.button6.setStyleSheet("\n"
"background-color:rgb(242, 242, 242);\n"
"")
        self.button6.setText("")
        self.button6.setShortcut("")
        self.button6.setAutoDefault(False)
        self.button6.setDefault(False)
        self.button6.setFlat(True)
        self.button6.setObjectName("button6")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 20, 421, 61))
        font = QtGui.QFont()
        font.setFamily("Press Start 2P")
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.X_score = QtWidgets.QLabel(self.centralwidget)
        self.X_score.setGeometry(QtCore.QRect(20, 520, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Press Start 2P")
        font.setPointSize(10)
        self.X_score.setFont(font)
        self.X_score.setObjectName("X_score")
        font = QtGui.QFont()
        font.setFamily("Press Start 2P")
        font.setPointSize(10)
        self.O_score = QtWidgets.QLabel(self.centralwidget)
        self.O_score.setGeometry(QtCore.QRect(20, 550, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Press Start 2P")
        font.setPointSize(10)
        self.O_score.setFont(font)
        self.O_score.setObjectName("O_score")
        self.Tie_score = QtWidgets.QLabel(self.centralwidget)
        self.Tie_score.setGeometry(QtCore.QRect(20, 580, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Press Start 2P")
        font.setPointSize(9)
        self.Tie_score.setFont(font)
        self.Tie_score.setObjectName("Tie_score")
        #
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(240, 590, 181, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:rgb(145, 145, 142);")
        self.label_2.setObjectName("label_2")
        self.restartButton = QtWidgets.QPushButton(self.centralwidget,clicked = self.restart)
        self.restartButton.setGeometry(QtCore.QRect(290, 510, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.restartButton.setFont(font)
        self.restartButton.setToolTipDuration(-1)
        self.restartButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        #
        self.restartButton.setObjectName("restartButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 424, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Noughts and Crosses", "Noughts and Crosses"))
        MainWindow.setWindowIcon(QtGui.QIcon('Icon/Screenshot 2022-07-15 201711.ico'))
        self.label.setText(_translate("MainWindow", "Tic Tac Toe"))
        self.X_score.setText(_translate("MainWindow", "X:"))
        self.O_score.setText(_translate("MainWindow", "O:"))
        self.Tie_score.setText(_translate("MainWindow", "Tie:"))
        #
        self.label_2.setText(_translate("MainWindow", "Made with curiosity by @Loftyyyy"))
        self.restartButton.setText(_translate("MainWindow", "RESTART"))
        self.restartButton.setIcon(QtGui.QIcon('Icon/reload.png'))
#records button clicks    
    def eventClicker(self,b):
        if self.counter % 2 == 0:
                b.setText('x')
                b.setEnabled(False)
                mixer.music.load('SFX/X_SFX.ogg')                
                mixer.music.set_volume(0.2)
                mixer.music.play()
        else:
                b.setText('o')
                b.setEnabled(False)
                mixer.music.load('SFX/O_SFX.ogg')
                mixer.music.set_volume(0.2)
                mixer.music.play()
        self.counter += 1
        self.MainLogic()

#restarts the board 
    def reset(self):
        buttons = [self.button0, self.button1, self.button2, self.button3, self.button4, self.button5, self.button6, self.button7, self.button8]

        #clears the board
        for clearing in buttons:
                clearing.setText('')
        
        #enables keypress again
        for keypress in buttons:
                keypress.setEnabled(True)
        
        #resets counter to 0; always starts with x
        self.counter = 0

    def restart(self):
        buttons = [self.button0, self.button1, self.button2, self.button3, self.button4, self.button5, self.button6, self.button7, self.button8]

        #clears the board
        for clearing in buttons:
                clearing.setText('')
        
        #enables keypress again
        for keypress in buttons:
                keypress.setEnabled(True)
        
        #resets counter to 0; always starts with x
        self.counter = 0
        self.tie_count = 0
        self.X_score.setText('X:')
        self.O_score.setText('O:')
        self.Tie_score.setText('Tie:')
        self.label.setText('Tic Tac Toe')
        mixer.music.load('SFX/RESTART_SFX.ogg')
        mixer.music.set_volume(0.09)
        mixer.music.play()
        
        
        
    def MainLogic(self):
        #Horizontal Winning Combinations 
                #X and O Horizontal Combinations
        if self.button0.text() != '' and self.button0.text() == self.button1.text() == self.button2.text():
                self.winCheck(self.button0)
                
        if self.button3.text() != '' and self.button3.text() == self.button4.text() == self.button5.text():
                self.winCheck(self.button3)
                
        if self.button6.text() != '' and self.button6.text() == self.button7.text() == self.button8.text():
                self.winCheck(self.button6)
                
                #X and O Vertical Combinations
        if self.button0.text() != '' and self.button0.text() == self.button3.text() == self.button6.text():
                self.winCheck(self.button0)
                
        if self.button1.text() != '' and self.button1.text() == self.button4.text() == self.button7.text():
                self.winCheck(self.button1)
                
        if self.button2.text() != '' and self.button2.text() == self.button5.text() == self.button8.text():
                self.winCheck(self.button2)
        
                #X and O Slope/Incline Combinations
        if self.button0.text() != '' and self.button0.text() == self.button4.text() == self.button8.text():
                self.winCheck(self.button0)
        if self.button2.text() != '' and self.button2.text() == self.button4.text() == self.button6.text():
                self.winCheck(self.button2)
                
                #checks if tie
        if self.button0.text() != '' and self.button1.text() != '' and  self.button2.text() != '' and  self.button3.text() != '' and  self.button4.text() != '' and self.button5.text() != '' and  self.button6.text() != '' and self.button7.text() != '' and self.button8.text() != '':
                mixer.music.load('SFX/tie_SFX.ogg')
                mixer.music.set_volume(0.2)
                mixer.music.play()
                self.tie += 1
                self.Tie_score.setText(f'Tie:{self.tie}')
                self.label.setText('Tie!')
                self.reset()
    def winCheck(self,btn):
            self.label.setText(f'{btn.text().upper()} wins!')

            #updates scores
            if btn.text() == 'x':
                    mixer.music.load('SFX/XWIN_SFX.ogg')
                    mixer.music.set_volume(0.2)
                    mixer.music.play()
                    self.x += 1
                    self.X_score.setText(f"X:{self.x}")
            if btn.text() == 'o':
                    mixer.music.load('SFX/OWIN_SFX.ogg')
                    mixer.music.set_volume(0.2)
                    mixer.music.play()
                    self.o += 1
                    self.O_score.setText(f"O:{self.o}")
            self.reset()
            

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
