#!/bin/env python
# Solution 1815

import sys

def get_char(x, y, lines):
	if x < 0 or y < 0 or y >= len(lines) or x >= len(lines[y]):
		return '_'

	return lines[y][x]

def check_xmas(x, y, lines):
	if get_char(x, y, lines) != 'A':
		return 0

	c11 = get_char(x - 1, y - 1, lines)
	c12 = get_char(x + 1, y + 1, lines)
	c21 = get_char(x + 1, y - 1, lines)
	c22 = get_char(x - 1, y + 1, lines)

	if ((c11 == 'M' and c12 == 'S')  or  \
	    (c11 == 'S' and c12 == 'M')) and \
	   ((c21 == 'M' and c22 == 'S')  or  \
	    (c21 == 'S' and c22 == 'M')):
		return 1;

	return 0

def main():
	res = 0
	lines = []
	file = sys.argv[1] if len(sys.argv)>=2 else 'day04-input.txt'
	with open(file, 'r') as f:
		for line in f:
			lines.append(line[:-1])

	num_sol = 0
	for y in range(0, len(lines)):
		for x in range(0, len(lines[y])):
			num_sol += check_xmas(x, y, lines)

	print(f"num_sol: {num_sol}")

if __name__ == "__main__":
    exit(main())
