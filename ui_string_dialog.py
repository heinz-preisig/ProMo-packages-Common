# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/heinz/1_Gits/ProcessModeller/ProcessModeller_v3_9/packages/Common/ui_string_dialog.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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
        Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog.resize(483, 86)
        Dialog.setModal(True)
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(20, 10, 461, 27))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.pushAccept = QtGui.QPushButton(Dialog)
        self.pushAccept.setGeometry(QtCore.QRect(20, 40, 99, 27))
        self.pushAccept.setObjectName(_fromUtf8("pushAccept"))
        self.pushReject = QtGui.QPushButton(Dialog)
        self.pushReject.setGeometry(QtCore.QRect(130, 40, 99, 27))
        self.pushReject.setObjectName(_fromUtf8("pushReject"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.pushAccept.setText(_translate("Dialog", "accept", None))
        self.pushReject.setText(_translate("Dialog", "reject", None))

