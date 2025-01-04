#!/bin/env python
# Solution is 18941802053

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
	for secret in secrets:
		for _ in range(2000):
			secret = calculate(secret)

		res += secret

	print(f"Res: {res}")

if __name__ == "__main__":
    exit(main())
