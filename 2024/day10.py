#!/bin/env python
# Solution part 1 is 574
# Solution part 2 is 1238

import sys

direction = [
	(-1, 0),
	(0, 1),
	(1, 0),
	(0, -1),
]

def print_matrix(matrix):
	for line in matrix:
		print(f"{''.join(map(str, line))}")
	print("")

def get_at(matrix, r, c):
	if r < 0 or c < 0:
		return None

	try:
		return matrix[r][c]
	except:
		return None

def walk_trail(matrix, r, c, part1):
	v = get_at(matrix, r, c)
	if v == 9:
		if part1:
			matrix[r][c] = -1
		return 1

	res = 0
	for m in direction:
		next_v = get_at(matrix, r + m[0], c + m[1])
		if next_v is not None and next_v == v + 1:
			res += walk_trail(matrix, r + m[0], c + m[1], part1)

	return res

def restore_matrix(matrix):
	for r in range(len(matrix)):
		for c in range(len(matrix[r])):
			if get_at(matrix, r, c) == -1:
				matrix[r][c] = 9

def main():
	matrix = []
	file = sys.argv[1] if len(sys.argv)>=2 else 'day10-input.txt'
	with open(file, 'r') as f:
		for line in f:
			matrix.append(list(map(int, line[:-1])))

	res_p1 = 0
	res_p2 = 0
	for r in range(len(matrix)):
		for c in range(len(matrix[r])):
			if get_at(matrix, r, c) == 0:
				res_p1 += walk_trail(matrix, r, c, True)
				restore_matrix(matrix)
				res_p2 += walk_trail(matrix, r, c, False)

	print(f"Part 1: {res_p1}")
	print(f"Part 2: {res_p2}")

if __name__ == "__main__":
    exit(main())
