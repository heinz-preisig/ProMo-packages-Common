#!/usr/local/bin/python3
# encoding: utf-8

"""

@author : "PREISIG, Heinz A"
@copyright : "Copyright 2015, PREISIG, Heinz A"

NOTE:constructStructureComponentID
 the graph component is not a class but a simple string. Reason being that it
 is easier to handle for the automaton implementation.
 Could be handled differently by defining a class with a __str__ method and
 a converting method when "loading" automaton.

 Object ID :  <structure ID>.<decoration ID>&<application-type>:<state>

 delimiters:
     O_delimiter = '.'
     T_delimiter = '&'  within the application type we split with |
     S_delimiter = ':'

  application_type is now also a composite:
     node : <nodetype>|<token>|conversion
     arc  : <arc type>|<token>|<mechanism>


  each arc and each node have a network membership

Application filters
  graphical_object level 0 - topology
  graphical object level i - adding layer i

@changes :2017-03-24 : simple node got a network indicator
"""

__project__ = "ProcessModeller  Suite"
__author__ = "PREISIG, Heinz A"
__copyright__ = "Copyright 2017, PREISIG, Heinz A"
__since__ = "2017. 03. 23"
__license__ = "GPL planned -- until further notice for internal Bio4Fuel & MarketPlace use only"
__version__ = "5.04 or later"
__email__ = "heinz.preisig@chemeng.ntnu.no"
__status__ = "beta"

import json
import os
import sys

from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets

from Common.resource_initialisation import DIRECTORIES
from Common.single_list_selector_impl import SingleListSelector
from Common.ui_string_dialog_impl import UI_String

# global
# terminology

DEFAULT = "default"

DIALOGUE = {
        "choose"   : "make a choice",
        "new model": "new model",
        "new case" : "new case"
        }

M_None = "-"  # used in place of None as the latter is not a string.
M_any  = "*"

# ontology definitions --------------------------------------------------------

ARC_COMPONENT_SEPARATOR = "|"
EQUATION_COMPONENT_SEPARATOR = "|"
CONNECTION_NETWORK_SEPARATOR = " >>> "  # RULE: separator is the same for inter and intra networks
CONVERSION_SEPARATOR = " --> "

TEMPLATE_ARC_APPLICATION = "%s" + ARC_COMPONENT_SEPARATOR + "%s" + ARC_COMPONENT_SEPARATOR + "%s"  # %(token,
# mechanism, nature)
TEMPLATE_CONNECTION_NETWORK = "%s" + CONNECTION_NETWORK_SEPARATOR + "%s"
TEMPLATE_EQUATION_ASSIGNMENT_KEY = "%s" + EQUATION_COMPONENT_SEPARATOR + "%s" + EQUATION_COMPONENT_SEPARATOR + "%s"
# % (node_type, nature, token)


def invertDict(dictionary):
  d = {}
  for i in dictionary:
    d[dictionary[i]] = i
  return d
  # return dict(zip(dictionary.values(), list(dictionary.keys())))


def getData(file_spec):
  # print("get data from ", file_spec)
  if os.path.exists(file_spec):
    f = open(file_spec, "r")
    data = json.loads(f.read())
    return data
  else:
    return None


def putDataOrdered(data, file_spec, indent="  "):
  dump = json.dumps(data, sort_keys=True, indent=indent)
  print("saved file : ", file_spec)
  with open(file_spec, "w") as f:
    f.write(dump)


def putData(data, file_spec, indent="  "):
  print("WRITING TO FILE: ", file_spec)
  dump = json.dumps(data, indent=indent)
  with open(file_spec, "w+") as f:
    f.write(dump)


def __getSortedDirList(location):
  """
  appears in two places,
  - at the beginning to select the model to be edited
  - to define a snippsel

  :return: model name
  """
  print("location: ", location)
  if not os.path.exists(location):
    # print("debugging no such directory")
    os.makedirs(location)
  things = os.listdir(location)
  dirs = []
  for thing in things:
    path, spec = os.path.split(thing)
    # print(path, spec)
    name, ext = os.path.splitext(spec)
    # print(name, ext)
    dirs.append(name)
  dirs.sort()

  return dirs


