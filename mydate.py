#!/usr/bin/python

# -*- coding: utf-8 -*-
"""Framework for the StaidWorks shell.
"""

__doc__ = "mydate.py"
__author__ = "Staidworks, LLC"
__email__ = "contact@staidworks.com"
__version__ = "0.1"
__copyright__ = "Copyright (c) 2010 StaidWorks, LLC"
__license__ = "Python"
__status__ = "Production"

import usage
import os

datausage = "date [-i] [now]"

errmgr = usage.format()

class swshdate:


	def __init__(self):
		pass
	def display(self):
		os.system("date '+%h %d %y %H:%m:%S'")

	def command(self, args):
		if len(args) == 1:
			self.display()
		else:
			errmgr.msg(datausage)
