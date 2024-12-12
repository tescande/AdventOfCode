#!/bin/env python
# Solution 2344

import sys

directions = [
	(0, -1), # up
	(1, -1), # up right
	(1, 0),  # right
	(1, 1),  # down right
	(0, 1),  # down
	(-1, 1), # down left
	(-1, 0), # left
	(-1, -1) # up left
]

next_chars = {
	'X': 'M',
	'M': 'A',
	'A': 'S',
}

def check_char(c, x, y, direction, lines):
	if x < 0 or y < 0 or y >= len(lines) or x >= len(lines[y]) or lines[y][x] != c:
		return 0;

	if c == 'S':
		return 1

	num_sol = 0
	if direction is None:
		for d in directions:
			num_sol += check_char(next_chars[c], x + d[0], y + d[1], d, lines)
	else:
		num_sol += check_char(next_chars[c], x + direction[0], y + direction[1], direction, lines)

	return num_sol

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
			if lines[y][x] == 'X':
				num_sol += check_char('X', x, y, None, lines)

	print(f"num_sol: {num_sol}")

if __name__ == "__main__":
    exit(main())
