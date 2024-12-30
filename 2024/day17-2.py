#!/bin/env python
# Solution is 190384615275535

import re
import sys

insts = [ "adv", "bxl", "bst", "jnz", "bxc", "out", "bdv", "cdv" ]

def get_combo_op(op, regs):
	match op:
		case 4:
			op = regs['A']
		case 5:
			op = regs['B']
		case 6:
			op = regs['C']

	return op

def run(prog, regA):
	out = []
	sp = 0
	p_len = len(prog)
	regs = { 'A': regA, 'B': 0, 'C': 0 }

	while sp < p_len:
		inst = prog[sp]
		op = prog[sp + 1]

		match insts[inst]:
			case "adv":
				regs['A'] = regs['A'] >> get_combo_op(op, regs)
			case "bxl":
				regs['B'] = regs['B'] ^ op
			case "bst":
				regs['B'] = get_combo_op(op, regs) & 7
			case "jnz":
				if regs['A']:
					sp = op - 2
			case "bxc":
				regs['B'] = regs['B'] ^ regs['C']
			case "out":
				out.append(get_combo_op(op, regs) & 7)
			case "bdv":
				regs['B'] = regs['A'] >> get_combo_op(op, regs)
			case "cdv":
				regs['C'] = regs['A'] >> get_combo_op(op, regs)
		sp += 2

	return out

def main():
	regs = {}
	prog = []

	file = sys.argv[1] if len(sys.argv)>=2 else 'day17-input.txt'
	with open(file, 'r') as f:
		for line in f:
			m = re.match(r"^Program: ([\d,]+)$", line)
			if m:
				prog = list(map(int, m.group(1).split(',')))

	# What the program does is:
	#  - Take the last 3 bits of reg A
	#  - Do some calculations
	#  - Print a result
	#  - Shift reg A >> 3
	#  - start over until reg A is 0
	# This loop test all values for last 3 bits until it prints the
	# corresponding program instruction or operand
	regA = 0
	for i in reversed(range(len(prog))):
		regA <<= 3
		while run(prog, regA) != prog[i:]:
			regA += 1

	print(regA)

if __name__ == "__main__":
    exit(main())
