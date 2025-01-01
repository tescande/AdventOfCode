#!/usr/bin/env python
# Solution is 304

from functools import cache
import sys

def main():
	filename = sys.argv[1] if len(sys.argv)>=2 else 'day19-input.txt'
	file = open(filename, 'r').read()

	patterns, towels = file.split('\n\n')
	patterns = set(patterns.split(', '))

	@cache
	def match_count(towel):
		if not towel:
			return 1

		res = 0
		for p in patterns:
			if towel.startswith(p):
				res += match_count(towel[len(p):])

		return res

	res = 0
	for towel in towels.strip().split('\n'):
		if match_count(towel):
			res += 1

	print(f"Res: {res}")

if __name__ == "__main__":
	exit(main())
