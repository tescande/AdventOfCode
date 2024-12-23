#!/bin/env python
# Solution is 1431316

import sys

direction = [
	(-1, 0),
	(0, 1),
	(1, 0),
	(0, -1),
]

def print_garden(garden):
	for line in garden:
		print(f"{''.join(map(str, line))}")
	print("")

def get_at(matrix, r, c):
	if r < 0 or c < 0:
		return None

	try:
		return matrix[r][c]
	except:
		return None

def walk(garden, row, col, plant, visited, region):
	perimeter = 0
	area = 1

	region[(row, col)] = 1
	visited[(row, col)] = 1

	for d in direction:
		r = row + d[0]
		c = col + d[1]
		if get_at(garden, r, c) == plant and (r, c) not in visited:
			p, a = walk(garden, r, c, plant, visited, region)
			perimeter += p
			area += a
		elif (r, c) not in region:
			perimeter += 1

	return perimeter, area

def main():
	garden = []
	file = sys.argv[1] if len(sys.argv)>=2 else 'day12-input.txt'
	with open(file, 'r') as f:
		for line in f:
			garden.append(list(line[:-1]))

	res = 0
	visited = {}
	for r in range(len(garden)):
		for c in range(len(garden)):
			if (r, c) not in visited:
				region = {}
				p, a = walk(garden, r, c, garden[r][c], visited, region)
				res += p * a

	print(f"Res: {res}")

if __name__ == "__main__":
    exit(main())
