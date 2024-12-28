#!/bin/env python
# Solution is 1548815

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

def is_movable(pos, direction, wh):
	r = pos[0]
	c = pos[1]
	dr = directions[direction][0]
	dc = directions[direction][1]

	# Check for first side of the box
	match wh[r+dr][c+dc]:
		case '.':
			res = True
		case '#':
			res = False
		case '[' | ']':
			res = is_movable((r+dr,c+dc), direction, wh)

	if res:
		# Check for other side of the box if needed
		box_side = 1 if wh[r][c] == '[' else -1
		match wh[r+dr][c+dc+box_side]:
			case '.':
				res = True
			case '#':
				res = False
			case '[' | ']':
				res = is_movable((r+dr,c+dc+box_side), direction, wh)

	return res

def move(pos, direction, wh):
	r = pos[0]
	c = pos[1]
	dr = directions[direction][0]
	dc = directions[direction][1]

	next_r = r + dr
	next_c = c + dc
	do_move = False
	v = wh[next_r][next_c]
	match v:
		case '#':
			pass
		case '.':
			do_move = True
		case '[' | ']':
			if direction == '<' or direction == '>':
				(mr, mc) = move((next_r, next_c), direction, wh)
				do_move = (mr, mc) != (next_r, next_c)
			else:
				do_move = is_movable((next_r, next_c), direction, wh)
				if do_move:
					box_side = 1 if v == '[' else -1
					(mr, mc) = move((next_r, next_c + box_side), direction, wh)
					(mr, mc) = move((next_r, next_c), direction, wh)

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
				new_r = []
				for col, c in enumerate(line[:-1]):
					match c:
						case 'O':
							new_r += ['[', ']']
						case '@':
							bot_pos = (row, len(new_r))
							new_r += ['@', '.']
						case _:
							new_r += [c, c]

				wh.append(new_r)
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
			if v == '[':
				res += 100 * r + c

	print_warehouse(wh)
	print(f"Res: {res}")

if __name__ == "__main__":
    exit(main())
