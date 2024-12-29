#!/bin/env python
# Solution is 4,3,7,1,5,3,0,5,4

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

def run(regs, prog):
	out = []
	sp = 0
	p_len = len(prog)

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
				out.append(f"{get_combo_op(op, regs) & 7}")
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
			m = re.match(r"^Register (.): (\d+)$", line)
			if m:
				regs[m.group(1)] = int(m.group(2))
				continue

			m = re.match(r"^Program: ([\d,]+)$", line)
			if m:
				prog = list(map(int, m.group(1).split(',')))

	res = run(regs, prog)
	print(','.join(res))

if __name__ == "__main__":
    exit(main())
