#!/bin/env python
# Solution is 41,26

from collections import deque
import re
import sys

directions = [
	(-1,  0),
	( 0,  1),
	( 1,  0),
	( 0, -1),
]

def print_maze(maze, solpath={}):
	for y, line in enumerate(maze):
		for x, v in enumerate(line):
			if (x, y) in solpath:
				print(f"O", end='')
			else:
				print(f"{v}", end='')
		print("")
	print("")

def get_neighbour_cell(maze, cell, direction):
	x = cell[0] + direction[0]
	y = cell[1] + direction[1]

	if maze[y][x] == '#':
		return None

	return (x, y)

def solve_bfs(maze, start, end):
	q = deque()
	scores = {}

	q.append((start, (0, 1), 0))
	scores[start] = 0

	while q:
		cell, d, score = q.popleft()
		for n_d in directions:
			n_cell = get_neighbour_cell(maze, cell, n_d);
			if n_cell is None:
				continue;

			n_score = score + 1
			if n_cell not in scores or scores[n_cell] > n_score:
				scores[n_cell] = n_score
				q.append((n_cell, n_d, n_score))

	return end in scores

def main():
	width = 73
	height = 73
	max_bytes = 1024
	start = (1, 1)
	end = (71, 71)

	maze = []
	for y in range(height):
		maze.append([])
		for x in range(width):
			if x == 0 or x == width - 1 or y == 0 or y == height - 1:
				maze[y].append('#')
			else:
				maze[y].append('.')

	file = sys.argv[1] if len(sys.argv)>=2 else 'day18-input.txt'
	with open(file, 'r') as f:
		for n_bytes, line in enumerate(f):
			x, y = map(int, line[:-1].split(','))
			maze[y+1][x+1] = '#'

			if n_bytes > 1024 and not solve_bfs(maze, start, end):
				print(f"{x},{y}")
				break

if __name__ == "__main__":
    exit(main())
