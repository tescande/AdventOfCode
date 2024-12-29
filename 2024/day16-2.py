#!/bin/env python
# Solution is 516

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
	for row, line in enumerate(maze):
		for col, c in enumerate(line):
			if (row, col) in solpath:
				print(f"O", end='')
			else:
				print(f"{c}", end='')
		print("")
	print("")

def get_neighbour_cell(maze, cell, direction):
	row = cell[0] + direction[0]
	col = cell[1] + direction[1]

	if maze[row][col] == '#':
		return None

	return (row, col)

def backwalk_maze(maze, start, end, scores):
	q = deque()
	visited = set()
	res = 1

	for d in directions:
		cell = get_neighbour_cell(maze, end, d);
		if cell:
			q.append((end, d, scores[end]))

	while q:
		cell, d, score = q.popleft()

		for n_d in directions:
			n_cell = get_neighbour_cell(maze, cell, n_d);
			if n_cell is None:
				continue;

			n_score = score - 1
			if n_d != d:
				n_score -= 1000

			if n_cell in scores and scores[n_cell] in [n_score, n_score - 1000] and n_cell not in visited:
				res += 1
				visited.add(n_cell)
				q.append((n_cell, n_d, n_score))

	return res

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
			if n_d != d:
				n_score += 1000

			if n_cell not in scores or scores[n_cell] > n_score:
				scores[n_cell] = n_score
				q.append((n_cell, n_d, n_score))

	return backwalk_maze(maze, start, end, scores)

def main():
	maze = []

	file = sys.argv[1] if len(sys.argv)>=2 else 'day16-input.txt'
	with open(file, 'r') as f:
		for row, line in enumerate(f):
			col = line.find("E")
			if col >= 0:
				end = (row, col)

			col = line.find("S")
			if col >= 0:
				start = (row, col)

			maze.append(list(line[:-1]))

	res = solve_bfs(maze, start, end)

	print(f"Res: {res}")

if __name__ == "__main__":
    exit(main())