def askForModelFileGivenOntologyLocation(model_library_location, alternative=True, new=False, exit="exit"):
  acceptance_list = []
  if exit == "exit":
    model_names = [exit]
  else:
    model_names = []
  if not new:
    if alternative:
      model_names.append(DIALOGUE["new model"])
      acceptance_list.append(DIALOGUE["new model"])
    else:
      pass

    model_names.extend(__getSortedDirList(model_library_location))
    acceptance_list.extend(__getSortedDirList(model_library_location))

    modellist = SingleListSelector(model_names)
    modellist.exec_()
    modellist.show()
    model_name = modellist.getSelection()

  else:
    return DIALOGUE["new model"], True

  if model_name == DIALOGUE["new model"]:
    while (model_name in acceptance_list):
      ui_ask = UI_String("give new model name or type exit ", "model name or exit", limiting_list=acceptance_list)
      ui_ask.exec_()
      model_name = ui_ask.getText()
      print("new model name defined", model_name)
      if model_name == "exit":
        return model_name, False
    return model_name, True

  return model_name, False


def askForCasefileGivenLocation(case_rep_loc, alternative=True, new=False, exit="exit"):
  acceptance_list = []
  if exit == "exit":
    case_names = [exit]
  else:
    case_names = []
  if not new:
    if alternative:
      case_names.append(DIALOGUE["new case"])
      acceptance_list.append(DIALOGUE["new case"])
    else:
      pass

    case_names.extend(__getSortedDirList(case_rep_loc))
    acceptance_list.extend(__getSortedDirList(case_rep_loc))

    caselist = SingleListSelector(case_names)
    caselist.exec_()
    caselist.show()
    case_name = caselist.getSelection()

  else:
    return DIALOGUE["new case"], True

  if case_name == DIALOGUE["new case"]:
    while (case_name in acceptance_list):
      ui_ask = UI_String("give new case name or type exit ", "case name or exit", limiting_list=acceptance_list)
      ui_ask.exec_()
      case_name = ui_ask.getText()
      print("new case name defined", case_name)
      if case_name == "exit":
        return case_name, False
    return case_name, True

  return case_name, False


def getOntologyName(new=False, task="ProMo_logo", behaviour="on_click", accept_icon=None, reject_icon=None):
  from Common.logo_impl import Logo
  """
  asks for a ontology name from a list of ontologies in the repository
  if it allows for a new one.
  hiden directories are ignored
  :param new: logical
  :param task: selects logo from logo repository -- default is ProMo_logo
  :param behaviour: on_cklick makes logo to behave as button (default) alterenative is auto_close after selection has 
  been made
  :return:  depends on new
            new == True :  it returns the chosen ontology, but also the list of existing ontologies
                           that can be used to constrain the definition of a new one.
            new ==False:   it returns the chosen ontology
  """

  logo = Logo(task)  # ("task_ontology_foundation")
  if behaviour == "on_click":
    logo.exec_()
  else:
    logo.show()

  location = DIRECTORIES["ontology_repository"]

  ontologies_d = [f.path for f in os.scandir(location) if f.is_dir()]
  ontologies = [os.path.splitext(os.path.basename(o))[0] for o in ontologies_d]
  for o in ontologies:
    if o[0] == ".":
      ontologies.remove(o)

  if behaviour != "on_click":
    logo.close()

  ontology = __selectFromList(ontologies, accept_icon=accept_icon, reject_icon=reject_icon)
  if new:
    return ontology, ontologies
  elif ontology:
    return ontology
  else:
    sys.exit(0)


