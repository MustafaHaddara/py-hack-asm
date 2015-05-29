#!/usr/bin/python
# hack assembler (main module)

import sys
from Parser import Parser
from Code import Code
from SymbolTable import SymbolTable

def main():
	asmFileName = getFileName()
	parser = Parser(asmFileName)

def getFileName():
	if len(sys.argv) != 2:
		print "Correct usage: assembler.py /path/to/asm/file"
		sys.exit(1)
	else:
		return sys.argv[1]

def openAndRead(infile):
	fh = open(infile, 'r')



if __name__ == '__main__':
	main()