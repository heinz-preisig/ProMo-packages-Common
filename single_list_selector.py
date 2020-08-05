# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'single_list_selector.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.setWindowModality(QtCore.Qt.NonModal)
        Dialog.resize(411, 182)
        self.listWidget = QtGui.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(10, 50, 201, 111))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.myframe = QtGui.QFrame(Dialog)
        self.myframe.setGeometry(QtCore.QRect(10, 0, 201, 51))
        self.myframe.setFrameShape(QtGui.QFrame.StyledPanel)
        self.myframe.setFrameShadow(QtGui.QFrame.Raised)
        self.myframe.setObjectName(_fromUtf8("myframe"))
        self.widget = QtGui.QWidget(self.myframe)
        self.widget.setGeometry(QtCore.QRect(0, 10, 201, 29))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushCancle = QtGui.QPushButton(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushCancle.sizePolicy().hasHeightForWidth())
        self.pushCancle.setSizePolicy(sizePolicy)
        self.pushCancle.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.pushCancle.setAutoDefault(False)
        self.pushCancle.setObjectName(_fromUtf8("pushCancle"))
        self.horizontalLayout.addWidget(self.pushCancle)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushAccept = QtGui.QPushButton(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushAccept.sizePolicy().hasHeightForWidth())
        self.pushAccept.setSizePolicy(sizePolicy)
        self.pushAccept.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.pushAccept.setAutoDefault(False)
        self.pushAccept.setObjectName(_fromUtf8("pushAccept"))
        self.horizontalLayout.addWidget(self.pushAccept)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.listWidget.setSortingEnabled(True)
        self.pushCancle.setToolTip(_translate("Dialog", "exit dialog", None))
        self.pushCancle.setText(_translate("Dialog", "x", None))
        self.pushAccept.setToolTip(_translate("Dialog", "accept selection", None))
        self.pushAccept.setText(_translate("Dialog", "a", None))

