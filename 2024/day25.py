#!/bin/env python
# Solution is 3114

import sys

def fit(key, lock, height):
	for kv, kl in zip(key, lock):
		if kv + kl > height:
			return False

	return True

def main():
	file = sys.argv[1] if len(sys.argv)>=2 else 'day25-input.txt'
	with open(file, 'r') as f:
		entries = f.read().split('\n\n')

		locks = []
		keys = []
		height = 0
		for entry in entries:
			lines = entry.strip().split('\n')
			values = list([0] * len(lines[0]))
			height = len(lines)

			for line in lines:
				for i, v in enumerate(line):
					if v == '#':
						values[i] += 1

			if entry[0][0] == '#':
				locks.append(values)
			else:
				keys.append(values)

	res = 0
	for key in keys:
		for lock in locks:
			if fit(key, lock, height):
				res += 1

	print(f"Res: {res}")

if __name__ == "__main__":
    exit(main())
