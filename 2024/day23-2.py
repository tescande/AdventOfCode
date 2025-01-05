#!/bin/env python
# Solution is bx,cx,dr,dx,is,jg,km,kt,li,lt,nh,uf,um

from collections import defaultdict
import sys

# From https://en.wikipedia.org/wiki/Bron%E2%80%93Kerbosch_algorithm
# algorithm BronKerbosch1(R, P, X) is
# if P and X are both empty then
# 	report R as a maximal clique
# for each vertex v in P do
# 	BronKerbosch1(R | {v}, P & N(v), X & N(v))
# 	P := P ^ {v}
# 	X := X | {v}
def bron_kerbosch(neighbors, R, P, X):
	if not P and not X:
		return R

	clique = set()
	for v in P.copy():
		n_clique = bron_kerbosch(neighbors, R | {v}, P & neighbors[v], X & neighbors[v])
		if len(n_clique) > len(clique):
			clique = n_clique
		P ^= {v}
		X |= {v}

	return clique

def main():
	neighbors = defaultdict(set)

	file = sys.argv[1] if len(sys.argv)>=2 else 'day23-input.txt'
	with open(file, 'r') as f:
		for line in f:
			s1, s2 = line[:-1].split('-')
			neighbors[s1].add(s2)
			neighbors[s2].add(s1)

	clique = bron_kerbosch(neighbors, set(), set(neighbors.keys()), set())
	print(f"Res: {','.join(sorted(clique))}")

if __name__ == "__main__":
    exit(main())
