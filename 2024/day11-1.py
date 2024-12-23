#!/bin/env python
# Solution is 191690

import sys

def blink(stones):
	res = []

	for s in stones:
		length = len(str(s))
		if int(s) == 0:
			res.append(1)
		elif length & 1 == 0:
			res.append(int(str(s)[:length // 2]))
			res.append(int(str(s)[length // 2:]))
		else:
			res.append(s * 2024)

	return res

def main():
	stones = []
	file = sys.argv[1] if len(sys.argv)>=2 else 'day11-input.txt'
	with open(file, 'r') as f:
		stones = list(map(int, f.readline().split()))

	for i in range(25):
		stones = blink(stones)

	print(f"Res: {len(stones)}")

if __name__ == "__main__":
    exit(main())
