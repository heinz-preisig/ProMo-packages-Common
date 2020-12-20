
"""
===============================================================================
 define data record structures
===============================================================================

This program is part of the ProcessModelling suite

This extends the record structures definitions because of loop in intialisation
The intention is to bring this further up into an ontology

"""

__project__ = "ProcessModeller  Suite"
__author__ = "PREISIG, Heinz A"
__copyright__ = "Copyright 2015, PREISIG, Heinz A"
__since__ = "15.11.2020"
__license__ = "GPL planned -- until further notice for Bio4Fuel & MarketPlace internal use only"
__version__ = "7.00"
__version__ = "8.00"
__email__ = "heinz.preisig@chemeng.ntnu.no"
__status__ = "beta"

from copy import deepcopy

from Common.common_resources import ENTITY_OBJECT_SEPARATOR
from Common.common_resources import TEMPLATE_ENTITY_OBJECT



def functionMakeObjectStringID(network, entity, variant):
  entity_str_ID = TEMPLATE_ENTITY_OBJECT % (network, entity, variant)
  return entity_str_ID

def functionGetObjectsFromObjectStringID(entity_str_ID):
  network, entity, variant = entity_str_ID.split(ENTITY_OBJECT_SEPARATOR)
  return network, entity, variant

class EntityBehaviour(dict):
  def __init__(self, networks, entities):
    super().__init__()
    for nw in networks:
      for entity in entities[nw]:
        entity_str_ID = TEMPLATE_ENTITY_OBJECT % (
                nw, entity, "base")  # RULE: "base" is used for the base bipartite graph
        self[entity_str_ID] = None

  def addVariant(self, network, entity, variant, data):
    entity_str_ID = functionMakeObjectStringID(network, entity, variant)

    # self[entity_str_ID] = VariantRecord(tree=data["tree"],
    #                                     nodes=data["nodes"],
    #                                     IDs= data["IDs"],
    #                                     root_variable = data["root_variable"],
    #                                     blocked_list = data["blocked"],
    #                                     buddies_list = data["buddies"])
    self[entity_str_ID] = deepcopy(data)

  def removeVariant(self, network, entity, variant):
    entity_str_ID = functionMakeObjectStringID(network, entity, variant)
    if variant == "base":
      for o in self:
        if "base" not in o:
          del self[entity_str_ID]
        else:
          self[o] = None
    else:
      del self[entity_str_ID]


  def getRootVariableID(self, entity_str_ID):
    return int(self[entity_str_ID]["root_variable"])

  def getVariantList(self):
    variant_set = set()
    for entity_str_ID in self:
      network, entity, variant = functionGetObjectsFromObjectStringID(entity_str_ID)
      variant_set.add(variant)
    return sorted(variant_set)

  def getEquationIDList(self, entity_str_ID ):
    equation_ID_list = []
    for n in self[entity_str_ID]["nodes"]:
      _label, ID = self[entity_str_ID]["nodes"][n].split("_")
      if _label == "equation":
        equation_ID_list.append(int(ID))
    return equation_ID_list

  def getBlocked(self, entity_str_ID):
    blocked_ID = []
    for ID in self[entity_str_ID]["blocked"]:
      blocked_ID.append(int(ID))
    return blocked_ID


class VariantRecord(dict):  # .............................................................. hash is global index_ID
  def __init__(self, tree={}, nodes=[], IDs=[], root_variable=None, blocked_list=[], buddies_list=[]):
    super()
    self["tree"] = tree
    self["nodes"] = nodes
    self["IDs"] = IDs
    self["root_variable"] = root_variable
    self["blocked"] = blocked_list
    self["buddies"]= buddies_list
  #
  # def getEquationIDList(self, ):
  #   equation_ID_list = []
  #   for n in self["nodes"]:
  #     _label, ID = self["nodes"][n].split("_")
  #     if _label == "equation":
  #       equation_ID_list.append(ID)
  #
  #   return equation_ID_list