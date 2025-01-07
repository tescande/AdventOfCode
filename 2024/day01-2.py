#!/bin/env python
# Solution is 24869388

import sys

left = []
right = []

file = sys.argv[1] if len(sys.argv)>=2 else 'day01-input.txt'
with open(file, 'r') as f:
	for line in f:
		vals = line.split()
		left.append(int(vals[0]))
		right.append(int(vals[1]))
left.sort()
right.sort()
dist = 0
for l in left:
	count = 0
	for r in right:
		if r == l:
			count += 1
		elif r > l:
			break
	dist += l * count

print(dist)
