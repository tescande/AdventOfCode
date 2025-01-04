#!/bin/env python
# Solution part 1 is 157892
# Solution part 2 is 197015606336332

from functools import cache
from math import inf
import sys

num_keypad = {
	'7': (0, 0), '8': (0, 1), '9': (0, 2),
	'4': (1, 0), '5': (1, 1), '6': (1, 2),
	'1': (2, 0), '2': (2, 1), '3': (2, 2),
	'#': (3, 0), '0': (3, 1), 'A': (3, 2)
}

dir_keypad = {
	'#': (0, 0), '^': (0, 1), 'A': (0, 2),
	'<': (1, 0), 'v': (1, 1), '>': (1, 2)
}

def check_path(keypad, start, moves):
	directions = { '<': (0, -1), '^': (-1, 0), '>': (0, 1), 'v': (1, 0) }

	pos = start
	for m in moves:
		d = directions[m]
		pos = (pos[0] + d[0], pos[1] + d[1])
		if pos == keypad['#']:
			return False

	return True

@cache
def get_moves_length(code, n_iter, max_iter):
	res = 0

	if n_iter > max_iter:
		return len(code)

	keypad = dir_keypad if n_iter else num_keypad
	pos = keypad['A']

	for c in code:
		key = keypad[c]
		dr = key[0] - pos[0]
		dc = key[1] - pos[1]

		moves = ""
		if dr < 0:
			moves += '^' * abs(dr)
		elif dr > 0:
			moves += 'v' * abs(dr)
		if dc < 0:
			moves += '<' * abs(dc)
		elif dc > 0:
			moves += '>' * abs(dc)

		# Test the move and its reversed version (i.e. <<v and v<<)
		# If one move goes through the keypad empty slot, its reversed won't.
		# Also turns out that testing only a path and its reversed give the
		# shortest path too
		min_length = inf
		for m in [moves, moves[::-1]]:
			if check_path(keypad, pos, list(m)):
				l = get_moves_length(m + 'A', n_iter + 1, max_iter)
				min_length = min(min_length, l)

		res += min_length
		pos = key

	return res

def main():
	codes = []

	file = sys.argv[1] if len(sys.argv)>=2 else 'day21-input.txt'
	with open(file, 'r') as f:
		for line in f:
			codes.append(line[:-1])

	res_p1 = 0
	res_p2 = 0
	for code in codes:
		length = get_moves_length(code, 0, 2)
		# ~ print(f"{length} * {int(code[:-1])} = {length * int(code[:-1])}")
		res_p1 += length * int(code[:-1])

		length = get_moves_length(code, 0, 25)
		# ~ print(f"{length} * {int(code[:-1])} = {length * int(code[:-1])}")
		res_p2 += length * int(code[:-1])

	print(f"Res part 1: {res_p1}")
	print(f"Res part 2: {res_p2}")

if __name__ == "__main__":
    exit(main())
