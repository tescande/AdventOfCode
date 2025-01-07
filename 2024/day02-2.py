#!/bin/env python
# Solution is 692

import sys

def is_valid(values):
	prev = values[0]
	prev_delta = 0
	for v in values[1:]:
		delta = prev - v
		prev = v
		if delta == 0 or abs(delta) > 3:
			return False

		if prev_delta == 0:
			prev_delta = delta
		elif (prev_delta < 0 and delta > 0) or \
			 (prev_delta > 0 and delta < 0):
			return False

	return True

def main():
	count = 0
	file = sys.argv[1] if len(sys.argv)>=2 else 'day02-input.txt'
	with open(file, 'r') as f:
		for line in f:
			values = list(map(int, line.split()))
			good = is_valid(values)
			if not good:
				for i in range(0, len(values)):
					good = is_valid(values[0:i] + values[i+1:])
					if good:
						break

			if good:
				count += 1

	print(f"count: {count}")

if __name__ == "__main__":
    exit(main())
