
Process Modeller ProMod Equation Editor
=======================================

.. image:: file: /home/heinz/1_Gits/ProcessModeller/ProcessModeller_v7_04/packages/Common/icons/task_ontology_equations.png
   :align: center
   :scale: 50
   :height: 300px





Usage
-----

.. |date| date::

:Date: 2020-02-28
:Version: 7.04
:Authors:
    - Heinz A `PREISIG`_


 .. _PREISIG: https://www.ntnu.no/ansatte/heinz.a.preisig

How to use
----------

1) Initial dialog askes for an ontology name
    - rejecting opens a dialog asking for a new ontology name
        - rejecting exits
        - providing name generates the directories and the infrastructure for the ontology and models being build using this ontology.
2) Main window opens providing four choices
    - variables --> opens a tree view of the onotology-defined structure in the first tab
        - selection of an entry triggers the editing mode for the tree components
            - graph
            - node
            - arc
        - selection of  variable class shown below opens a new window with a table of the defined variables for this node in the definition tree and the selected variable class. See point 3) to continue.
    - variable aliases  --> opens the same tree view selection of an entry in the tree opens a new window with the alias table for the selection. The columns are labelled with the available compilation languages.
    - compile --> compiles all variable & equations into the target languages and generates a LaTex documentation that is discplayed.
    - index aliases --> opens a window to change the notation of the aliases. These are usually not to be modified. The default notation served us sofar very well indeed.

3) Entering or modifying an equation
    - on selecting a variable class to edit, a table for the variable class on the selected tree node is opened. It shows the currently defined variable.
        - new variables are defined by clicking on the anywhere in the type column.
        - a new variable may be 
            - a port variable, that is it is not a function of other variables or
            - a variable defined by an equation
        - variables are defined for a specific tree node. The context extends all the way down the branch
        - once a variable is defined, equations can be added to its definition. Those new / additional definitions may be on a node in the context branch
        - labels and descriptions can be changed,
        - units and indices cannot be changed once the variable is used in an expression because the information is used to define the new variables.
        - equations can be edited by selecting the respective field in the "eqs" column



