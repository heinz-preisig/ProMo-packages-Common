# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'single_list_selector.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore
from PyQt5 import QtWidgets


class Ui_Dialog(object):
  def setupUi(self, Dialog):
    Dialog.setObjectName("Dialog")
    Dialog.setWindowModality(QtCore.Qt.NonModal)
    Dialog.resize(411, 182)
    self.listWidget = QtWidgets.QListWidget(Dialog)
    self.listWidget.setGeometry(QtCore.QRect(10, 50, 201, 111))
    self.listWidget.setObjectName("listWidget")
    self.myframe = QtWidgets.QFrame(Dialog)
    self.myframe.setGeometry(QtCore.QRect(10, 0, 201, 51))
    self.myframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
    self.myframe.setFrameShadow(QtWidgets.QFrame.Raised)
    self.myframe.setObjectName("myframe")
    self.widget = QtWidgets.QWidget(self.myframe)
    self.widget.setGeometry(QtCore.QRect(0, 10, 201, 29))
    self.widget.setObjectName("widget")
    self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
    self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
    self.horizontalLayout.setObjectName("horizontalLayout")
    self.pushCancle = QtWidgets.QPushButton(self.widget)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.pushCancle.sizePolicy().hasHeightForWidth())
    self.pushCancle.setSizePolicy(sizePolicy)
    self.pushCancle.setFocusPolicy(QtCore.Qt.ClickFocus)
    self.pushCancle.setAutoDefault(False)
    self.pushCancle.setObjectName("pushCancle")
    self.horizontalLayout.addWidget(self.pushCancle)
    spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
    self.horizontalLayout.addItem(spacerItem)
    self.pushAccept = QtWidgets.QPushButton(self.widget)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.pushAccept.sizePolicy().hasHeightForWidth())
    self.pushAccept.setSizePolicy(sizePolicy)
    self.pushAccept.setFocusPolicy(QtCore.Qt.ClickFocus)
    self.pushAccept.setAutoDefault(False)
    self.pushAccept.setObjectName("pushAccept")
    self.horizontalLayout.addWidget(self.pushAccept)

    self.retranslateUi(Dialog)
    QtCore.QMetaObject.connectSlotsByName(Dialog)

  def retranslateUi(self, Dialog):
    _translate = QtCore.QCoreApplication.translate
    Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
    self.listWidget.setSortingEnabled(True)
    self.pushCancle.setToolTip(_translate("Dialog", "exit dialog"))
    self.pushCancle.setText(_translate("Dialog", "x"))
    self.pushAccept.setToolTip(_translate("Dialog", "accept selection"))
    self.pushAccept.setText(_translate("Dialog", "a"))
