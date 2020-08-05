# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_text_browser_popup.ui'
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

class Ui_TextBrowserPopUp(object):
    def setupUi(self, TextBrowserPopUp):
        TextBrowserPopUp.setObjectName(_fromUtf8("TextBrowserPopUp"))
        TextBrowserPopUp.setWindowModality(QtCore.Qt.NonModal)
        TextBrowserPopUp.resize(875, 870)
        self.textBrowser = QtGui.QTextBrowser(TextBrowserPopUp)
        self.textBrowser.setGeometry(QtCore.QRect(20, 10, 841, 841))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.textBrowser.setFont(font)
        self.textBrowser.setAutoFormatting(QtGui.QTextEdit.AutoAll)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))

        self.retranslateUi(TextBrowserPopUp)
        QtCore.QMetaObject.connectSlotsByName(TextBrowserPopUp)

    def retranslateUi(self, TextBrowserPopUp):
        TextBrowserPopUp.setWindowTitle(_translate("TextBrowserPopUp", "Dialog", None))

