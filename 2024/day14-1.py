#!/bin/env python
# Solution is 215987200

import re
import sys

def move(pos, velocity, steps, width, height):
	x = (pos[0] + (velocity[0] * steps)) % width
	y = (pos[1] + (velocity[1] * steps)) % height

	return (x, y)

def main():
	# ~ width = 11
	# ~ height = 7
	width = 101
	height = 103
	quads = [ 0, 0, 0, 0 ]

	file = sys.argv[1] if len(sys.argv)>=2 else 'day14-input.txt'
	with open(file, 'r') as f:
		for line in f:
			m = re.match(r"^p=(\d+),(\d+) v=(-?\d+),(-?\d+)$", line)
			if m is not None:
				velocity = (int(m.group(3)), int(m.group(4)))
				pos = move((int(m.group(1)), int(m.group(2))),
					   velocity, 100, width, height)

				if pos[0] < width // 2:
					if pos[1] < height // 2:
						quads[0] += 1
					elif pos[1] > height // 2:
						quads[2] += 1
				elif pos[0] > width // 2:
					if pos[1] < height // 2:
						quads[1] += 1
					elif pos[1] > height // 2:
						quads[3] += 1

	print(f"Res: {quads[0] * quads[1] * quads[2] * quads[3]}")

if __name__ == "__main__":
    exit(main())
