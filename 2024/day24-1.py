#!/bin/env python
# Solution is 61495910098126

from collections import deque
import re
import sys

def eval_gate(inputs, w1, op, w2, out):
	if not w1 in inputs or w2 not in inputs:
		return False

	i1 = inputs[w1]
	i2 = inputs[w2]

	match op:
		case 'AND':
			inputs[out] = i1 & i2
		case 'OR':
			inputs[out] = i1 | i2
		case 'XOR':
			inputs[out] = i1 ^ i2
		case _:
			raise("Unknown operator {op}")

	return True

def main():
	file = sys.argv[1] if len(sys.argv)>=2 else 'day24-input.txt'
	_inputs, _gates = open(file, 'r').read().split('\n\n')

	inputs = {}
	for i in _inputs.strip().split('\n'):
		w, v = i.split(': ')
		inputs[w] = int(v)

	gates = deque()
	for g in _gates.strip().split('\n'):
		m = re.match(r'^(...) ([ANDXOR]+) (...) -> (...)', g)
		gates.append((m.group(1), m.group(2), m.group(3), m.group(4)))

	while gates:
		w1, op, w2, out = gates.popleft()
		if not eval_gate(inputs, w1, op, w2, out):
			gates.append((w1, op, w2, out))

	res = str()
	for w in reversed(sorted(inputs)):
		if w.startswith('z'):
			res += str(inputs[w])

	print(f"Res: {int(res, 2)}")

if __name__ == "__main__":
    exit(main())
