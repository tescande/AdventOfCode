#!/bin/env python
# Solution is 303

import sys

def print_matrix(matrix):
	for line in matrix:
		print(f"{''.join(line)}")
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
	anti_r = 2 * r - orig_r
	anti_c = 2 * c - orig_c
	if get_at(matrix, anti_r, anti_c) is not None:
		if get_at(antinodes, anti_r, anti_c) != '#':
			set_at(antinodes, anti_r, anti_c, '#')
			return 1

	return 0

def check_antenna(matrix, row, col, antenna, antinodes):
	res = 0
	for r in range(len(matrix)):
		for c in range(len(matrix[r])):
			if (r == row and c == col) or get_at(matrix, r, c)[0] != antenna:
				continue

			res += set_antinodes(matrix, row, col, r, c, antinodes)

	return res

def main():
	matrix = []
	antinodes = []
	file = sys.argv[1] if len(sys.argv)>=2 else 'day08-input.txt'
	with open(file, 'r') as f:
		for line in f:
			matrix.append(list(line[:-1]))
			antinodes.append(list('.' * len(line)))

	count = 0
	for row in range(len(matrix)):
		for col in range(len(matrix[row])):
			antenna = get_at(matrix, row, col);
			if antenna[0] != '.':
				count += check_antenna(matrix, row, col, antenna, antinodes)

	print(f"count: {count}")

if __name__ == "__main__":
    exit(main())
