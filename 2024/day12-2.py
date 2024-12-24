#!/bin/env python
# Solution is 821428

import sys

direction = [
	(-1,  0), # top
	( 0,  1), # right
	( 1,  0), # bottom
	( 0, -1), # left
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

def get_corners(garden, row, col, plant):
	corners = 0

	left = get_at(garden, row, col - 1)
	right = get_at(garden, row, col + 1)
	bottom = get_at(garden, row + 1, col)
	top = get_at(garden, row - 1, col)
	bottom_right = get_at(garden, row + 1, col + 1)
	bottom_left = get_at(garden, row + 1, col - 1)
	top_right = get_at(garden, row - 1, col + 1)
	top_left = get_at(garden, row - 1, col - 1)

	if left != plant:
		if top != plant:
			corners += 1
		elif top_left == plant:
			corners += 1
		if bottom != plant:
			corners += 1
		elif bottom_left == plant:
			corners += 1

	if right != plant:
		if top != plant:
			corners += 1
		elif top_right == plant:
			corners += 1
		if bottom != plant:
			corners += 1
		elif bottom_right == plant:
			corners += 1

	return corners


def walk(garden, row, col, plant, visited, region):
	corners = 0
	area = 1

	region[(row, col)] = 1
	visited[(row, col)] = 1

	corners = get_corners(garden, row, col, plant)

	for dr, dc in direction:
		r = row + dr
		c = col + dc

		if get_at(garden, r, c) == plant and (r, c) not in visited:
			co, ar = walk(garden, r, c, plant, visited, region)
			corners += co
			area += ar

	return corners, area

def main():
	garden = []
	visited = {}
	res = 0

	file = sys.argv[1] if len(sys.argv)>=2 else 'day12-input.txt'
	with open(file, 'r') as f:
		for line in f:
			garden.append(list(line[:-1]))

	for r in range(len(garden)):
		for c in range(len(garden)):
			if (r, c) not in visited:
				region = {}
				# The number of sides of a region is equal to the number of corners
				corners, area = walk(garden, r, c, garden[r][c], visited, region)
				res += corners * area

	print(f"Res: {res}")

if __name__ == "__main__":
    exit(main())
