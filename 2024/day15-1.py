#!/bin/env python
# Solution is 1509863

import re
import sys

directions = {
	'^': (-1,  0),
	'>': ( 0,  1),
	'v': ( 1,  0),
	'<': ( 0, -1),
}

def print_warehouse(wh):
	for line in wh:
		print(''.join(line))
	print("")

def move(pos, direction, wh):
	r = pos[0]
	c = pos[1]
	dr = directions[direction][0]
	dc = directions[direction][1]

	next_r = r + dr
	next_c = c + dc
	do_move = False
	match wh[next_r][next_c]:
		case '#':
			pass
		case '.':
			do_move = True
		case 'O':
			(mr, mc) = move((next_r, next_c), direction, wh)
			do_move = (mr, mc) != (next_r, next_c)

	if do_move:
		wh[next_r][next_c] = wh[r][c]
		wh[r][c] = '.'

	return (next_r, next_c) if do_move else (r, c)

def main():
	wh = []
	moves = []
	row = col = 0
	bot_pos = None

	file = sys.argv[1] if len(sys.argv)>=2 else 'day15-input.txt'
	with open(file, 'r') as f:
		for row, line in enumerate(f):
			m = re.match(r"^#.*$", line)
			if m is not None:
				if bot_pos is None:
					col = line.find("@")
					if col >= 0:
						bot_pos = (row, col)
				wh.append(list(line[:-1]))
				continue

			m = re.match(r"^[\^v<>].*$", line)
			if m is not None:
				moves += list(line[:-1])
				continue

	print_warehouse(wh)

	for m in moves:
		bot_pos = move(bot_pos, m, wh)

	res = 0
	for r, line in enumerate(wh):
		for c, v in enumerate(line):
			if v == 'O':
				res += 100 * r + c

	print_warehouse(wh)
	print(f"Res: {res}")

if __name__ == "__main__":
    exit(main())