def makeTreeView(treeWidget, ontology_tree):
  root = "root"  # RULE: root of tree is called "root"

  treeWidget.clear()
  tree_items = {}
  networks = list(ontology_tree.keys())
  # root = self.root
  tree_items[root] = __addItemToTreeWidget(treeWidget, None, root)
  tree_items[root].name = ontology_tree[root]["name"]
  for nw in networks:
    if nw != root:
      parent = root
      child = ontology_tree[nw]["name"]
      nodes = []
      [nodes.append(n) for n in ontology_tree[nw]["parents"][::-1]]
      nodes.append(child)
      for child in nodes:
        if child in tree_items:
          parent = child
        else:
          parent_item = tree_items[parent]
          tree_items[child] = __addItemToTreeWidget(treeWidget, parent_item, child)
          tree_items[child].name = ontology_tree[child]["name"]
          parent = child

  treeWidget.expandAll()
  return tree_items


def __addItemToTreeWidget(treeWidget, parent, nodeID):
  name = str(nodeID)
  item = QtWidgets.QTreeWidgetItem(parent, None)
  item.nodeID = nodeID
  item.setText(0, name)
  item.setSelected(True)

  k = QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsUserCheckable \
    # | QtCore.Qt.ItemIsEditable
  item.setFlags(k)

  item.setSelected(False)

  treeWidget.addTopLevelItem(item)

  return item


def __selectFromList(items, accept_icon, reject_icon):
  items.sort()
  if accept_icon:
    if reject_icon:
      selector = SingleListSelector(items, accept_icon=accept_icon)
    else:
      selector = SingleListSelector(items, accept_icon=accept_icon, reject_icon=reject_icon)
  elif reject_icon:
    selector = SingleListSelector(items, reject_icon=reject_icon)
  else:
    selector = SingleListSelector(items)
  selector.setWindowTitle("ontology name")
  selector.exec_()
  selector.show()
  selection = selector.getSelection()
  del selector
  return selection


def saveBackupFile(path):
  ver_temp = "(%s)"
  (abs_name, ext) = os.path.splitext(path)  # path : directory/<name>.<ext>
  #  TODO: the access check fails -- not clear why, when removed writing works OK
  if os.path.exists(path):
    _f, ver = getFilesAndVersions(abs_name, ext)
    old = path
    new = abs_name + ver_temp % str(ver + 1) + ext
    os.rename(old, new)
    return old, new
  else:
    print("no such file : ", path)


def getFilesAndVersions(abs_name, ext):
  base_name = os.path.basename(abs_name)
  ver = 0  # initial last version
  _s = []
  directory = os.path.dirname(abs_name)  # listdir(os.getcwd())
  files = os.listdir(directory)

  for f in files:
    n, e = os.path.splitext(f)
    #        print 'name', n
    if e == ext:  # this is another type
      if n[0:len(base_name) + 1] == base_name + "(":  # only those that start with name
        #  extract version
        l = n.index("(")
        r = n.index(")")
        assert l * r >= 0  # both must be there
        v = int(n[l + 1:r])
        ver = max([ver, v])
        _s.append(n)
  return _s, ver


# NOTE: the global handling of the IDs has been abandoned for the time being -- was not practical now but may be
# necessary to reconsider in the future
# RULE: ProMoIRIs are handled local to the ontologies for the time being.
# def globalEquationID(update=False, reset=False):
#   """
#   defines a new global equation ID
#   :param reset: if true it will reset the counter to 0 and returns the 0 as the first ID
#   :return: ID
#   """
#   return globalID(FILES["global_equation_identifier"],update=update, reset=reset)
#
# def globalVariableID( update=False, reset=False):
#   """
#   defines a new global equation ID  essentially implements a global enumeration variable
#   :param reset: if true it will reset the counter to 0 and returns the 0 as the first ID
#   :return: ID
#   """
#   return globalID(FILES["global_variable_identifier"], update=update, reset=reset)
#
#
# def globalID(file, update=False, reset=False):
#   """
#   utility function for defining global ID for variables and equations.
#   NOTE: python runs this function when importing the function... that's very unfortunate as it changes the counter.
#         So there was a need for more control.
#   :param file:  file name -- allows for several enumeration types
#   :param update: adds control allowing to have the module to be loaded without changing the global counter
#   :param reset: reset the counter.
#   :return: the new ID
#   """
#
#   if (not os.path.exists(file)) or reset:
#     with open(file,'w') as f:
#       f.write('0')
#       return 0
#   with open(file) as f:
#     a = f.read()
#   ID = int(a) + 1
#
#   if update:
#     with open(file,'w') as f:
#       f.write(str(ID))
#
#       # print("debugging -- 383 -- new ID:",ID)
#   return ID


