#!/bin/env python
# Solution is 228651922369703

import sys

def blink(stone, num_blinks, lengths):
	res = []

	if (stone, num_blinks) in lengths:
		return lengths[(stone, num_blinks)]

	length = len(str(stone))
	if num_blinks == 0:
		res = 1
	elif stone == 0:
		res = blink(1, num_blinks - 1, lengths)
	elif length & 1 == 0:
		s1 = int(str(stone)[:length // 2])
		s2 = int(str(stone)[length // 2:])
		res = blink(s1, num_blinks - 1, lengths) + blink(s2, num_blinks - 1, lengths)
	else:
		res = blink(stone * 2024, num_blinks - 1, lengths)

	lengths[(stone, num_blinks)] = res
	return res

def main():
	stones = []
	lengths = {}
	file = sys.argv[1] if len(sys.argv)>=2 else 'day11-input.txt'
	with open(file, 'r') as f:
		stones = list(map(int, f.readline().split()))


	res = 0
	for s in stones:
		res += blink(s, 75, lengths)

	print(f"Res: {res}")

if __name__ == "__main__":
    exit(main())
