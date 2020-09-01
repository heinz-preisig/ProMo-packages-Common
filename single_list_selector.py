# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'single_list_selector.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.NonModal)
        Dialog.resize(341, 182)
        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(10, 50, 321, 111))
        self.listWidget.setObjectName("listWidget")
        self.myframe = QtWidgets.QFrame(Dialog)
        self.myframe.setGeometry(QtCore.QRect(10, 0, 321, 51))
        self.myframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.myframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.myframe.setObjectName("myframe")
        self.layoutWidget = QtWidgets.QWidget(self.myframe)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 10, 311, 29))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushLeft = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushLeft.sizePolicy().hasHeightForWidth())
        self.pushLeft.setSizePolicy(sizePolicy)
        self.pushLeft.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.pushLeft.setAutoDefault(False)
        self.pushLeft.setObjectName("pushLeft")
        self.horizontalLayout.addWidget(self.pushLeft)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushRight = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushRight.sizePolicy().hasHeightForWidth())
        self.pushRight.setSizePolicy(sizePolicy)
        self.pushRight.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.pushRight.setAutoDefault(False)
        self.pushRight.setObjectName("pushRight")
        self.horizontalLayout.addWidget(self.pushRight)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.listWidget.setSortingEnabled(True)
        self.pushLeft.setToolTip(_translate("Dialog", "exit dialog"))
        self.pushLeft.setText(_translate("Dialog", "x"))
        self.pushRight.setToolTip(_translate("Dialog", "accept selection"))
        self.pushRight.setText(_translate("Dialog", "a"))
