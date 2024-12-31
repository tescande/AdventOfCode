#!/bin/env python
# Solution is 264

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

def backwalk_maze(maze, start, end, scores):
	q = deque()
	solpath = set()
	res = 0

	cell = t_cell = end
	solpath.add(end)
	while cell != start:
		for n_d in directions:
			n_cell = get_neighbour_cell(maze, cell, n_d);
			if n_cell is None:
				continue;

			if n_cell in scores and scores[n_cell] < scores[t_cell]:
				t_cell = n_cell

		solpath.add(t_cell)
		cell = t_cell

	return solpath

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

	return backwalk_maze(maze, start, end, scores)

def main():
	# ~ width = 9
	# ~ height = 9
	# ~ max_bytes = 12
	# ~ start = (1, 1)
	# ~ end = (7, 7)

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
			if n_bytes >= max_bytes:
				break

			x, y = map(int, line[:-1].split(','))
			maze[y+1][x+1] = '#'

	solpath = solve_bfs(maze, start, end)
	print_maze(maze, solpath)

	print(f"Res: {len(solpath)-1}")

if __name__ == "__main__":
    exit(main())
