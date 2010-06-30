#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Framework for the StaidWorks shell.
"""

__author__ = "Staidworks, LLC"
__email__ = "contact@staidworks.com"
__version__ = "0.1"
__copyright__ = "Copyright (c) 2010 StaidWorks, LLC"
__license__ = "Python"
__status__ = "Production"

import exceptions
import grp
import os
import pwd
import shlex
import signal
import subprocess
import sys
import threading
import time
import mydate
import intro
import passwd
import ipaddr

command_list = ['date',
		'ipaddr',
		'passwd',
		'show'
		]

a = intro.swsh()
a.display()

class ExitException(exceptions.BaseException):
	""""exit" command is given to the shell."""
	pass

class SIGINTException(exceptions.BaseException):
	"""SIGINT has been received."""
	pass

class MShell():
	"""A primitive interactive shell."""

	def __init__(self):
		"""Initializes shell."""
		signal.signal(signal.SIGINT, self.sigint_handler)

	def run(self):
		"""Starts the infinite loop for receiving input
		until one of the exceptions is raised.
		"""

		date = mydate.swshdate()
		changepass = passwd.mypass()
		changeip = ipaddr.setip()

		while(True):
			try:
				prompt = "[%s@%s %s]>> " % \
					(os.getlogin(),
					os.uname()[1],
					os.path.basename(os.getcwd()))
				command = raw_input(prompt)
				args = shlex.split(command)

				if args[0] == "exit":
					raise ExitException

				if args[0] == "quit":
					raise ExitException				 
				
				if args[0] in command_list:
					if args[0] == "date":
						date.command(args)
					if args[0] == "ipaddr":
						changeip.command(args)	
					elif args[0] == "passwd":
						changepass.command(args)
				else:
					print args, ": Command not found"

			except IndexError:
				continue

			except EOFError:
				print "<EOF received, bye-bye>"
				return 0

			except ExitException:
				print "<exit called, bye-bye>"
				return 0

			except SIGINTException:
				print >> sys.stderr, \
					"<SIGINT received, bye-bye>"
				return 1

	def sigint_handler(self, signum, frame):
		"""Handler for the SIGINT signal."""
		raise SIGINTException

	def default(self, *args):
		"""Default handler for programs that aren't recognized as
		internal commands. Passes arguments to the child program.
		"""
		try:
			proc = subprocess.Popen(args,
				executable = args[0],
				stdin = sys.stdin,
				stdout = sys.stdout,
				stderr = sys.stderr)

		except OSError, e:
			print e

		else:
			print "Executing child process", proc.pid
			proc.wait()



if __name__ == "__main__":
	sys.exit(MShell().run())
