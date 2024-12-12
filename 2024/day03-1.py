#!/bin/env python
# Solution 167650499

import re
import sys

def main():
	res = 0
	file = sys.argv[1] if len(sys.argv)>=2 else 'day03-input.txt'
	file = open(file, 'r').read()

	for mul in re.finditer(r"mul\([\d]{1,3},[\d]{1,3}\)", file):
		values = re.findall(r"\d+", mul.group(0))
		res += int(values[0]) * int(values[1])

	print(f"res: {res}")

if __name__ == "__main__":
    exit(main())
