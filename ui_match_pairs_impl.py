#!/usr/local/bin/python3
# encoding: utf-8

"""
===============================================================================
 GUI resource -- selects from a list into a list
===============================================================================


"""

__project__ = "ProcessModeller  Suite"
__author__ = "PREISIG, Heinz A"
__copyright__ = "Copyright 2015, PREISIG, Heinz A"
__since__ = "2021. 02. 24"
__license__ = "GPL planned -- until further notice for Bio4Fuel & MarketPlace internal use only"
__version__ = "8.00"
__email__ = "heinz.preisig@chemeng.ntnu.no"
__status__ = "beta"

from PyQt5 import QtCore
from PyQt5 import QtGui, QtWidgets

from Common.ui_match_pairs import Ui_Dialog
from Common.resources_icons import roundButton

PAIRDELIMITER = " & "

class UI_MatchPairs(QtWidgets.QDialog):
  '''
  selects from a list generating a new list, which can also re-arranged by moving elements up or down.
  '''
  selection = QtCore.pyqtSignal(list)

  def __init__(self, left_items, right_items, connector):
    '''
    plain constructor
    '''

    super().__init__()
    self.ui = Ui_Dialog()
    self.ui.setupUi(self)
    self.show()
    try:
      roundButton(self.ui.pushButtonExit, "exit", "exit" )
    except:
      pass
    self.selected_left=False
    self.selected_right=False
    self.populateLists(left_items, right_items)
    self.selection.connect(connector)


  def close(self):
    selected_list = self.getSelected()
    self.selection.emit(selected_list)
    QtCore.QObject.close(self)
    del self

  def populateLists(self, left_items, right_items):
    self.ui.listWidgetLeft.clear()
    self.ui.listWidgetRight.clear()
    for i in left_items:
        self.ui.listWidgetLeft.addItem(i)
    for i in right_items:
        self.ui.listWidgetRight.addItem(i)

  def getSelected(self):
    selected = []
    count = self.ui.listWidgetPairs.count()
    for i in range(0, count):
      item = self.ui.listWidgetPairs.item(i)
      s = str(item.text())
      s_left,s_right = s.split(PAIRDELIMITER)
      selected.append((s_left,s_right))
    return selected

  def on_listWidgetRight_itemClicked(self):
    # print("debugging -- right clicked")
    self.selected_left = True
    self.__makePair()

  def on_listWidgetLeft_itemClicked(self):
    # print("debugging -- left clicked")
    self.selected_right = True
    self.__makePair()

  def __makePair(self):
    if self.selected_left:
      if self.selected_right:
        row_left = self.ui.listWidgetLeft.currentRow()
        item_left = self.ui.listWidgetLeft.takeItem(row_left)
        row_right = self.ui.listWidgetRight.currentRow()
        item_right = self.ui.listWidgetRight.takeItem(row_right)
        text_left = item_left.text()
        text_right = item_right.text()
        text_pair = "%s%s%s"%(text_left,PAIRDELIMITER,text_right)
        self.ui.listWidgetPairs.addItem(text_pair)
        self.selected_left = False
        self.selected_right = False
        self.ui.listWidgetRight.clearSelection()
        self.ui.listWidgetLeft.clearSelection()

  def on_listWidgetPairs_itemClicked(self):
    row_pair = self.ui.listWidgetPairs.currentRow()
    item_pair = self.ui.listWidgetPairs.takeItem(row_pair)
    text_pair = item_pair.text()
    text_left, text_right = text_pair.split(PAIRDELIMITER)
    self.ui.listWidgetLeft.addItem(text_left.strip())
    self.ui.listWidgetRight.addItem(text_right.strip())
    self.ui.listWidgetLeft.sortItems()
    self.ui.listWidgetRight.sortItems()


  def on_pushButtonExit_pressed(self):
    self.accept()
    selected_list = self.getSelected()
    self.selection.emit(selected_list)
    return self.getSelected()

def gottenList(selection):
  print(selection)

if __name__ == '__main__':
  import sys
  right = ['a','b','c','d']
  left = ['1','2','3']

  app = QtWidgets.QApplication([])

  ui = UI_MatchPairs(left,right, gottenList)
  ui.show()

  my_list = sys.exit(app.exec_())
  print(my_list)