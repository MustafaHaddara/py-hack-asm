#!/usr/bin/python
# hack parser

class Command():
	A_COMMAND = 0  # @Xxx
	C_COMMAND = 1  # dest=comp;jump
	L_COMMAND = 2  # (Xxx) ie label


class Parser():
	def __init__(self, fname):
		self.infile = open(fname, 'r')
		self.currentLine = ''


	def hasMoreCommands(self):
		# This is stupid and inefficient 
		line = self.infile.readline()
		self.infile.seek(-1*len(line), 1)
		return line != ''


	def advance(self):
		# Totally unpythonic
		self.currentLine = self.infile.readline().strip()


	def commandType(self):
		# Parse currentLine and decide which type of command it is
		if self.currentLine[0] == '@':
			return Command.A_COMMAND
		elif ('=' in self.currentLine) or (';' in self.currentLine):
			# Yay stupid generalizations
			return Command.C_COMMAND
		elif self.currentLine[0] == '(':
			return Command.L_COMMAND
		else:
			raise SyntaxError


	def symbol(self):
		if self.commandType() == Command.A_COMMAND:
			sym = self.currentLine[1:]  # cut off @
		elif self.commandType() == Command.L_COMMAND:
			sym = self.currentLine[1:-1] # trim out ( )
		else:
			raise SyntaxError

		return sym


	def dest(self):
		if (self.commandType() == Command.C_COMMAND) and ('=' in self.currentLine):
			dest = self.currentLine.split('=')[0]
		else:
			raise SyntaxError

		return dest


	def comp(self):
		if self.commandType() == Command.C_COMMAND:
			if '=' in self.currentLine:
				part = self.currentLine.split('=')[1]
				if ';' in part:
					comp = part.split(';')[0]
				else:
					comp = part
			elif ';' in self.currentLine:
				comp = self.currentLine.split(';')[0]
			else:
				raise SyntaxError

			return comp

		else:
			raise SyntaxError

	def jump(self):
		if self.commandType() == Command.C_COMMAND and (';' in self.currentLine):
			jump = self.currentLine.split(';')[-1]
		else:
			raise SyntaxError

		return jump





	def end(self):
		self.infile.close()