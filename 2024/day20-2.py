#!/bin/env python
# Solution is 983054

from collections import deque
import re
import sys

directions = [
	(-1,  0),
	( 1,  0),
	( 0,  1),
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

def solve_bfs(maze, start, end):
	q = deque()
	scores = {}

	q.append((start, (0, 1), 0))
	scores[start] = 0

	while q:
		cell, d, score = q.popleft()

		if cell == end:
			break

		for n_d in directions:
			n_cell = get_neighbour_cell(maze, cell, n_d);
			if n_cell is None:
				continue;

			n_score = score + 1
			if n_cell not in scores or scores[n_cell] > n_score:
				scores[n_cell] = n_score
				q.append((n_cell, n_d, n_score))

	return scores

def main():
	maze = []
	file = sys.argv[1] if len(sys.argv)>=2 else 'day20-input.txt'
	with open(file, 'r') as f:
		for row, line in enumerate(f):
			col = line.find("E")
			if col >= 0:
				end = (row, col)

			col = line.find("S")
			if col >= 0:
				start = (row, col)

			maze.append(list(line[:-1]))

	scores = solve_bfs(maze, start, end)

	res = 0
	solpath = sorted(scores, key=scores.get)
	for score2 in range(100, len(solpath)):
		for score1 in range(score2 - 100):
			(r1, c1) = solpath[score1]
			(r2, c2) = solpath[score2]
			distance = abs(r1 - r2) + abs(c1 - c2)
			if distance <= 20 and score2 - score1 - distance >= 100:
				res += 1

	print(f"Res: {res}")

if __name__ == "__main__":
    exit(main())
