#!/bin/env python
# Solution is 1045

import sys
from math import gcd

def print_matrix(matrix):
	for line in matrix:
		print(f"{''.join(line)}")
	print("")

def print_matrix_and_antinodes(matrix, antinodes):
	for r in range(0, len(matrix)):
		for c in range(0, len(matrix[r])):
			if matrix[r][c] != '.':
				print(matrix[r][c], end='')
			elif antinodes[r][c] == '#':
				print('#', end='')
			else:
				print('.', end='')
		print("")
	print("")

def get_at(matrix, row, col):
	try:
		if row < 0 or col < 0:
			return None

		return matrix[row][col]
	except:
		return None

def set_at(matrix, row, col, v):
	matrix[row][col] = v

def set_antinodes(matrix, orig_r, orig_c, r, c, antinodes):
	res = 0
	drow = r - orig_r
	dcol = c - orig_c
	drow //= gcd(drow, dcol)
	dcol //= gcd(drow, dcol)

	while True:
		orig_r += drow
		orig_c += dcol
		if get_at(matrix, orig_r, orig_c) is None:
			break

		if get_at(antinodes, orig_r, orig_c) == '.':
			set_at(antinodes, orig_r, orig_c, '#')
			res += 1

	return res

def check_antenna(matrix, row, col, antenna, antinodes):
	res = 0
	for r in range(0, len(matrix)):
		for c in range(0, len(matrix[r])):
			if (r == row and c == col) or get_at(matrix, r, c)[0] != antenna:
				continue

			res += set_antinodes(matrix, row, col, r, c, antinodes)
	return res

def main():
	file = sys.argv[1] if len(sys.argv)>=2 else 'day08-input.txt'
	matrix = []
	antinodes = []
	with open(file, 'r') as f:
		for line in f:
			matrix.append(list(line[:-1]))
			antinodes.append(list('.' * len(line)))
	count = 0
	for row in range(0, len(matrix)):
		for col in range(0, len(matrix[row])):
			antenna = get_at(matrix, row, col);
			if antenna[0] != '.':
				count += check_antenna(matrix, row, col, antenna, antinodes)

	print_matrix_and_antinodes(matrix, antinodes)
	print(f"count: {count}")

if __name__ == "__main__":
    exit(main())
