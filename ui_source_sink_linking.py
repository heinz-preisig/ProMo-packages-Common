# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_source_sink_linking.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SourceSinkLinking(object):
    def setupUi(self, SourceSinkLinking):
        SourceSinkLinking.setObjectName("SourceSinkLinking")
        SourceSinkLinking.resize(1244, 331)
        self.gridLayoutWidget = QtWidgets.QWidget(SourceSinkLinking)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(60, 30, 1131, 251))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.listSink = QtWidgets.QListWidget(self.gridLayoutWidget)
        self.listSink.setObjectName("listSink")
        self.gridLayout.addWidget(self.listSink, 1, 2, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushAccept = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushAccept.sizePolicy().hasHeightForWidth())
        self.pushAccept.setSizePolicy(sizePolicy)
        self.pushAccept.setMinimumSize(QtCore.QSize(52, 52))
        self.pushAccept.setObjectName("pushAccept")
        self.verticalLayout.addWidget(self.pushAccept)
        self.pushReset = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushReset.sizePolicy().hasHeightForWidth())
        self.pushReset.setSizePolicy(sizePolicy)
        self.pushReset.setMinimumSize(QtCore.QSize(52, 52))
        self.pushReset.setObjectName("pushReset")
        self.verticalLayout.addWidget(self.pushReset)
        self.pushReject = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushReject.sizePolicy().hasHeightForWidth())
        self.pushReject.setSizePolicy(sizePolicy)
        self.pushReject.setMinimumSize(QtCore.QSize(52, 52))
        self.pushReject.setObjectName("pushReject")
        self.verticalLayout.addWidget(self.pushReject)
        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)
        self.listSource = QtWidgets.QListWidget(self.gridLayoutWidget)
        self.listSource.setObjectName("listSource")
        self.gridLayout.addWidget(self.listSource, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)

        self.retranslateUi(SourceSinkLinking)
        QtCore.QMetaObject.connectSlotsByName(SourceSinkLinking)

    def retranslateUi(self, SourceSinkLinking):
        _translate = QtCore.QCoreApplication.translate
        SourceSinkLinking.setWindowTitle(_translate("SourceSinkLinking", "Form"))
        self.pushAccept.setText(_translate("SourceSinkLinking", "accept"))
        self.pushReset.setText(_translate("SourceSinkLinking", "reset"))
        self.pushReject.setText(_translate("SourceSinkLinking", "reject"))
        self.label.setText(_translate("SourceSinkLinking", "source"))
        self.label_2.setText(_translate("SourceSinkLinking", "sink"))
