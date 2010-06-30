#!/usr/bin/python

# -*- coding: utf-8 -*-
"""Framework for the StaidWorks shell.
"""

__doc__ = "passwd.py"
__author__ = "Staidworks, LLC"
__email__ = "contact@staidworks.com"
__version__ = "0.1"
__copyright__ = "Copyright (c) 2010 StaidWorks, LLC"
__license__ = "Python"
__status__ = "Production"

import usage
import os

datausage = "passwd"

errmgr = usage.format()

class mypass:

	def __init__(self):
		pass
	def display(self):
		errmgr.display(datausage)
		
	def command(self, args):
		if len(args) != 1:
			self.display()	
		else:
			print "change passwd"
