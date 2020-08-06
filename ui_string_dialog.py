# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_string_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore
from PyQt5 import QtWidgets


class Ui_Dialog(object):
  def setupUi(self, Dialog):
    Dialog.setObjectName("Dialog")
    Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
    Dialog.resize(483, 86)
    Dialog.setModal(True)
    self.lineEdit = QtWidgets.QLineEdit(Dialog)
    self.lineEdit.setGeometry(QtCore.QRect(20, 10, 461, 27))
    self.lineEdit.setObjectName("lineEdit")
    self.pushAccept = QtWidgets.QPushButton(Dialog)
    self.pushAccept.setGeometry(QtCore.QRect(20, 40, 99, 27))
    self.pushAccept.setObjectName("pushAccept")
    self.pushReject = QtWidgets.QPushButton(Dialog)
    self.pushReject.setGeometry(QtCore.QRect(130, 40, 99, 27))
    self.pushReject.setObjectName("pushReject")

    self.retranslateUi(Dialog)
    QtCore.QMetaObject.connectSlotsByName(Dialog)

  def retranslateUi(self, Dialog):
    _translate = QtCore.QCoreApplication.translate
    Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
    self.pushAccept.setText(_translate("Dialog", "accept"))
    self.pushReject.setText(_translate("Dialog", "reject"))
