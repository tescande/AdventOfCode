#!/usr/bin/env python
# Solution part 1 is 304
# Solution part 2 is 705756472327497

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

	res_p1 = 0
	res_p2 = 0
	for towel in towels.strip().split('\n'):
		res = match_count(towel)
		res_p2 += res
		if res:
			res_p1 += 1

	print(f"Res part 1: {res_p1}")
	print(f"Res part 2: {res_p2}")

if __name__ == "__main__":
	exit(main())
