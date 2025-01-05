#!/bin/env python
# Solution is 1156

from collections import defaultdict
import sys

def main():
	servers = defaultdict(set)

	file = sys.argv[1] if len(sys.argv)>=2 else 'day23-input.txt'
	with open(file, 'r') as f:
		for line in f:
			s1, s2 = line[:-1].split('-')
			servers[s1].add(s2)
			servers[s2].add(s1)

	res = 0
	seen = set()
	for s1 in servers:
		if s1.startswith('t'):
			for s2 in servers[s1]:
				for s3 in servers[s2]:
					if s3 in servers[s1]:
						t = tuple(sorted((s1, s2, s3)))
						seen.add(t)

	print(f"Res: {len(seen)}")

if __name__ == "__main__":
    exit(main())
