#!/bin/env python
# Solution is 40069

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

	res = 0
	for m in machines:
		lines = m.splitlines()
		try:
			button_a = parse_machine_line(lines[0], r"^Button A: X\+(\d+), Y\+(\d+)$")
			button_b = parse_machine_line(lines[1], r"^Button B: X\+(\d+), Y\+(\d+)$")
			prize = parse_machine_line(lines[2], r"^Prize: X=(\d+), Y=(\d+)$")
		except Exception as e:
			print(e)
			return 0

		res += solve(button_a, button_b, prize)

	print(f"Res: {res}")

if __name__ == "__main__":
    exit(main())
