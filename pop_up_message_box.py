#!/usr/local/bin/python3
# encoding: utf-8

"""
===============================================================================
 Ontology design facility
===============================================================================

This program is part of the ProcessModelling suite

"""

__project__ = "ProcessModeller  Suite"
__author__ = "PREISIG, Heinz A"
__copyright__ = "Copyright 2015, PREISIG, Heinz A"
__since__ = "11.11.2019"
__license__ = "GPL planned -- until further notice for Bio4Fuel & MarketPlace internal use only"
__version__ = "5.04"
__email__ = "heinz.preisig@chemeng.ntnu.no"
__status__ = "beta"

import sys

from PyQt4 import QtGui

BUTTONS = {
      "OK"             : QtGui.QMessageBox.Ok,
      "open"           : QtGui.QMessageBox.Open,
      "save"           : QtGui.QMessageBox.Save,
      "cancel"         : QtGui.QMessageBox.Cancel,
      "close"          : QtGui.QMessageBox.Close,
      "discard"        : QtGui.QMessageBox.Discard,
      "apply"          : QtGui.QMessageBox.Apply,
      "reset"          : QtGui.QMessageBox.Reset,
      "restore_default": QtGui.QMessageBox.RestoreDefaults,
      "help"           : QtGui.QMessageBox.Help,
      "save_all"       : QtGui.QMessageBox.SaveAll,
      "yes"            : QtGui.QMessageBox.Yes,
      "yes_to_all"     : QtGui.QMessageBox.YesToAll,
      "no"             : QtGui.QMessageBox.No,
      "no_to_all"      : QtGui.QMessageBox.NoToAll,
      "abort"          : QtGui.QMessageBox.Abort,
      "retry"          : QtGui.QMessageBox.Retry,
      "ignore"         : QtGui.QMessageBox.Ignore,
      "no button"      : QtGui.QMessageBox.NoButton,
      }


def makeMessageBox(message, buttons=["cancel","OK"], infotext=""):
  msg_box = QtGui.QMessageBox()
  msg_box.setText(message)
  msg_box.setInformativeText(infotext)
  msg_box.setWindowTitle("dialog")

  # save = QtGui.QMessageBox.Save
  # discard = QtGui.QMessageBox.Discard
  # cancel = QtGui.QMessageBox.Cancel
  mybuttons = BUTTONS[buttons[0]]
  for buts in buttons:
    mybuttons = mybuttons | BUTTONS[buts]

  msg_box.setStandardButtons(mybuttons) # discard | save | cancel);
  msg_box.show()
  r = msg_box.exec_()

  for i in BUTTONS:
    if r == BUTTONS[i]:
      return i

  return None


if __name__ == '__main__':
  a = QtGui.QApplication(sys.argv)
  s = makeMessageBox("hello this is a very long message  even longer than one expcts \n hello",
                                      infotext="gugus")
  print(s)
  sys.exit()
