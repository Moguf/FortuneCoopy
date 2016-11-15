#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import sys
from PyQt5 import QtWidgets as qw
from PyQt5 import QtGui as qg
from PyQt5.QtCore import pyqtSlot 

class FxViewer(object):
    def __init__(self):
        self.app = qw.QApplication(sys.argv)
        self.w = qw.QMainWindow()
        self._initWindow()
        self._initBotton()
        self._initMenu()        
        self.w.show()
        sys.exit(self.app.exec_())
        
    def _initWindow(self):
        self.w.resize(320, 240)
        self.w.setWindowTitle("Stury Forex.")

    def _initBotton(self):
        btn = qw.QPushButton('hello world.', self.w)
        btn.setToolTip('click to quit!')
        #btn.clicked.connect(exit)
        btn.resize(btn.sizeHint())
        btn.move(0, 0)

        @pyqtSlot()
        def on_click():
            print('clicked')
        @pyqtSlot()
        def on_press():
            print('pressed')
        @pyqtSlot()
        def on_release():
            print('released')

        btn.clicked.connect(on_click)        
        btn.pressed.connect(on_press)
        btn.released.connect(on_release)

    def _initMenu(self):
        mainMenu = self.w.menuBar()
        mainMenu.setNativeMenuBar(False)
        fileMenu = mainMenu.addMenu('&amp;File')
        exitButton = qw.QAction(qg.QIcon('exit24.png'), 'Exit', self.w)
        exitButton.setShortcut('Ctrl+Q')
        exitButton.setStatusTip('Exit application')
        exitButton.triggered.connect(self.w.close)
        fileMenu.addAction(exitButton)
        
    def run(self):
        pass


if __name__ == "__main__":
    v = FxViewer()
    v.run()
