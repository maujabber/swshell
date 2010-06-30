#!/usr/bin/python

# -*- coding: utf-8 -*-
"""Framework for the StaidWorks shell.
"""

__doc__ = "ipaddr.py"
__author__ = "Staidworks, LLC"
__email__ = "contact@staidworks.com"
__version__ = "0.1"
__copyright__ = "Copyright (c) 2010 StaidWorks, LLC"
__license__ = "Python"
__status__ = "Production"

import usage
import os

datausage = "ipaddr address  broadcast netmask "

errmgr = usage.format()

class setip:

	def __init__(self):
		pass
	def display(self):
		errmgr.msg(datausage)
		
	def command(self, args):
		if len(args) == 1:
			self.display()	
		else:
			print "change IP Address"
