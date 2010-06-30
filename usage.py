#!/usr/bin/python


# -*- coding: utf-8 -*-
"""Framework for the StaidWorks shell.
"""

__doc__ = "usage.py"
__author__ = "Staidworks, LLC"
__email__ = "contact@staidworks.com"
__version__ = "0.1"
__copyright__ = "Copyright (c) 2010 StaidWorks, LLC"
__license__ = "Python"
__status__ = "Production"

appname = "SWshell"
intro = ": Command Usage"

class format:

	def __init__(self):
		pass

	def msg(self, command):
		print  appname, __version__, intro, "\n", command, "\n",

