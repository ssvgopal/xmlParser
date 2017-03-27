# -*- coding: utf-8 -*-
"""
Created on Thu Mar 2 10:19:24 2017

@author: Sai Sunkara
"""

"""XML sort and parse tool to compare 2 xml files effectively.
"""

import time, datetime
import os
import sys
import re
import logging
import hashlib
import MainWindowUI
import lxml.etree as le
from lxml import etree, objectify
from difflib import SequenceMatcher
import PyQt4
from PyQt4 import uic
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from collections import defaultdict

class MainWindow():
  pass


def sort_attrs(item, sorteditem):
  """Sort XML attributes alphabetically by key.
  The original item is left unmodified and its attributes are copied to the
  provided `sorteditem`.
  """
  attrkeys = sorted(item.keys())
  for key in attrkeys:
    sorteditem.set(key, item.get(key))

def sort_file(envobj):
  """Sort the provided XML file.
  """
  xmlorig = envobj['tree']
  xmlroot = xmlorig.getroot()
  gl_win_node_count = 0 #Reset for this file

  # Create a new XML element that will be the top of the sorted copy of
  # the XML file
  newxmlroot = le.Element(xmlroot.tag)

  # Create the sorted copy of the XML file
  sort_attrs(xmlroot, newxmlroot)
  envobj['depth'] = 0
  sort_elements()

  newtree = le.ElementTree(newxmlroot)
  rootnode = newtree.getroot()
  envobj['sortedtree']=newtree

if __name__ == '__main__':
  # Sort the arguments

  app = QApplication(sys.argv)
  window = MainWindow()
  mainwindow = window
  window.show()
  
  sys.exit(app.exec_())
