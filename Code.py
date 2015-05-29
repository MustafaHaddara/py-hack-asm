#!/usr/bin/python
# hack code translator

# M = 1
# 111
# a = 0
# cccccc = 1111 11
# ddd = 001
# jjj = 000
# 1110 1111 1100 1000

jumpTable = { 'null': '000',
			  'JGT' : '001',
			  'JEQ' : '010',
			  'JEQ' : '010',
			  'JGE' : '011',
			  'JLT' : '100',
			  'JNE' : '101',
			  'JLE' : '110',
			  'JMP' : '111'  }

compTable = { '0'   : '101010',
			  '1'   : '111111',
			  '-1'  : '111010',
			  'D'   : '001100',
			  'A'   : '110000',
			  '!D'  : '001101',
			  '!A'  : '110001',
			  '-D'  : '001111',
			  '-A'  : '110011',
			  'D+1' : '011111',
			  'A+1' : '110111',
			  'D-1' : '001110',
			  'A-1' : '110010',
			  'D+A' : '000010',
			  'D-A' : '010011',
			  'A-D' : '000111',
			  'D&A' : '000000',
			  'D|A' : '010101' }


def dest(srcStr):
	# Of the three portions of the opcodes,
	# this is the only one that makes obvious logical sense
	# No point in a lookup table

	# Any combination of A, D, M
	# in that order
	# TODO: bitops this
	bits = ['0', '0', '0']  # 0 by default
	if 'A' in srcStr:
		bits[0] = '1'
	if 'D' in srcStr:
		bits[1] = '1'
	if 'M' in srcStr:
		bits[2] = '1'

	return ''.join(bits)


def comp(srcStr):
	aBit = '0'

	if 'M' in srcStr:
		if 'A' in srcStr:
			raise SyntaxError
		else:
			aBit = '1'
			nStr = srcStr.replace('M', 'A')  # this way we use only one lookup table

	else:
		nStr = srcStr[]

	return aBit + compTable[nStr]	


def jump(srcStr):
	return jumpTable[srcStr]
	
	
