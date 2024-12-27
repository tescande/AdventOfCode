#!/bin/env python
# Solution part 1 is 40069
# Solution part 2 is 71493195288102

import re
import sys
import numpy as np

def parse_machine_line(line, regex):
	m = re.match(regex, line)
	if m is None:
		raise Exception(f"Invalid line: {line}")

	return { 'x': int(m.group(1)), 'y': int(m.group(2)) }


def solve(button_a, button_b, prize):
	b1 = button_b['x'] * button_a['y']
	b2 = button_b['y'] * button_a['x']
	db = b1 - b2
	x = prize['x'] * button_a['y']
	y = prize['y'] * button_a['x']
	dxy = x - y

	if dxy % db:
		return 0
	b = dxy // db

	if (prize['x'] - button_b['x'] * b) % button_a['x']:
		return 0
	a = (prize['x'] - button_b['x'] * b) // button_a['x']

	return a * 3 + b

def main():
	machines = []
	file = sys.argv[1] if len(sys.argv)>=2 else 'day13-input.txt'
	with open(file, 'r') as f:
		machines = f.read().strip().split("\n\n")

	res_p1 = 0
	res_p2 = 0
	for m in machines:
		lines = m.splitlines()
		try:
			button_a = parse_machine_line(lines[0], r"^Button A: X\+(\d+), Y\+(\d+)$")
			button_b = parse_machine_line(lines[1], r"^Button B: X\+(\d+), Y\+(\d+)$")
			prize_p1 = parse_machine_line(lines[2], r"^Prize: X=(\d+), Y=(\d+)$")
			prize_p2 = { 'x': prize_p1['x'] + 10000000000000, 'y': prize_p1['y'] + 10000000000000 }
		except Exception as e:
			print(e)
			return 0

		res_p1 += solve(button_a, button_b, prize_p1)
		res_p2 += solve(button_a, button_b, prize_p2)

	print(f"Part 1: {res_p1}")
	print(f"Part 2: {res_p2}")

if __name__ == "__main__":
    exit(main())