def walkDepthFirstFnc(tree, id):
  """
  walk a tree depth first iteratively
  :param tree: container with node and its children specified tree[#node]["children" ]
  :param id: #node
  :return: nodes
  """
  nodes = []
  stack = [id]
  while stack:
    cur_node = stack[0]
    stack = stack[1:]
    nodes.append(cur_node)
    for child in reversed(tree[cur_node]["children"]):
      stack.insert(0, child)
  return nodes


def walkBreathFirstFnc(tree, id):
  """
  walk a tree breath first iteratively
  :param tree: container with node and its children specified tree[#node]["children" ]
  :param id: #node
  :return: nodes
  """
  nodes = []
  stack = [id]
  while stack:
    cur_node = stack[0]
    stack = stack[1:]
    nodes.append(cur_node)
    for child in tree[cur_node]["children"]:
      stack.append(child)
  return nodes


# ===========================================  icons ==============================
ICONS = {}
ICONS["+"] = "plus-icon.png"
ICONS["-"] = "minus-icon.png"
ICONS["->"] = "right-icon.png"
ICONS["<-"] = "left-icon.png"
ICONS["^"] = "up-icon.png"
ICONS["v"] = "right-icon.png"
ICONS["delete"] = "icon_trash_it.png"
ICONS["ontology"] = "ontology.xpm"
ICONS["exit"] = "exit.xpm"
ICONS["task_automata"] = "task_automata.svg"
ICONS["task_ontology_foundation"] = "task_ontology_foundation.svg"
ICONS["task_ontology_equations"] = "task_ontology_equations.svg"
ICONS["task_model_composer"] = "task_model_composer.svg"
ICONS["task_graphic_objects"] = "task_graphic_objects.svg"
ICONS["task_entity_generation"] = "task_entity_generation.svg"
ICONS["task_automata"] = "task_automata.svg"
ICONS["info"] = "info_button.png"
ICONS["accept"] = "accept.png"
ICONS["reject"] = "reject.png"
ICONS["back"] = "back.png"
ICONS["new"] = "new_button.png"
ICONS["compile"] = "compile_button.png"
ICONS["dot_graph"] = "dot_graph_button.png"
ICONS["save"] = "save_button.png"

BUTTON_ICON_SIZE = QtCore.QSize(40, 40)
BUTTON_ICON_STYLE_ROUND = 'background-color: black; '
BUTTON_ICON_STYLE_ROUND += 'border-style: outset; '
BUTTON_ICON_STYLE_ROUND += 'border-width: 2px; '
BUTTON_ICON_STYLE_ROUND += 'border-radius: 20px; '
# BUTTON_ICON_STYLE_ROUND += 'border-color: beige;    '
BUTTON_ICON_STYLE_ROUND += 'font: bold 14px;   '
BUTTON_ICON_STYLE_ROUND += 'padding: 6px;'


def getIcon(what):
  assert what in ICONS.keys()
  f_name = os.path.join(DIRECTORIES["icon_location"], ICONS[what])
  # print("debugging .....", f_name)
  if os.path.exists(f_name):
    pm = QtGui.QPixmap(f_name)
    return QtGui.QIcon(pm)
  else:
    print("no such file : ", f_name)
    pass


def roundButton(button, what, tooltip=None):
  button.setIcon(getIcon(what))
  button.setStyleSheet(BUTTON_ICON_STYLE_ROUND)
  button.setIconSize(BUTTON_ICON_SIZE)
  button.setToolTip(tooltip)
