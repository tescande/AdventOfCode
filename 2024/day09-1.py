#!/bin/env python
# Solution is 6200294120911

import sys

def main():
	chksum = 0
	file = sys.argv[1] if len(sys.argv)>=2 else 'day09-input.txt'
	with open(file, 'r') as f:
		disk_map = list(map(int, f.readline()[:-1]))

	last_file_index = len(disk_map) - 1
	if last_file_index & 1:
		last_file -= 1

	blocks_map_index = 0
	for i, n in enumerate(disk_map):
		if i >= last_file_index + 1:
			break

		while n > 0:
			# Free blocks
			if i & 0x1:
				while disk_map[last_file_index] == 0:
					last_file_index -= 2
				disk_map[last_file_index] -= 1
				file_id = last_file_index // 2
			else:
				file_id = i // 2

			# ~ print(file_id, end='')
			chksum += blocks_map_index * file_id
			blocks_map_index += 1
			n -= 1

	# ~ print("")

	print(f"checksum: {chksum}")

if __name__ == "__main__":
    exit(main())
