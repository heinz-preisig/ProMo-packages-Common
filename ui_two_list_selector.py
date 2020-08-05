# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'two_list_selector.ui'
#
# Created: Mon Feb 27 21:41:37 2012
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_TwoListSelector(object):
    def setupUi(self, TwoListSelector):
        TwoListSelector.setObjectName(_fromUtf8("TwoListSelector"))
        TwoListSelector.resize(1058, 300)
        TwoListSelector.setWindowTitle(QtGui.QApplication.translate("TwoListSelector", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox = QtGui.QGroupBox(TwoListSelector)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 1021, 281))
        self.groupBox.setTitle(QtGui.QApplication.translate("TwoListSelector", "Select", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.layoutWidget = QtGui.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(910, 100, 87, 76))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.pushUp = QtGui.QPushButton(self.layoutWidget)
        self.pushUp.setText(QtGui.QApplication.translate("TwoListSelector", "up", None, QtGui.QApplication.UnicodeUTF8))
        self.pushUp.setObjectName(_fromUtf8("pushUp"))
        self.verticalLayout.addWidget(self.pushUp)
        self.pushDown = QtGui.QPushButton(self.layoutWidget)
        self.pushDown.setText(QtGui.QApplication.translate("TwoListSelector", "down", None, QtGui.QApplication.UnicodeUTF8))
        self.pushDown.setObjectName(_fromUtf8("pushDown"))
        self.verticalLayout.addWidget(self.pushDown)
        self.layoutWidget_2 = QtGui.QWidget(self.groupBox)
        self.layoutWidget_2.setGeometry(QtCore.QRect(430, 110, 87, 62))
        self.layoutWidget_2.setObjectName(_fromUtf8("layoutWidget_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.pushRight = QtGui.QPushButton(self.layoutWidget_2)
        self.pushRight.setText(QtGui.QApplication.translate("TwoListSelector", ">>>", None, QtGui.QApplication.UnicodeUTF8))
        self.pushRight.setObjectName(_fromUtf8("pushRight"))
        self.verticalLayout_2.addWidget(self.pushRight)
        self.pushLeft = QtGui.QPushButton(self.layoutWidget_2)
        self.pushLeft.setText(QtGui.QApplication.translate("TwoListSelector", "<<<", None, QtGui.QApplication.UnicodeUTF8))
        self.pushLeft.setObjectName(_fromUtf8("pushLeft"))
        self.verticalLayout_2.addWidget(self.pushLeft)
        self.listAvailable = QtGui.QListWidget(self.groupBox)
        self.listAvailable.setGeometry(QtCore.QRect(41, 51, 371, 192))
        self.listAvailable.setObjectName(_fromUtf8("listAvailable"))
        self.listSelected = QtGui.QListWidget(self.groupBox)
        self.listSelected.setGeometry(QtCore.QRect(521, 51, 381, 192))
        self.listSelected.setObjectName(_fromUtf8("listSelected"))
        self.pushOK = QtGui.QPushButton(self.groupBox)
        self.pushOK.setGeometry(QtCore.QRect(410, 250, 97, 27))
        self.pushOK.setText(QtGui.QApplication.translate("TwoListSelector", "OK", None, QtGui.QApplication.UnicodeUTF8))
        self.pushOK.setObjectName(_fromUtf8("pushOK"))

        self.retranslateUi(TwoListSelector)
        QtCore.QMetaObject.connectSlotsByName(TwoListSelector)

    def retranslateUi(self, TwoListSelector):
        pass

