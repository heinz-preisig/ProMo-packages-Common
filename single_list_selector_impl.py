#!/usr/local/bin/python3
# encoding: utf-8

"""
===============================================================================
 graph object resources
===============================================================================

The graph objects are used in the ModelComposer and defined based on a basic structure stored in
gaph_objects_ini.json
and edited in GraphComponentenEditor
"""

__project__ = "ProcessModeller  Suite"
__author__ = "PREISIG, Heinz A"
__copyright__ = "Copyright 2015, PREISIG, Heinz A"
__since__ = "2013. 01. 09"
__license__ = "GPL planned -- until further notice for Bio4Fuel & MarketPlace internal use only"
__version__ = "6.00"
__email__ = "heinz.preisig@chemeng.ntnu.no"
__status__ = "beta"

import os
from copy import copy

from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets

from Common.resource_initialisation import DIRECTORIES
from Common.single_list_selector import Ui_Dialog

# Note: entanglement -- Common.common_resources -- roundButton cannot be loaded here.
BUTTON_ICON_SIZE = QtCore.QSize(30, 30)
BUTTON_ICON_STYLE_ROUND = 'background-color: white; '
BUTTON_ICON_STYLE_ROUND += 'border-style: outset; '
BUTTON_ICON_STYLE_ROUND += 'border-width: 2px; '
BUTTON_ICON_STYLE_ROUND += 'border-radius: 14px; '
BUTTON_ICON_STYLE_ROUND += 'border-color: beige;    '


# BUTTON_ICON_STYLE_ROUND += 'font: bold 14px;   '
# BUTTON_ICON_STYLE_ROUND += 'padding: 6px;'

class SingleListSelector(QtWidgets.QDialog):
  '''
  selects an item from a list
  '''

  newSelection = QtCore.pyqtSignal(str)

  def __init__(self, thelist, selected=None, myparent=None, accept_icon="accept.png", reject_icon="reject.png"):
    '''
    Constructor
    '''
    self.thelist = thelist
    self.selection = None
    QtWidgets.QDialog.__init__(self, parent=myparent)
    self.ui = Ui_Dialog()
    self.ui.setupUi(self)

    self.ui.listWidget.addItems(thelist)
    accept_file = os.path.join(DIRECTORIES["icon_location"], accept_icon)  # 'accept.png')
    reject_file = os.path.join(DIRECTORIES["icon_location"], reject_icon)  # 'reject.png')
    accept_icon = QtGui.QIcon(QtGui.QPixmap(accept_file))
    reject_icon = QtGui.QIcon(QtGui.QPixmap(reject_file))

    self.ui.pushAccept.setStyleSheet(BUTTON_ICON_STYLE_ROUND)
    self.ui.pushAccept.setIconSize(BUTTON_ICON_SIZE)
    self.ui.pushAccept.setIcon(accept_icon)
    self.ui.pushAccept.setText('')

    self.ui.pushCancle.setStyleSheet(BUTTON_ICON_STYLE_ROUND)
    self.ui.pushCancle.setIconSize(BUTTON_ICON_SIZE)
    self.ui.pushCancle.setIcon(reject_icon)
    self.ui.pushCancle.setText('')
    self.selection = None

    max_width = 0
    height = 20
    for i in thelist:
      label = QtWidgets.QLabel(i)
      width = label.fontMetrics().boundingRect(label.text()).width()
      height = height + label.fontMetrics().boundingRect(label.text()).height()
      if width > max_width: max_width = width
    self.__resizeMe(height, max_width + 20)

    self.__move2row(selected)
    self.hide()

  def __move2row(self, selected):
    if (selected != None) and (selected in self.thelist):
      row = self.thelist.index(selected)
      self.ui.listWidget.setCurrentRow(row)
      self.selection = copy(selected)
    else:
      row = -1
      self.ui.pushAccept.hide()
    self.ui.listWidget.setCurrentRow(row)

  def Show(self, entry):
    self.__move2row(entry)
    QtWidgets.QDialog.show(self)

  def hide(self):
    QtWidgets.QWidget.hide(self)

  def getSelection(self):
    return self.selection

  def __resizeMe(self, height, width):
    tab_size = QtCore.QSize(width, height)
    self.ui.listWidget.resize(tab_size)
    size_b = self.ui.myframe.size()
    b_width = size_b.width()
    b_height = size_b.height()
    if b_width < width:
      size_b.setWidth(width)
      self.ui.myframe.resize(size_b)  # adjust box
    elif width < b_width:
      width = b_width
      tab_size = QtCore.QSize(width, height)
      self.ui.listWidget.resize(tab_size)
    s = QtCore.QSize(width + 20, b_height + height + 20)
    # s.setHeight(size_b.height() + height +10)
    # s.setWidth(width+20)
    self.resize(s)

  def on_listWidget_itemClicked(self, v):
    # print('item clicked')
    currentItem = self.ui.listWidget.currentItem()
    self.selection = str(currentItem.text())
    self.ui.pushAccept.show()

  def on_listWidget_itemDoubleClicked(self, v):
    self.on_listWidget_itemClicked(v)
    self.on_pushAccept_pressed()

  def on_pushAccept_pressed(self):
    self.newSelection.emit(str(self.selection))
    self.hide()

  def on_pushCancle_pressed(self):
    self.selection = None
    self.hide()

  def accept(self):
    # print('accept', self.selection)
    self.hide()

  def reject(self):
    # print('reject', self.selection)
    self.hide()
