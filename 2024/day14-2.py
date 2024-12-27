#!/bin/env python
# Solution is 215987200

import re
import sys

def move(pos, velocity, steps, width, height):
	x = (pos[0] + (velocity[0] * steps)) % width
	y = (pos[1] + (velocity[1] * steps)) % height

	return (x, y)

def print_robots(robots, width, height):
	for y in range(height):
		for x in range(width):
			if (x, y) in robots:
				print('#', end='')
			else:
				print(" ", end='')
		print("")
	print("")

def has_cluster(robots):
	# Search for a cluster of 3x3 robots
	for pos in robots.keys():
		if (pos[0]+1, pos[1])   in robots and \
		   (pos[0]+2, pos[1])   in robots and \
		   (pos[0],   pos[1]+1) in robots and \
		   (pos[0]+1, pos[1]+1) in robots and \
		   (pos[0]+2, pos[1]+1) in robots and \
		   (pos[0],   pos[1]+2) in robots and \
		   (pos[0]+1, pos[1]+2) in robots and \
		   (pos[0]+2, pos[1]+2) in robots:
			   return True
	return False

def main():
	width = 101
	height = 103
	quads = [ 0, 0, 0, 0 ]
	robots = {}

	file = sys.argv[1] if len(sys.argv)>=2 else 'day14-input.txt'
	with open(file, 'r') as f:
		for line in f:
			m = re.match(r"^p=(\d+),(\d+) v=(-?\d+),(-?\d+)$", line)
			if m is not None:
				velocity = (int(m.group(3)), int(m.group(4)))
				pos = (int(m.group(1)), int(m.group(2)))
				if pos not in robots:
					robots[pos] = []
				robots[pos].append(velocity)

	for i in range(10000):
		new_positions = {}
		for p, vs in robots.items():
			for v in vs:
				pos = move(p, v, 1, width, height)
				if pos not in new_positions:
					new_positions[pos] = []
				new_positions[pos].append(v)

		if has_cluster(new_positions):
			print_robots(new_positions, width, height)
			print(f"Steps: {i+1}")
			return 0

		robots = new_positions

if __name__ == "__main__":
    exit(main())
