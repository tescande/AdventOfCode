#!/bin/env python
# Solution is 249943041417600

import re
import sys

def calc(plates, target):
	if len(plates) == 1:
		return plates[0] == target

	if calc([plates[0] + plates[1]] + plates[2:], target):
		return True

	if calc([plates[0] * plates[1]] + plates[2:], target):
		return True

	if calc([int(str(plates[0]) + str(plates[1]))] + plates[2:], target):
		return True

	return False

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

			if calc(plates, target):
				res += target

	print(f"res: {res}")

if __name__ == "__main__":
    exit(main())
