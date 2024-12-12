#!/bin/env python
# Solution is 2941973819040

import re
import sys

def evaluate(ops, target):
	current_op = -1
	res = ops[0]

	for i in range(1, len(ops) - 1, 2):
		if i >= len(ops):
			break
		if ops[i] == '+':
			res += ops[i+1]
		elif ops[i] == '*':
			res *= ops[i+1]
		else:
			print(f"Invalid op {ops[i]} at {i}")

		if res > target:
			return False

		if res == target:
			return True

	return False

def calc(plates, target):
	ops = []
	num_op = len(plates) - 1

	for i in range(0, 1 << num_op):
		ops.clear()
		for j in range(0, num_op):
			ops.append(plates[j])
			if i & (1 << j):
				ops.append('+')
			else:
				ops.append('*')
		ops.append(plates[-1])

		if evaluate(ops, target):
			return target

	return 0

def main():
	res = 0
	file = sys.argv[1] if len(sys.argv)>=2 else 'day07-input.txt'
	with open(file, 'r') as f:
		for line in f:
			m = re.match(r"^(\d+):(.*)$", line)
			if m is None:
				#print(f"Failed to parse {line[:-1]}")
				continue

			target = int(m.group(1))
			plates = list(map(int, m.group(2).split()))

			res += calc(plates, target)

	print(f"res: {res}")

if __name__ == "__main__":
    exit(main())
