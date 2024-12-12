#!/bin/env python
# Solution is 663

import sys

def is_valid(values):
	prev = values[0]
	initial_delta = 0
	for v in values[1:]:
		delta = prev - v
		prev = v
		if delta == 0 or abs(delta) > 3:
			return 0

		if initial_delta == 0:
			initial_delta = delta
		elif (initial_delta < 0 and delta > 0) or \
			 (initial_delta > 0 and delta < 0):
			return 0

	return 1

def main():
	count = 0
	file = sys.argv[1] if len(sys.argv)>=2 else 'day02-input.txt'
	with open(file, 'r') as f:
		for line in f:
			values = list(map(int, line.split()))
			count += 1 if is_valid(values) else 0

	print(f"count: {count}")

if __name__ == "__main__":
    exit(main())
