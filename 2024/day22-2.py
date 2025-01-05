#!/bin/env python
# Solution is 2218

import sys

def calculate(secret):
	secret = ((secret <<  6) ^ secret) & 0xffffff
	secret = ((secret >>  5) ^ secret) & 0xffffff
	secret = ((secret << 11) ^ secret) & 0xffffff

	return secret

def main():
	secrets = []

	file = sys.argv[1] if len(sys.argv)>=2 else 'day22-input.txt'
	with open(file, 'r') as f:
		for line in f:
			secrets.append(int(line[:-1]))

	res = 0
	bananas = {}
	for secret in secrets:
		sequence = []
		seen = set()
		for _ in range(2000):
			n_secret = calculate(secret)

			price = secret % 10
			n_price = n_secret % 10

			sequence.append(n_price - price)
			if len(sequence) > 3:
				# list type is not hashable for set() and dict() entries
				t_seq = tuple(sequence)
				if t_seq not in seen:
					seen.add(t_seq)
					if not bananas.get(t_seq):
						bananas[t_seq] = 0
					bananas[t_seq] += n_price
				sequence.pop(0)

			secret = n_secret

	print(f"Res: {max(bananas.values())}")

if __name__ == "__main__":
    exit(main())
